// SPDX-License-Identifier: GPL3
pragma solidity ^0.8;

import '../interfaces/IERC20.sol';
import '../interfaces/IChessTable.sol';

import './ChessTable.sol';
import './libraries/SafeMath.sol';


contract ChessLobby {
    using SafeMath for uint;

    string public constant name = "lobby-test-01";
    uint8  public constant maxTableCount = 3;
    uint8  public constant maxWaitingListLength = 10;

    bytes4 private constant SELECTOR = bytes4(keccak256(bytes('transfer(address,uint256)')));

    address public house;
    address public chessToken;
    address public freeTable;
    uint8 public waitingListLength;
    uint8 public tableCounter;

    address[maxTableCount] public tables;
    //assuming each player can sit only on one table
    mapping(address => address) public playerToTable;
    mapping(address => address[2]) public tableToPlayers;
    mapping(address => uint8) public tableToState;
    mapping(uint8 => address) public WaitingIndexToPlayer;

    // supporting only its own token right now
    mapping(address => uint) public credits;
    mapping(address => uint) public nonces;

    event TableCreated(address indexed table, uint8 indexed tableCounter);
    event TableInitialized(address indexed table, uint result);

    event PlayerDeposited(address indexed player, uint amount);
    event PlayerSit(address indexed player, uint8 waitingListLength);

    constructor(address chessTokenAddress) public {
        waitingListLength = 0;
        chessToken = chessTokenAddress;
        house = msg.sender;

        uint tableOneConfig = 0x0;
        _createTable(tableOneConfig);

        uint tableTwoConfig = 0x0;
        _createTable(tableTwoConfig);

    }

    function _safeTransferFrom(
        IERC20 token,
        address sender,
        address recipient,
        uint amount
    ) private {
        bool sent = token.transferFrom(sender, recipient, amount);
        require(sent, "ChessLobby: TOKEN_TRANSFER_FAILED");
    }

    function _deposit(address player, uint value) private {
        _safeTransferFrom(IERC20(chessToken), player, address(this), value);
        credits[player] = credits[player] + value;
        emit PlayerDeposited(player, value);
        // (bool success, bytes memory data) = token.call(abi.encodeWithSelector(SELECTOR, to, value));
        // require(success && (data.length == 0 || abi.decode(data, (bool))), 'ChessLobby: DEPOSIT_FAILED');
    }

    function _cashout(address player, uint value) private {
        (bool success, bytes memory data) = chessToken.call(abi.encodeWithSelector(SELECTOR, player, value));
        require(success && (data.length == 0 || abi.decode(data, (bool))), 'ChessLobby: CASHOUT_FAILED');
    }

    function _createTable(uint options) private returns (address){
        require(tableCounter < maxTableCount - 1, 'ChessLobby: OUT_OF_TABLE');
        bytes memory bytecode = type(ChessTable).creationCode;
        bytes32 salt = keccak256(abi.encodePacked(tableCounter));
        address newTable = address(0x0);
        assembly {
            newTable := create2(0, add(bytecode, 32), mload(bytecode), salt)
        }
        tableToState[newTable] = 0x01;

        // any new table is a free table
        freeTable = newTable;
        emit TableCreated(newTable, tableCounter);
        tableCounter = tableCounter + 1;

        return newTable;
    }

    function _findFreeTable() private returns (address){
        return freeTable;
    }

    function _sitAndWait(address player, uint options) private {
        // TODO:: this waitingList only matches the waitingplayer with the first coming player
        // later it would be added to waitingList and selected randomly
        emit PlayerSit(player, waitingListLength);
        if(waitingListLength % 2 == 1){
            address player1 = WaitingIndexToPlayer[waitingListLength - 1];
            address player2 = player;
            require(player1 != player2, 'ChessLobby: IDENTICAL_ADDRESSES');

            address newTable = _findFreeTable();
            IChessTable(newTable).initialize(player1, player2);
            emit TableInitialized(newTable, 0x0); 

            credits[player1] -= 100;
            credits[player2] -= 100;
            playerToTable[player1] = newTable;
            playerToTable[player2] = newTable;
            tableToPlayers[newTable] = [player1, player2];

            delete WaitingIndexToPlayer[waitingListLength - 1];
            waitingListLength = waitingListLength - 1;

        }
        else{
            WaitingIndexToPlayer[waitingListLength] = player;
            waitingListLength = waitingListLength + 1;
        }
        emit PlayerSit(player, waitingListLength);

    }


    function sitAndWait(uint options) external returns (bool) {
        // Player must not be sitting on a table
        require(playerToTable[msg.sender] == address(0x0) , "ChessLobby: ALREADY_IN_GAME");
        
        // Player must have sufficient credit
        // TODO:: 0 is buggy, we should calculate min credit required to play
        require(credits[msg.sender] >= 100 , "ChessLobby: INSUFFICIENT_CREDIT");
        
        require(waitingListLength < maxWaitingListLength, "ChessLobby: FULL_WAITING_LIST");

        _sitAndWait(msg.sender, options);
        return true;
    }

    function deposit(uint256 _value) external returns (bool) {
        require(
            IERC20(chessToken).allowance(msg.sender, address(this)) >= _value,
            "ChessLobby: LOW_ALLOWANCE"
        );
        _deposit(msg.sender, _value);
        return true;
    }

    function cashout(uint value) external returns (bool) {
        require(credits[msg.sender] >= value, "NOT_ENOUGH_CREDIT");
        _cashout(msg.sender, value);
        return true;
    }

}



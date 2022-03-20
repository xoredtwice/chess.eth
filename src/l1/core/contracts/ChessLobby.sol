// SPDX-License-Identifier: GPL3
pragma solidity ^0.8;

import '../interfaces/IERC20.sol';
import '../interfaces/IChessBoard.sol';

import './ChessBoard.sol';
import './libraries/SafeMath.sol';


contract ChessLobby {
    using SafeMath for uint;

    string public constant name = "lobby-test-01";
    uint8  public constant maxBoardCount = 3;
    uint8  public constant maxWaitingListLength = 10;

    bytes4 private constant SELECTOR = bytes4(keccak256(bytes('transfer(address,uint256)')));

    address public house;
    address public chessToken;
    address public freeBoard;
    uint8 public waitingListLength;
    uint8 public boardCounter;

    address[maxBoardCount] public boards;
    //assuming each player can sit only on one board
    mapping(address => address) public playerToBoard;
    mapping(address => address[2]) public boardToPlayers;
    mapping(address => uint8) public boardToState;
    mapping(uint8 => address) public WaitingIndexToPlayer;

    // supporting only its own token right now
    mapping(address => uint) public credits;
    mapping(address => uint) public nonces;

    event BoardCreated(address indexed board, uint8 indexed boardCounter);
    event PlayerDeposited(address indexed player, uint amount);
    event PlayerSit(address indexed player, uint8 waitingListLength);
    event GameStarted(address indexed board, address indexed player1, address indexed player2, uint meta);
    event GameEnded(address indexed board, uint result);

    constructor(address chessTokenAddress) public {
        waitingListLength = 0;
        chessToken = chessTokenAddress;
        house = msg.sender;

        uint boardOneConfig = 0x0;
        _createBoard(boardOneConfig);

        uint boardTwoConfig = 0x0;
        _createBoard(boardTwoConfig);

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
        // _safeTransferFrom(IERC20(chessToken), player, address(this), value);
        credits[player] = credits[player] + value;
        emit PlayerDeposited(player, value);
        // (bool success, bytes memory data) = token.call(abi.encodeWithSelector(SELECTOR, to, value));
        // require(success && (data.length == 0 || abi.decode(data, (bool))), 'ChessLobby: DEPOSIT_FAILED');
    }

    function _cashout(address player, uint value) private {
        (bool success, bytes memory data) = chessToken.call(abi.encodeWithSelector(SELECTOR, player, value));
        require(success && (data.length == 0 || abi.decode(data, (bool))), 'ChessLobby: CASHOUT_FAILED');
    }

    function _createBoard(uint options) private returns (address){
        require(boardCounter < maxBoardCount - 1, 'ChessLobby: OUT_OF_BOARD');
        bytes memory bytecode = type(ChessBoard).creationCode;
        bytes32 salt = keccak256(abi.encodePacked(boardCounter));
        address board = address(0x0);
        assembly {
            board := create2(0, add(bytecode, 32), mload(bytecode), salt)
        }
        boardToState[board] = 0x01;

        // any new board is a free board
        freeBoard = board;
        emit BoardCreated(board, boardCounter);
        boardCounter = boardCounter + 1;

        return board;
    }

    function _findFreeBoard() private returns (address){
        return freeBoard;
    }

    function _sitAndWait(address player, uint options) private {
        // TODO:: this waitingList only matches the waitingplayer with the first coming player
        // later it would be added to waitingList and selected randomly
        if(waitingListLength % 2 == 1){
            address player1 = WaitingIndexToPlayer[waitingListLength - 1];
            address player2 = player;
            require(player1 != player2, 'ChessLobby: IDENTICAL_ADDRESSES');

            address newBoard = _findFreeBoard();
            IChessBoard(newBoard).initialize(player1, player2);
            playerToBoard[player1] = newBoard;
            playerToBoard[player2] = newBoard;
            boardToPlayers[newBoard] = [player1, player2];

            delete WaitingIndexToPlayer[waitingListLength - 1];
            waitingListLength = waitingListLength - 1;

            emit GameStarted(newBoard, player1, player2, 0x0); 
        }
        else{
            WaitingIndexToPlayer[waitingListLength] = player;
            waitingListLength = waitingListLength + 1;
        }

    }


    function sitAndWait(uint options) external returns (bool) {
        // Player must not be sitting on a board
        require(playerToBoard[msg.sender] == address(0x0) , "ChessLobby: ALREADY_IN_GAME");
        
        // Player must have sufficient credit
        // TODO:: 0 is buggy, we should calculate min credit required to play
        require(credits[msg.sender] == 0 , "ChessLobby: INSUFFICIENT_CREDIT");
        
        require(waitingListLength < maxWaitingListLength, "ChessLobby: FULL_WAITING_LIST");

        _sitAndWait(msg.sender, options);
        return true;
    }

    function deposit(uint256 _value) external returns (bool) {
        require(
            IERC20(chessToken).allowance(msg.sender, house) >= _value,
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



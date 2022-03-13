pragma solidity ^0.8;

import '../interfaces/IERC20.sol';
import './libraries/SafeMath.sol';

contract Lobby {
    using SafeMath for uint;

    string public constant name = "lobby-test-01"
    uint8  public constant maxBoards = 2;
    uint8  public constant maxWaitingListLength = 10;

    bytes4 private constant SELECTOR = bytes4(keccak256(bytes('transfer(address,uint256)')));

    address public generosity;
    address public freeBoard;
    uint8 public waitingListLength;

    //assuming each player can sit only on one board
    mapping(address => address) public playerToBoard;
    mapping(address => mapping(address => address)) public boardToPlayers;
    mapping(address => uint8) public boardToState;
    mapping(address => uint8) public WaitingIndexToPlayer;

    // supporting only its own token right now
    mapping(address => uint) public credits;
    mapping(address => uint) public nonces;

    event BoardCreated(address indexed board);
    event PlayerDeposited(address indexed player, uint amount);
    event PlayerSit(address indexed player, uint8 waitingListLength);
    event GameStarted(address indexed board, address indexed player1, address indexed player2, uint meta);
    event GameEnded(address indexed board, uint result);

    constructor(address chessToken) public {
        waitingListLength = 0;
        generosity = chessTokenAddress;

        uint8 constant boardOneConfig = 0x0;
        _createBoard("gary", boardOneConfig);

        uint8 constant boardTwoConfig = 0x0;
        _createBoard("magnus", boardOneConfig);

    }

    function _deposit(address owner, address spender, uint value) private {
        (bool success, bytes memory data) = token.call(abi.encodeWithSelector(SELECTOR, to, value));
        require(success && (data.length == 0 || abi.decode(data, (bool))), 'ChessLobby: DEPOSIT_FAILED');
    }

    function _cashout(address owner, address spender, uint value) private {
        (bool success, bytes memory data) = token.call(abi.encodeWithSelector(SELECTOR, to, value));
        require(success && (data.length == 0 || abi.decode(data, (bool))), 'ChessLobby: CASHOUT_FAILED');
    }

    function _createBoard(uint options) private {
        bytes memory bytecode = type(ChessBoard).creationCode;
        bytes32 salt = keccak256(abi.encodePacked(options));
        assembly {
            board := create2(0, add(bytecode, 32), mload(bytecode), salt)
        }
        emit BoardCreated(board, boards.length);
    }

    function _getFreeBoard() private{

    }

    function _sitAndWait(address player, uint8 options) private {
        // TODO:: this waitingList only matches the waitingplayer with the first coming player
        // later it would be added to waitingList and selected randomly
        if(waitingListLength % 2 == 1){
            address constant player1 = WaitingIndexToPlayer[waitingListLength - 1];
            address constant player2 = player;
            require(player1 != player2, 'ChessLobby: IDENTICAL_ADDRESSES');

            address constant freeBoard = _getFreeBoard()
            IChessBoard(freeBoard).initialize(player1, player2);
            playerToBoard[player1] = freeBoard;
            playerToBoard[player2] = freeBoard;

            delete WaitingIndexToPlayer[waitingListLength - 1];
            waitingListLength = waitingListLength - 1;

            emit GameStarted(freeBoard, player1, player2, 0x0); 
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
        // TODO:: 0 is buggy, we should calculate mix credit required to play
        require(credit[msg.sender] == 0 , "ChessLobby: INSUFFICIENT_CREDIT");
        
        require(waitingListLength < maxWaitingListLength, "ChessLobby: FULL_WAITING_LIST");

        _sitAndWait(msg.sender, options);
        return true;
    }

    function deposit(uint value) external returns (bool) {
        _deposit(msg.sender, spender, value);
        return true;
    }

    function cashout(uint value) external returns (bool) {
        _deposit(msg.sender, spender, value);
        return true;
    }

}



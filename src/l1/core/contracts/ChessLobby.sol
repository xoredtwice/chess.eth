pragma solidity ^0.8;

import '../interfaces/IERC20.sol';
import './libraries/SafeMath.sol';

contract Lobby {
    using SafeMath for uint;

    string public constant name = "lobby-test-01"
    uint8  public constant maxBoards = 2;

    address public generosity;
    //assuming each player can sit only on one board
    mapping(address => address) public playerToBoard;
    mapping(address => (address, address)) public boardToPlayers;

    // supporting only its own token right now
    mapping(address => uint) public credits;
    mapping(address => uint) public nonces;

    event BoardCreated(address indexed board);
    event PlayerDeposited(address indexed player, uint amount);
    event PlayerSit(address indexed player, address indexed board);
    event GameStarted(address indexed board, address indexed white, address indexed black, uint meta);
    event GameEnded(address indexed board, uint result);

    bytes4 private constant SELECTOR = bytes4(keccak256(bytes('transfer(address,uint256)')));

    constructor(address chessToken) public {
        generosity = chessTokenAddress;
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
        emit BoardCreated(token0, token1, pair, allPairs.length);

    }

    function _sitAndWait(address player, address board) private {

        require(player1 != player2, 'ChessLobby: IDENTICAL_ADDRESSES');
        require(IChessBoard(board).getState() == 0, "ChessLobby: BOARD_BUSY");

        playerToBoard[player1] = board;
        playerToBoard[player2] = board;

        IChessBoard(board).initialize(player1, player2);

    }

    function createBoard(uint options) external returns (bool){
        // check whether options are valid or not

    }

    function deposit(uint value) external returns (bool) {
        _deposit(msg.sender, spender, value);
        return true;
    }

    function sitAndWait(address board, uint options) external returns (bool) {
        require(playerToBoard[msg.sender] == address(0x0) , "ChessLobby, ALREADY_IN_GAME");
        // TODO:: 0 is buggy, we should calculate mix credit required to play
        require(credit[msg.sender] == 0 , "ChessLobby, INSUFFICIENT_CREDIT");

        _sitAndWait(msg.sender, board, options);
        return true;
    }

    function cashout(uint value) external returns (bool) {
        _deposit(msg.sender, spender, value);
        return true;
    }

}



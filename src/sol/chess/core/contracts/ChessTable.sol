// SPDX-License-Identifier: GPL3
pragma solidity ^0.8;

import './libraries/SafeMath.sol';
import '../interfaces/IERC20.sol';
import '../interfaces/IChessTable.sol';

contract ChessTable is IChessTable{
    using SafeMath  for uint;

    // The longest tournament chess game (in terms of moves) is 269 moves 
    // (Nikolic-Arsovic, Belgrade 1989). The game ended in a draw after 
    // over 20 hours of play. 10 games have been 200 moves or over in 
    // tournament play. In theory, the longest chess game can go up to 
    // 5,949 moves.
    uint16 public constant MAX_MOVES = 400;
    
    // FromTo encoding    
    uint16 public constant FROM_MASK = 0xFC00;
    uint16 public constant FROM_FILE_MASK = 0xE000;
    uint16 public constant FROM_RANK_MASK = 0x1C00;

    uint16 public constant TO_MASK = 0x03F0;
    uint16 public constant TO_FILE_MASK = 0x0380;
    uint16 public constant TO_RANK_MASK = 0x0070;

    uint16 public constant META_MASK = 0x000F; //lol

    // piece encoding
    uint8 public constant PIECE_PAWN = 0x10;
    uint8 public constant PIECE_KING = 0x50;

    uint8 public constant PIECE_KNIGHT = 0x30;

    // Queen moves Bishop + Rook
    uint8 public constant PIECE_BISHOP = 0x20;
    uint8 public constant PIECE_ROOK = 0x40;
    uint8 public constant PIECE_QUEEN = 0x60;

    uint8 public constant COLOR_WHITE = 0x00;
    uint8 public constant COLOR_BLACK = 0xE0;

    uint8 public constant WH_P = COLOR_WHITE | PIECE_PAWN;
    uint8 public constant WH_N = COLOR_WHITE | PIECE_KNIGHT;
    uint8 public constant WH_B = COLOR_WHITE | PIECE_BISHOP;
    uint8 public constant WH_R = COLOR_WHITE | PIECE_ROOK;
    uint8 public constant WH_Q = COLOR_WHITE | PIECE_QUEEN;
    uint8 public constant WH_K = COLOR_WHITE | PIECE_KING;
    
    uint8 public constant BL_P = COLOR_BLACK | PIECE_PAWN;
    uint8 public constant BL_N = COLOR_BLACK | PIECE_KNIGHT;
    uint8 public constant BL_B = COLOR_BLACK | PIECE_BISHOP;
    uint8 public constant BL_R = COLOR_BLACK | PIECE_ROOK;
    uint8 public constant BL_Q = COLOR_BLACK | PIECE_QUEEN;
    uint8 public constant BL_K = COLOR_BLACK | PIECE_KING;

    string public name;
    address public lobby;
    address public white;
    address public black;
    address public turn;
    
    uint public activeGame;
    uint16 public lastMove;
    uint8 public state;


    // square to piece
    mapping (uint8 => uint8) public piece;
    
    // square to squares
    mapping (uint8 => uint8[]) public paths;

    // square to squares
    mapping (uint8 => uint8[]) public enemies;

    // square to squares
    mapping (uint8 => uint8) public allies;

    uint private unlocked = 1;
    uint16[] private moves;

    modifier lock() {
        require(unlocked == 1, 'ChessTable: LOCKED');
        unlocked = 0;
        _;
        unlocked = 1;
    }

    constructor() public {
        lobby = msg.sender;
        name = "gary";
        // initial state
    }


    // called once by the lobby at time of deployment
    function _initialize(address _player1, address _player2, uint8 meta) private {
        white = _player1;
        black = _player2;
        turn = white;
        state = 0x10;

        // piece[]
        emit GameStarted(white, black, meta);

    }

    function _logic(uint8 _from, uint8 _to , uint8 _meta) private {
        // 

        // board[][]
    }

    function _move(address _player, uint16 _newMove, uint8 _from, uint8 _to , uint8 _meta) private{   


        _logic(_from, _to, _meta);
        lastMove = _newMove; 
        moves.push(lastMove);

        // TODO:: it can be done through flipping the addresses too.
        turn = moves.length % 2 == 0 ? white : black;

        emit PlayerMoved(_player, _newMove, state);
    }

    function getBoard() external view returns(uint16[] memory){

    }

    function initialize(address _player1, address _player2, uint8 meta) external returns (bool) {
        require(msg.sender == lobby, 'ChessTable: NOT_AUTHORIZED');
        _initialize(_player1, _player2, meta);
        return true;
    }

    function move(uint16 newMove) external returns (bool) {
        require(state >= 0x10, 'ChessTable: STATE_MISMATCH');
        
        // TODO:: the maxed out game's result must get resolved.
        require(moves.length < MAX_MOVES, 'ChessTable: MOVE_OVERFLOW');
        
        // checking the turn condition
        require(msg.sender == turn, 'ChessTable: NOT_YOUR_TURN');
        
        uint8 _from = (uint8)((newMove & FROM_MASK) >> 8);
        uint8 _to = (uint8)((newMove & TO_MASK) >> 8);
        uint8 _meta = (uint8)((newMove & META_MASK) >> 8);

        // player should not be able to move other player's pieces
        address pieceOwner = (piece[_from] & COLOR_BLACK == 0 ? white : black);
        require( msg.sender == pieceOwner, 'ChessTable: NOT_YOUR_PIECE');

        _move(pieceOwner, newMove, _from, _to, _meta);
        return true;
    }
}
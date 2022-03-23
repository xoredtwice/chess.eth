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
    
    uint8 public constant PIECE_MASK = 0xF0;
    
    uint8 public constant FROM_MASK = 0x0F;
    uint8 public constant FROM_RANK_MASK = 0x0C;
    uint8 public constant FROM_FILE_MASK = 0x03;

    uint8 public constant TO_MASK = 0xF0;
    uint8 public constant TO_RANK_MASK = 0xC0;
    uint8 public constant TO_FILE_MASK = 0x30;

    uint8 public constant PIECE_PAWN = 0x10;
    uint8 public constant PIECE_KING = 0x50;

    uint8 public constant PIECE_KNIGHT = 0x30;

    // Queen moves Bishop + Rock
    uint8 public constant PIECE_BISHOP = 0x20;
    uint8 public constant PIECE_ROCK = 0x40;
    uint8 public constant PIECE_QUEEN = 0x60;

    uint8 public constant COLOR_WHITE = 0x00;
    uint8 public constant COLOR_BLACK = 0x08;

    uint8 public constant WH_P = COLOR_WHITE | PIECE_PAWN;
    uint8 public constant WH_N = COLOR_WHITE | PIECE_KNIGHT;
    uint8 public constant WH_B = COLOR_WHITE | PIECE_BISHOP;
    uint8 public constant WH_R = COLOR_WHITE | PIECE_ROCK;
    uint8 public constant WH_Q = COLOR_WHITE | PIECE_QUEEN;
    uint8 public constant WH_K = COLOR_WHITE | PIECE_KING;
    
    uint8 public constant BL_P = COLOR_BLACK | PIECE_PAWN;
    uint8 public constant BL_N = COLOR_BLACK | PIECE_KNIGHT;
    uint8 public constant BL_B = COLOR_BLACK | PIECE_BISHOP;
    uint8 public constant BL_R = COLOR_BLACK | PIECE_ROCK;
    uint8 public constant BL_Q = COLOR_BLACK | PIECE_QUEEN;
    uint8 public constant BL_K = COLOR_BLACK | PIECE_KING;
    
    // mapping uint8 => ();

    string public name;
    address public lobby;
    address public white;
    address public black;
    address public turn;
    
    uint public activeGame;
    uint16 public lastMove;
    uint8 public state;
    uint8[8][8] public board;

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
    }

    // called once by the factory at time of deployment
    function _initialize(address _player1, address _player2, uint8 meta) private {
        white = _player1;
        black = _player2;
        turn = white;
        state = 0x10;
        board[7] = [BL_R, BL_N, BL_B, BL_Q, BL_K, BL_B, BL_N, BL_R];
        board[6] = [BL_P, BL_P, BL_P, BL_P, BL_P, BL_P, BL_P, BL_P];

        board[1] = [WH_P, WH_P, WH_P, WH_P, WH_P, WH_P, WH_P, WH_P];
        board[0] = [WH_R, WH_N, WH_B, WH_Q, WH_K, WH_B, WH_N, WH_R];
        emit GameStarted(white, black, meta);

    }

    // function _logic(uint8 _from, uint8 _to) private returns(bool){
    //     // require(_logic(_from, _to), 'ChessTable: INVALID_MOVE');

    //     // board[][]
    //     return false;
    // }

    function _move(address _player, uint8 _newMove ,uint8 _meta) private{        

        uint16 newMove = _newMove << 8 + _meta; 
        moves.push(newMove);
        // TODO:: it can be done through flipping the addresses too.
        turn = moves.length % 2 == 0 ? white : black;

        emit PlayerMoved(_player, _newMove, state);
    }

    function getBoard() external view returns(uint8[8][8] memory){
        return board;
    }


    function initialize(address _player1, address _player2, uint8 meta) external returns (bool) {
        require(msg.sender == lobby, 'ChessTable: NOT_AUTHORIZED');
        _initialize(_player1, _player2, meta);
        return true;
    }

    function move(uint8 newMove, uint8 meta) external returns (bool) {
        require(state >= 0x10, 'ChessTable: STATE_MISMATCH');
        // TODO:: the maxed out game's result must get resolved.
        require(moves.length < MAX_MOVES, 'ChessTable: MOVE_OVERFLOW');
        require(msg.sender == turn, 'ChessTable: NOT_YOUR_TURN');
        uint8 selectedPiece = board[newMove & FROM_RANK_MASK][newMove & FROM_FILE_MASK];
        address pieceOwner = (selectedPiece & COLOR_BLACK == 0 ? white : black);
        require( msg.sender == pieceOwner, 'ChessTable: NOT_YOUR_PIECE');

        _move(pieceOwner, newMove, meta);
        return true;
    }


}
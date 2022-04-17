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

    // maybe not needed
    uint8 public constant FILE_MASK = 0xF0;
    uint8 public constant RANK_MASK = 0x0F;

    // FILEs
    uint8 public constant F_A = 0x00 << 3;
    uint8 public constant F_B = 0x01 << 3;
    uint8 public constant F_C = 0x02 << 3;
    uint8 public constant F_D = 0x03 << 3;
    uint8 public constant F_E = 0x04 << 3;
    uint8 public constant F_F = 0x05 << 3;
    uint8 public constant F_G = 0x06 << 3;
    uint8 public constant F_H = 0x07 << 3;

    // RANKs
    uint8 public constant R_1 = 0x00;
    uint8 public constant R_2 = 0x01;
    uint8 public constant R_3 = 0x02;
    uint8 public constant R_4 = 0x03;
    uint8 public constant R_5 = 0x04;
    uint8 public constant R_6 = 0x05;
    uint8 public constant R_7 = 0x06;
    uint8 public constant R_8 = 0x07;

    // MODES
    uint8 public constant M_DEAD = 0x00 << 6;
    uint8 public constant M_SET = 0x01 << 6;
    uint8 public constant M_PINNED = 0x02 << 6;
    uint8 public constant M_IMP = 0x03 << 6;


    uint8 public constant W_K = 0;
    uint8 public constant B_K = 1;

    uint8 public constant W_Q = 2;
    uint8 public constant B_Q = 3;

    uint8 public constant W_R_A = 4;
    uint8 public constant B_R_A = 5;

    uint8 public constant W_R_H = 6;
    uint8 public constant B_R_H = 7;

    uint8 public constant W_B_C = 8;
    uint8 public constant B_B_C = 9;
    uint8 public constant W_B_F = 10;
    uint8 public constant B_B_F = 11;

    uint8 public constant W_N_B = 12;
    uint8 public constant B_N_B = 13;
    uint8 public constant W_N_G = 14;
    uint8 public constant B_N_G = 15;

    uint8 public constant W_P_A = 16;
    uint8 public constant B_P_A = 17;
    uint8 public constant W_P_B = 18;
    uint8 public constant B_P_B = 19;
    uint8 public constant W_P_C = 20;
    uint8 public constant B_P_C = 21;
    uint8 public constant W_P_D = 22;
    uint8 public constant B_P_D = 23;
    uint8 public constant W_P_E = 24;
    uint8 public constant B_P_E = 25;
    uint8 public constant W_P_F = 26;
    uint8 public constant B_P_F = 27;
    uint8 public constant W_P_G = 28;
    uint8 public constant B_P_G = 29;
    uint8 public constant W_P_H = 30;
    uint8 public constant B_P_H = 31;    

    string public name;
    address public lobby;
    address public white;
    address public black;
    address public turn;
    
    uint public activeGame;
    uint16 public lastMove;
    uint8 public state;

    uint256 public board;
    
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
    
        // setting the board pieces
        // this is for clean coding
        // this part can be replaced with
        // board = 57206024880500355210511422320168595472987210685811253910150542059381089396576

        // setting white pieces
        board = board | ((uint256)(M_SET | F_A | R_1) << (W_R_A * 8));
        board = board | ((uint256)(M_SET | F_B | R_1) << (W_N_B * 8));
        board = board | ((uint256)(M_SET | F_C | R_1) << (W_B_C * 8));
        board = board | ((uint256)(M_SET | F_D | R_1) << (W_Q * 8));
        board = board | ((uint256)(M_SET | F_E | R_1) << (W_K * 8));
        board = board | ((uint256)(M_SET | F_F | R_1) << (W_B_F * 8));
        board = board | ((uint256)(M_SET | F_G | R_1) << (W_N_G * 8));
        board = board | ((uint256)(M_SET | F_H | R_1) << (W_R_H * 8));

        board = board | ((uint256)(M_SET | F_A | R_2) << (W_P_A * 8));
        board = board | ((uint256)(M_SET | F_B | R_2) << (W_P_B * 8));
        board = board | ((uint256)(M_SET | F_C | R_2) << (W_P_C * 8));
        board = board | ((uint256)(M_SET | F_D | R_2) << (W_P_D * 8));
        board = board | ((uint256)(M_SET | F_E | R_2) << (W_P_E * 8));
        board = board | ((uint256)(M_SET | F_F | R_2) << (W_P_F * 8));
        board = board | ((uint256)(M_SET | F_G | R_2) << (W_P_G * 8));
        board = board | ((uint256)(M_SET | F_H | R_2) << (W_P_H * 8));

        // setting black pieces
        board = board | ((uint256)(M_SET | F_A | R_8) << (B_R_A * 8));
        board = board | ((uint256)(M_SET | F_B | R_8) << (B_N_B * 8));
        board = board | ((uint256)(M_SET | F_C | R_8) << (B_B_C * 8));
        board = board | ((uint256)(M_SET | F_D | R_8) << (B_Q * 8));
        board = board | ((uint256)(M_SET | F_E | R_8) << (B_K * 8));
        board = board | ((uint256)(M_SET | F_F | R_8) << (B_B_F * 8));
        board = board | ((uint256)(M_SET | F_G | R_8) << (B_N_G * 8));
        board = board | ((uint256)(M_SET | F_H | R_8) << (B_R_H * 8));

        board = board | ((uint256)(M_SET | F_A | R_7) << (B_P_A * 8));
        board = board | ((uint256)(M_SET | F_B | R_7) << (B_P_B * 8));
        board = board | ((uint256)(M_SET | F_C | R_7) << (B_P_C * 8));
        board = board | ((uint256)(M_SET | F_D | R_7) << (B_P_D * 8));
        board = board | ((uint256)(M_SET | F_E | R_7) << (B_P_E * 8));
        board = board | ((uint256)(M_SET | F_F | R_7) << (B_P_F * 8));
        board = board | ((uint256)(M_SET | F_G | R_7) << (B_P_G * 8));
        board = board | ((uint256)(M_SET | F_H | R_7) << (B_P_H * 8));
    }


    // called once by the lobby at time of deployment
    function _initialize(address _player1, address _player2, uint8 meta) private {
        white = _player1;
        black = _player2;
        turn = white;
        state = 0x10;
        emit GameStarted(white, black, meta);

    }

    function _logic(uint8 _piece, uint8 _action) private {
        // 

        // board[][]
    }

    function _move(address _player, uint8 _piece, uint8 _action) private{   


        _logic(_piece, _action);
        lastMove = _piece << 8 | _action; 
        moves.push(lastMove);

        // TODO:: it can be done through flipping the addresses too.
        turn = moves.length % 2 == 0 ? white : black;

        emit PlayerMoved(_player, lastMove, state);
    }

    function initialize(address _player1, address _player2, uint8 meta) external returns (bool) {
        require(msg.sender == lobby, 'ChessTable: NOT_AUTHORIZED');
        _initialize(_player1, _player2, meta);
        return true;
    }

    function move(uint8 piece, uint8 action) external returns (bool) {
        require(state >= 0x10, 'ChessTable: STATE_MISMATCH');
        
        // TODO:: the maxed out game's result must get resolved.
        require(moves.length < MAX_MOVES, 'ChessTable: MOVE_OVERFLOW');
        
        // checking the turn condition
        require(msg.sender == turn, 'ChessTable: NOT_YOUR_TURN');

        // player should not be able to move other player's pieces
        address pieceOwner = (piece % 2 == 0 ? white : black);
        require( msg.sender == pieceOwner, 'ChessTable: NOT_YOUR_PIECE');

        _move(pieceOwner, piece, action);
        return true;
    }
}
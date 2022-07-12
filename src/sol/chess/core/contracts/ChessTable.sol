// SPDX-License-Identifier: GPL3
pragma solidity ^0.8;

import './libraries/SafeMath.sol';
import '../interfaces/IERC20.sol';
import '../interfaces/IChessTable.sol';

contract ChessTable is IChessTable{
    // TODO:: verify and remove
    using SafeMath  for uint;

    //-----------------------------------------------------------------
    //-----------------------------------------------------------------
    //-----------------------------------------------------------------
    //                          [[CONSTANTS]]
    //-----------------------------------------------------------------

    // The longest tournament chess game (in terms of moves) is 269 moves 
    // (Nikolic-Arsovic, Belgrade 1989). The game ended in a draw after 
    // over 20 hours of play. 10 games have been 200 moves or over in 
    // tournament play. In theory, the longest chess game can go up to 
    // 5,949 moves.
    uint16 public constant MAX_MOVES = 400;
    uint8 public constant PIECE_COUNT = 32;
    uint8 public constant SQUARE_COUNT = 64;    
    //-----------------------------------------------------------------
    // PIECE indices
    // Kings
    uint8 public constant W_K   = 0 ; uint8 public constant B_K   =  1;
    // Queens
    uint8 public constant W_Q   = 2 ; uint8 public constant B_Q   =  3;
    // Rooks
    uint8 public constant W_R_A = 4 ; uint8 public constant B_R_A =  5;
    uint8 public constant W_R_H = 6 ; uint8 public constant B_R_H =  7;
    // Bishops
    uint8 public constant W_B_C = 8 ; uint8 public constant B_B_C =  9;
    uint8 public constant W_B_F = 10; uint8 public constant B_B_F = 11;
    // Knights
    uint8 public constant W_N_B = 12; uint8 public constant B_N_B = 13;
    uint8 public constant W_N_G = 14; uint8 public constant B_N_G = 15;
    // Pawns
    uint8 public constant W_P_A = 16; uint8 public constant B_P_A = 17;
    uint8 public constant W_P_B = 18; uint8 public constant B_P_B = 19;
    uint8 public constant W_P_C = 20; uint8 public constant B_P_C = 21;
    uint8 public constant W_P_D = 22; uint8 public constant B_P_D = 23;
    uint8 public constant W_P_E = 24; uint8 public constant B_P_E = 25;
    uint8 public constant W_P_F = 26; uint8 public constant B_P_F = 27;
    uint8 public constant W_P_G = 28; uint8 public constant B_P_G = 29;
    uint8 public constant W_P_H = 30; uint8 public constant B_P_H = 31;   
    //-----------------------------------------------------------------
    // Piece data encoding
    //              FILEs
    uint8 public constant F_A = 0x00 << 3;
    uint8 public constant F_B = 0x01 << 3;
    uint8 public constant F_C = 0x02 << 3;
    uint8 public constant F_D = 0x03 << 3;
    uint8 public constant F_E = 0x04 << 3;
    uint8 public constant F_F = 0x05 << 3;
    uint8 public constant F_G = 0x06 << 3;
    uint8 public constant F_H = 0x07 << 3;

    //              RANKs
    uint8 public constant R_1 = 0x00;
    uint8 public constant R_2 = 0x01;
    uint8 public constant R_3 = 0x02;
    uint8 public constant R_4 = 0x03;
    uint8 public constant R_5 = 0x04;
    uint8 public constant R_6 = 0x05;
    uint8 public constant R_7 = 0x06;
    uint8 public constant R_8 = 0x07;

    //              MODES
    uint8 public constant M_DEAD   = 0x00 << 6;
    uint8 public constant M_SET    = 0x01 << 6;
    uint8 public constant M_PINNED = 0x02 << 6;
    uint8 public constant M_IMP    = 0x03 << 6;
    //-----------------------------------------------------------------
    // Piece data masks
    uint8 public constant PC_FILE_MASK = 0x38;
    uint8 public constant PC_RANK_MASK = 0x07;
    uint8 public constant PC_COORD_MASK = 0x3F;
    uint8 public constant PC_MODE_MASK = 0xC0;
    //-----------------------------------------------------------------
    // State bit indices
    uint8 public constant S_TURN = 0x01;
    uint8 public constant S_STARTED = 0x02;
    uint8 public constant S_WHITE_CHECK = 0x04;
    uint8 public constant S_BLACK_CHECK = 0x08;
    uint8 public constant S_WHITE_CHECKMATE = 0x10;
    uint8 public constant S_BLACK_CHECKMATE = 0x20;
    uint8 public constant S_DRAW = 0x40;
    //-----------------------------------------------------------------
    // MASKS64 for visibility updates
    // NE:4, NW:5, SE:6, SW:7
    // N:0, S:1, E:2, W:3
    uint8 public constant D_N = 0;
    uint8 public constant D_S = 1;
    uint8 public constant D_E = 2;
    uint8 public constant D_W = 3;
    uint8 public constant D_NE = 4;
    uint8 public constant D_NW = 5;
    uint8 public constant D_SE = 6;
    uint8 public constant D_SW = 7;
    uint8 public constant D_ST = 8; // star patterns for king

    uint64 public constant U64_1 = 0x01;
    //-----------------------------------------------------------------
    //-----------------------------------------------------------------
    //-----------------------------------------------------------------
    //                          [[VIEW]]
    //-----------------------------------------------------------------
    string public name;
    address public lobby;
    address public white;
    address public black;
    address public turn;
    
    uint public activeGame;
    uint16 public lastMove;
    uint8 public state;

    uint256 public pieces;

    // piece to squares
    uint64[32] public visibility;

    // piece to pieces
    uint32[32] public engagements;

    // showing whether a square is filled or not
    uint64 public board64W;
    uint64 public board64B;


    uint private unlocked = 1;
    uint16[] private moves;

    mapping(uint8 => mapping (uint8 => uint64)) public M64;

    //-----------------------------------------------------------------
    //-----------------------------------------------------------------
    //-----------------------------------------------------------------
    //                          [[MODIFIER]]
    //-----------------------------------------------------------------
    modifier lock() {
        require(unlocked == 1, 'ChessTable: LOCKED');
        unlocked = 0;
        _;
        unlocked = 1;
    }
    //-----------------------------------------------------------------
    //-----------------------------------------------------------------
    //-----------------------------------------------------------------
    //                          [[CONSTRUCTOR]]
    //-----------------------------------------------------------------
    constructor(){
        lobby = msg.sender;
        name = "gary";
    
        _precomputations();
        _setBoard();
    }
    //-----------------------------------------------------------------
    //-----------------------------------------------------------------
    //-----------------------------------------------------------------
    //                     [[MATH FUNCTION]]
    //-----------------------------------------------------------------

    //-----------------------------------------------------------------
    function _msb64(uint64 x) private returns (uint8){
        uint8[32] memory bval = [ 0,1,2,2,3,3,3,3,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5];
        uint8 base = 0;
        if (x & 0xFFFFFFFF00000000 != 0){
            base = base + 32; // (64/2)
            x = x >> 32; // (64/2)
        }
        if (x & 0x00000000FFFF0000 != 0){
            base = base + 16; // (64/4)
            x = x >> 16; // (64/4)
        }
        if (x & 0x000000000000FF00 != 0){
            base = base + 8; // (64/8)
            x = x >> 8; // (64/8)
        }
        if (x & 0x00000000000000F0 != 0){
            base = base + 4; // (64/16)
            x = x >> 4; // (64/16)
        }
        return (base + bval[x] - 1); // -1 to convert to index
    }
    //-----------------------------------------------------------------
    function _lsb64(uint64 x) private returns (uint8){
        /*Returns the index, counting from 0, of the
        least significant set bit in `x`.
        */
        // return _msb64(x & -x);
        // TODO:: new!! test it.
        return _msb64(x & (~(x-1)));
    }
    //-----------------------------------------------------------------
    //                     [[PRIVATE FUNCTION]]
    //-----------------------------------------------------------------
    //-----------------------------------------------------------------
    function _mask_direction(uint8 _sq, uint8 _direction, uint64 _block64) private returns (uint64){
        uint8 lsb = _lsb64(_block64);
        uint8 msb = _msb64(_block64);

        if(_sq >= msb){
            // directions: NorthWest, West, SouthWest, South    
            return M64[_direction][msb];  
        }else{
            // directions: SouthEast, East, NorthEast, North
            return M64[_direction][lsb];
        }
    }
    //-----------------------------------------------------------------
    //                     [[VISIBILITY FUNCTIONS]]
    //-----------------------------------------------------------------
    function _pawn_white(uint8 _sq) private returns (uint64){
        uint8 r = (_sq % 8);
        uint8 f = ((_sq - r) / 8);
        uint64 mask = 0x00;
 
        require(r!=0, 'ChessTable: FATAL. PAWN_WHITE');

        if(r == 1){
            mask |= (uint64)(0x03 << (((f) * 8) + (r + 1)));
        }  
        else if(r < 7){
            mask |= (uint64)(0x01 << (((f) * 8) + (r + 1)));
        }
        else{
            // TODO:: implement pawn improvement
            require(1==0, 'ChessTable: IMPROVEMENT_ERROR');
        }

        if(f == 0){
            mask |= (uint64)(0x01 << (((f + 1) * 8) + (r + 1)));
        }
        else if (f == 7){
            mask |= (uint64)(0x01 << (((f - 1) * 8) + (r + 1)));
        }
        else{
            mask |= (uint64)(0x01 << (((f + 1) * 8) + (r + 1)));
            mask |= (uint64)(0x01 << (((f - 1) * 8) + (r + 1)));
        }

        return mask;
    }
    //-----------------------------------------------------------------
    function _pawn_black(uint8 _sq) private returns (uint64){
        uint8 r = (_sq % 8);
        uint8 f = ((_sq - r) / 8);
        uint64 mask = 0x00;
        require(r != 7, 'ChessTable: FATAL. PAWN_WHITE');

        if(r == 6){
            mask |= (uint64)(0x03 << ((f * 8) + (r - 2)));
        }  
        else if(r != 0){
            mask |= (uint64)(0x01 << ((f * 8) + (r - 1)));
        }
        else{
            // TODO:: implement pawn improvement
            require(1==0, 'ChessTable: IMPROVEMENT_ERROR');
        }

        if(f == 0){
            mask |= (uint64)(0x01 << (((f + 1) * 8) + (r - 1)));
        }
        else if (f == 7){
            mask |= (uint64)(0x01 << (((f - 1) * 8) + (r - 1)));
        }
        else{
            mask |= (uint64)(0x01 << (((f + 1) * 8) + (r - 1)));
            mask |= (uint64)(0x01 << (((f - 1) * 8) + (r - 1)));
        }

        return mask;
    }
    //-----------------------------------------------------------------
    function _knight(uint8 _sq) private returns (uint64){
        uint8 r = (_sq % 8);
        uint8 f = ((_sq - r) / 8);
        uint64 mask = 0x00;

        if((r < 7) && (f > 6)){
            mask |= (uint64)(1 << ((r + 1) + (8 * (f - 2))));
        }

        if((r > 0) && (f < 6)){
            mask |= (uint64)(1 << ((r - 1) + (8 * (f + 2))));
        }

        if((r < 7)  && (f < 6)){
            mask |= (uint64)(1 << ((r + 1) + (8 * (f + 2))));
        }

        if((r > 0) && (f > 1)){
            mask |= (uint64)(1 << ((r - 1) + (8 * (f - 2))));
        }

        if((r > 1) && (f > 0)){
            mask |= (uint64)(1 << ((r - 2) + (8 * (f - 1))));
        }

        if((r < 6) && (f > 0)){
            mask |= (uint64)(1 << ((r + 2) + (8 * (f - 1))));
        }

        if((r > 1) && (f < 7)){
            mask |= (uint64)(1 << ((r - 2) + (8 * (f + 1))));
        }

        if((r < 6) && (f < 7)){
            mask |= (uint64)(1 << ((r + 2) + (8 * (f + 1))));
        }

        return mask;
    }
    //-----------------------------------------------------------------
    function _bishop(uint64 board64, uint8 _sq) private returns (uint64){
        uint64 ne = M64[D_NE][_sq];
        uint64 ne_obs = board64 & ne;
        if(ne_obs != 0x00){
            ne &= (~ _mask_direction(_sq, D_NE, ne_obs));
        }

        uint64 nw = M64[D_NW][_sq];
        uint64 nw_obs = board64 & nw;
        if(nw_obs != 0x00){
            nw &= (~ _mask_direction(_sq, D_NW, nw_obs));
        }

        uint64 se = M64[D_SE][_sq];
        uint64 se_obs = board64 & se;
        if(se_obs != 0x00){
            se &= (~ _mask_direction(_sq, D_SE, se_obs));
        }

        uint64 sw = M64[D_SW][_sq];
        uint64 sw_obs = board64 & sw;
        if(sw_obs != 0x00){
            sw &= (~ _mask_direction(_sq, D_SW, sw_obs));
        }

        return ne | nw | se | sw;
    }
    //-----------------------------------------------------------------
    function _rook(uint64 board64, uint8 _sq) private returns (uint64){
        uint64 north = M64[D_N][_sq];
        uint64 north_obs = board64 & north;
        if(north_obs != 0x00){
            north &= (~ _mask_direction(_sq, D_N, north_obs));
        }

        uint64 south = M64[D_S][_sq];
        uint64 south_obs = board64 & south;
        if(south_obs != 0x00){
            south &= (~ _mask_direction(_sq, D_S, south_obs));
        }

        uint64 east = M64[D_E][_sq];
        uint64 east_obs = board64 & east;
        if(east_obs != 0x00){
            east &= (~ _mask_direction(_sq, D_E, east_obs));
        }

        uint64 west = M64[D_W][_sq];
        uint64 west_obs = board64 & west;
        if(west_obs != 0x00){
            west &= (~ _mask_direction(_sq, D_W, west_obs));
        }

        return north | south | east | west;
    }
    //-----------------------------------------------------------------
    function _queen(uint64 board64, uint8 _sq) private returns (uint64){
        return _bishop(board64, _sq) | _rook(board64, _sq);
    }
    //-----------------------------------------------------------------
    function _king(uint8 _sq) private returns (uint64){
        uint8 r = (_sq % 8);
        uint8 f = ((_sq - r) / 8);

        if(M64[D_ST][_sq] != 0){
            return M64[D_ST][_sq];
        }
        else{
            if(r == 0){
                return (uint64)(M64[D_ST][F_B | R_1] << (8 * (f - 1)));
            }
            else if(r == 7){
                return (uint64)(M64[D_ST][F_B | R_8] << (8 * (f - 1)));
            }
            else if(f == 0){
                return (uint64)(M64[D_ST][F_A | R_2] << (r - 1));
            }
            else if(f == 7){
                return (uint64)(M64[D_ST][F_H | R_2] << (r - 1));
            }
            else{
                return (uint64)(M64[D_ST][F_B | R_2] << ((r - 1) + (8 * (f - 1))));
            }
        }
    }
    //
    //-----------------------------------------------------------------
    function _reloadVisibility(uint64 _block64, uint8 _piece, uint8 _sq) private returns (uint64){
        require(_piece < PIECE_COUNT, "ChessTable, PIECE_OUT_OF_RANGE");
        require(_sq < SQUARE_COUNT, "ChessTable, SQUARE_OUT_OF_RANGE");

        if(_piece >= W_P_A){
            if(_piece % 2 == 0){
                return _pawn_white(_sq);
            }
            else{
                return _pawn_black(_sq);
            }
        }
        else if(_piece >= W_N_B){
            return _knight(_sq);
        }
        else if(_piece >= W_B_C){
            return _bishop(_block64, _sq);
        }
        else if(_piece >= W_R_A){
            return _rook(_block64, _sq);
        }
        else if(_piece >= W_Q){
            return _queen(_block64, _sq);
        }
        else{
            return _king(_sq);
        }
    }
    //-----------------------------------------------------------------
    function _updatePiece(uint8 _piece, uint8 _state) private{
        uint256 piece_mask = (0xFF << (_piece * 8));
        uint256 piece_state = ((uint256)(_state)) << (_piece * 8);
        pieces &= (~piece_mask); // clean previous piece state
        pieces |= piece_state; // shoving the modified piece byte in
    }
    //-----------------------------------------------------------------
    function _setEngagement(uint8 _f_piece, uint8 _t_piece, uint8 _value) private{
        if(_value == 0){
            engagements[_f_piece] &= (uint32)(~(1<< _t_piece));
        }
        else{
            engagements[_f_piece] |= (uint32)(1<< _t_piece);
        }
    }
    //-----------------------------------------------------------------
    function _clearEngagements(uint8 _piece) private{
        engagements[_piece] = 0xFFFFFFFF;
    }
    //-----------------------------------------------------------------
    function getVisibility(uint8 piece) external view returns(uint64){
        return visibility[piece];
    }
    //-----------------------------------------------------------------
    function _move(address _player, uint8 _piece, uint8 _action) private{
        uint64 pieceB64 = _piece % 2 == 0 ? board64W : board64B;
        uint8 to_sq = _action & PC_COORD_MASK;

        // is the square visible to the moved piece?
        // require(((visibility[_piece] & (~pieceB64)) >> to_sq) % 2 == 1, "ChessTable: ILLEGAL_MOVE");

        uint8 from_sq = (uint8)(pieces >> (_piece * 8)) & PC_COORD_MASK;

        // Updating board64
        if(_piece % 2 == 0){
            board64W &= (uint64)(~(1 << from_sq));
            board64W |= (uint64)(1 << to_sq);
        }
        else{
            board64B &= (uint64)(~(1 << from_sq));
            board64B |= (uint64)(1 << to_sq);
        }

        // updating pieces
        _updatePiece(_piece, M_SET | to_sq);

        // Reloading the visibility of the moved piece
        visibility[_piece] = _reloadVisibility(board64W | board64B,_piece, to_sq);

        // Making squares beyond from_sq visible to engaged pieces
        uint32 pc_engagements = engagements[_piece];
        
        // TODO:: It can be replaced with O(log(n)) algorithm
        for(uint8 i=0;i<PIECE_COUNT;i++){
            if(pc_engagements % 2 == 1){
                uint8 pc_sq = ((uint8)(pieces >> (i * 8)) & PC_COORD_MASK);
                visibility[i] = _reloadVisibility(board64W | board64B, i, pc_sq);               
            }
            pc_engagements = pc_engagements >> 1;
            
            if(pc_engagements == 0){
                break;
            }
        }

        // Reset engagements of the moved piece
        _clearEngagements(_piece);

        uint64 opp_vis = 0x00;
        uint64 self_vis = 0x00;
        uint8 self_king = 0;
        uint8 opp_king = 0;

        // Keeping kings position in mind
        if(_piece % 2 == 0){
            self_king = (uint8)(pieces) & PC_COORD_MASK;
            opp_king = (uint8)(pieces >> 8) & PC_COORD_MASK;
        }
        else{
            opp_king = (uint8)(pieces) & PC_COORD_MASK;
            self_king = (uint8)(pieces >> 8) & PC_COORD_MASK;
        }

        // Loop over all pieces
        for(uint8 i_piece = 0; i_piece < PIECE_COUNT; i_piece++){
            // opponent total visibility calculation
            if((_piece % 2 == 0 && i_piece % 2 == 1) || (_piece % 2 == 1 && i_piece % 2 == 0)){
                opp_vis |= visibility[i_piece];
            }
            else{
                self_vis |= visibility[i_piece];
            }

            // for all pieces except the moved piece
            if(i_piece != _piece){
                // i_piece square calculation
                uint8 i_sq = (uint8)((pieces >> (i_piece * 8)) % 256) & PC_COORD_MASK;

                // Update dead piece state
                if(i_sq == to_sq){
                    _updatePiece(i_piece, M_DEAD);
                    // i_sq = to_sq;
                }
                else{
                    uint8 ipc_mode = (uint8)((pieces >> (i_piece * 8)) % 256) & PC_MODE_MASK;

                    // Adding post-move _piece to i_piece engagements
                    if(((visibility[i_piece]) >> to_sq) % 2 == 1 && ipc_mode != M_DEAD){
                        // update engagement
                        _setEngagement(_piece, i_piece, 1);

                        // Making squares beyond to_sq invisible to i_piece
                        visibility[i_piece] = _reloadVisibility(board64W | board64B, i_piece, i_sq);

                        // removing the broken engagements
                        for(uint8 j_piece = 0;j_piece< PIECE_COUNT; j_piece++){
                            if((engagements[j_piece] >> i_piece) % 2 == 1){
                                uint8 j_sq = (uint8)((pieces >> (j_piece * 8))) & PC_COORD_MASK;
                                if((visibility[i_piece] >> j_sq) % 2 == 0){
                                    _setEngagement(j_piece, i_piece, 0);
                                }
                            }
                        }
                    }
                    // Adding post-move _piece to i_piece engagements
                    if(((visibility[_piece]) >> i_sq) % 2 == 1 && ipc_mode != 0){
                        _setEngagement(i_piece, _piece, 1);
                    }
                }
            }

        }

        // calculating checks
        if(_piece % 2 == 0){
            if((self_vis >> opp_king) % 2 == 1){
                state |= S_BLACK_CHECK;
            }
            else{
                state &= (~S_BLACK_CHECK);
            }
        }
        else{    
            if((self_vis >> opp_king) % 2 == 1){
                state |= S_WHITE_CHECK;
            }
            else{
                state &= (~S_WHITE_CHECK);
            }
        }

        // player's king must be safe post-move
        require( (opp_vis >> self_king) % 2 == 0, "ChessTABLE: KING_IS_CHECK");

        if(state & S_TURN == 0){
            state |= S_TURN;
        }
        else{
            state &= (~S_TURN);
        }


        lastMove = _piece << 8 | _action; 
        moves.push(lastMove);

        // Changing the turn
        // TODO:: it can be done through flipping the addresses too.
        turn = moves.length % 2 == 0 ? white : black;

        emit PlayerMoved(_player, _piece, _action);

        // Checking white's checkmate
        if((_piece % 2 == 1) && (state & S_WHITE_CHECK != 0) && (visibility[0] & (~opp_vis) & (~board64W)) == 0){

            // black won
            state |= S_WHITE_CHECKMATE;
            emit GameEnded(false, black, lobby); // TODO:: third param must be changed
        }

        // Checking black's checkmate
        if(_piece % 2 == 0 && (state & S_BLACK_CHECK != 0) && (visibility[1] & (~opp_vis) & (~board64B)) == 0){
            // white won
            state |= S_BLACK_CHECKMATE;
            emit GameEnded(false, white, lobby); // TODO:: third param must be changed
        }

    }

    //-----------------------------------------------------------------
    // called once by the lobby at time of deployment
    // function _initialize(address _player1, address _player2, uint8 meta) private {

    // }

    //-----------------------------------------------------------------
    //-----------------------------------------------------------------
    //-----------------------------------------------------------------
    //                      [[PUBLIC FUNCTION]]
    //-----------------------------------------------------------------

    function initialize(address player1, address player2, uint8 meta) external returns (bool) {
        require(msg.sender == lobby, 'ChessTable: NOT_AUTHORIZED');
        white = player1;
        black = player2;
        turn = white;
        state = S_STARTED;
        emit GameStarted(white, black, meta);
        return true;
    }

    function move(uint8 piece, uint8 action) external returns (bool) {
        require(state & S_STARTED != 0, 'ChessTable: STATE_MISMATCH');
        require(state & S_WHITE_CHECKMATE == 0, 'ChessTable: WHITE_CHECKMATE');
        require(state & S_BLACK_CHECKMATE == 0, 'ChessTable: BLACK_CHECKMATE');
        
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

    function _setBoard() private{
        // this part can be replaced with
        // pieces = 57206024880500355210511422320168595472987210685811253910150542059381089396576;

        // setting white pieces
        pieces |= ((uint256)(M_SET | F_A | R_1) << (W_R_A * 8));
        pieces |= ((uint256)(M_SET | F_B | R_1) << (W_N_B * 8));
        pieces |= ((uint256)(M_SET | F_C | R_1) << (W_B_C * 8));
        pieces |= ((uint256)(M_SET | F_D | R_1) << (W_Q   * 8));
        pieces |= ((uint256)(M_SET | F_E | R_1) << (W_K   * 8));
        pieces |= ((uint256)(M_SET | F_F | R_1) << (W_B_F * 8));
        pieces |= ((uint256)(M_SET | F_G | R_1) << (W_N_G * 8));
        pieces |= ((uint256)(M_SET | F_H | R_1) << (W_R_H * 8));

        pieces |= ((uint256)(M_SET | F_A | R_2) << (W_P_A * 8));
        pieces |= ((uint256)(M_SET | F_B | R_2) << (W_P_B * 8));
        pieces |= ((uint256)(M_SET | F_C | R_2) << (W_P_C * 8));
        pieces |= ((uint256)(M_SET | F_D | R_2) << (W_P_D * 8));
        pieces |= ((uint256)(M_SET | F_E | R_2) << (W_P_E * 8));
        pieces |= ((uint256)(M_SET | F_F | R_2) << (W_P_F * 8));
        pieces |= ((uint256)(M_SET | F_G | R_2) << (W_P_G * 8));
        pieces |= ((uint256)(M_SET | F_H | R_2) << (W_P_H * 8));

        // setting black pieces
        pieces |= ((uint256)(M_SET | F_A | R_8) << (B_R_A * 8));
        pieces |= ((uint256)(M_SET | F_B | R_8) << (B_N_B * 8));
        pieces |= ((uint256)(M_SET | F_C | R_8) << (B_B_C * 8));
        pieces |= ((uint256)(M_SET | F_D | R_8) << (B_Q   * 8));
        pieces |= ((uint256)(M_SET | F_E | R_8) << (B_K   * 8));
        pieces |= ((uint256)(M_SET | F_F | R_8) << (B_B_F * 8));
        pieces |= ((uint256)(M_SET | F_G | R_8) << (B_N_G * 8));
        pieces |= ((uint256)(M_SET | F_H | R_8) << (B_R_H * 8));

        pieces |= ((uint256)(M_SET | F_A | R_7) << (B_P_A * 8));
        pieces |= ((uint256)(M_SET | F_B | R_7) << (B_P_B * 8));
        pieces |= ((uint256)(M_SET | F_C | R_7) << (B_P_C * 8));
        pieces |= ((uint256)(M_SET | F_D | R_7) << (B_P_D * 8));
        pieces |= ((uint256)(M_SET | F_E | R_7) << (B_P_E * 8));
        pieces |= ((uint256)(M_SET | F_F | R_7) << (B_P_F * 8));
        pieces |= ((uint256)(M_SET | F_G | R_7) << (B_P_G * 8));
        pieces |= ((uint256)(M_SET | F_H | R_7) << (B_P_H * 8));

        // setting up the board through two variables
        // board64W 64bit, each bit shows whether a white piece fills a square or not
        // same for black

        // board64W =
        board64W |= (uint64)(1 << (F_A | R_1)); board64W |= (uint64)(1 << (F_A | R_2));
        board64W |= (uint64)(1 << (F_B | R_1)); board64W |= (uint64)(1 << (F_B | R_2));
        board64W |= (uint64)(1 << (F_C | R_1)); board64W |= (uint64)(1 << (F_C | R_2));
        board64W |= (uint64)(1 << (F_D | R_1)); board64W |= (uint64)(1 << (F_D | R_2));
        board64W |= (uint64)(1 << (F_E | R_1)); board64W |= (uint64)(1 << (F_E | R_2));
        board64W |= (uint64)(1 << (F_F | R_1)); board64W |= (uint64)(1 << (F_F | R_2));
        board64W |= (uint64)(1 << (F_G | R_1)); board64W |= (uint64)(1 << (F_G | R_2));
        board64W |= (uint64)(1 << (F_H | R_1)); board64W |= (uint64)(1 << (F_H | R_2));

        // board64B =
        board64B |= (uint64)(1 << (F_A | R_7)); board64B |= (uint64)(1 << (F_A | R_8));
        board64B |= (uint64)(1 << (F_B | R_7)); board64B |= (uint64)(1 << (F_B | R_8));
        board64B |= (uint64)(1 << (F_C | R_7)); board64B |= (uint64)(1 << (F_C | R_8));
        board64B |= (uint64)(1 << (F_D | R_7)); board64B |= (uint64)(1 << (F_D | R_8));
        board64B |= (uint64)(1 << (F_E | R_7)); board64B |= (uint64)(1 << (F_E | R_8));
        board64B |= (uint64)(1 << (F_F | R_7)); board64B |= (uint64)(1 << (F_F | R_8));
        board64B |= (uint64)(1 << (F_G | R_7)); board64B |= (uint64)(1 << (F_G | R_8));
        board64B |= (uint64)(1 << (F_H | R_7)); board64B |= (uint64)(1 << (F_H | R_8));

        engagements[W_K]   = 0x0004; engagements[B_K ]  = 0x0008;
        // Queens
        engagements[W_Q]   = 0x0001; engagements[B_Q ]  = 0x0002;
        // Rooks
        // engagements[W_R_A] = 0x00 ; engagements[B_R_A] =  0x00;
        // engagements[W_R_H] = 0x00 ; engagements[B_R_H] =  0x00;
        // Bishops
        engagements[W_B_C] = 0x0004; engagements[B_B_C] = 0x0008;
        engagements[W_B_F] = 0x0001; engagements[B_B_F] = 0x0002;
        // Knights
        engagements[W_N_B] = 0x0010; engagements[B_N_B] = 0x0020;
        engagements[W_N_G] = 0x0040; engagements[B_N_G] = 0x0080;
        // Pawns
        engagements[W_P_A] = 0x0010; engagements[B_P_A] = 0x0020;
        engagements[W_P_B] = 0x0100; engagements[B_P_B] = 0x0200;
        engagements[W_P_C] = 0x0004; engagements[B_P_C] = 0x0008;
        engagements[W_P_D] = 0x1105; engagements[B_P_D] = 0x220A;
        engagements[W_P_E] = 0x4405; engagements[B_P_E] = 0x880A;
        engagements[W_P_F] = 0x0001; engagements[B_P_F] = 0x0002;
        engagements[W_P_G] = 0x0400; engagements[B_P_G] = 0x0800;
        engagements[W_P_H] = 0x0040; engagements[B_P_H] = 0x0080;

        visibility[W_K] = 0x30203000000;
        visibility[B_K] = 0xc040c0000000;
        visibility[W_Q] = 0x302030000;
        visibility[B_Q] = 0xc040c00000;
        visibility[W_R_A] = 0x102;
        visibility[B_R_A] = 0x8040;
        visibility[W_R_H] = 0x201000000000000;
        visibility[B_R_H] = 0x4080000000000000;
        visibility[W_B_C] = 0x2000200;
        visibility[B_B_C] = 0x40004000;
        visibility[W_B_F] = 0x2000200000000;
        visibility[B_B_F] = 0x40004000000000;
        visibility[W_N_B] = 0x2040004;
        visibility[B_N_B] = 0x40200020;
        visibility[W_N_G] = 0x400040200000000;
        visibility[B_N_G] = 0x2000204000000000;
        visibility[W_P_A] = 0x40c;
        visibility[B_P_A] = 0x2030;
        visibility[W_P_B] = 0x40c04;
        visibility[B_P_B] = 0x203020;
        visibility[W_P_C] = 0x40c0400;
        visibility[B_P_C] = 0x20302000;
        visibility[W_P_D] = 0x40c040000;
        visibility[B_P_D] = 0x2030200000;
        visibility[W_P_E] = 0x40c04000000;
        visibility[B_P_E] = 0x203020000000;
        visibility[W_P_F] = 0x40c0400000000;
        visibility[B_P_F] = 0x20302000000000;
        visibility[W_P_G] = 0x40c040000000000;
        visibility[B_P_G] = 0x2030200000000000;
        visibility[W_P_H] = 0xc04000000000000;
        visibility[B_P_H] = 0x3020000000000000;
    }

    function _precomputations() private{
        M64[D_E][F_A | R_8] = 0x8080808080808000;
        M64[D_S][F_A | R_8] = 0x7f;
        M64[D_SE][F_A | R_8] = 0x102040810204000;
        M64[D_W][F_B | R_8] = 0x80;
        M64[D_E][F_B | R_8] = 0x8080808080800000;
        M64[D_S][F_B | R_8] = 0x7f00;
        M64[D_SE][F_B | R_8] = 0x204081020400000;
        M64[D_SW][F_B | R_8] = 0x40;
        M64[D_W][F_C | R_8] = 0x8080;
        M64[D_E][F_C | R_8] = 0x8080808080000000;
        M64[D_S][F_C | R_8] = 0x7f0000;
        M64[D_SE][F_C | R_8] = 0x408102040000000;
        M64[D_SW][F_C | R_8] = 0x4020;
        M64[D_W][F_D | R_8] = 0x808080;
        M64[D_E][F_D | R_8] = 0x8080808000000000;
        M64[D_S][F_D | R_8] = 0x7f000000;
        M64[D_SE][F_D | R_8] = 0x810204000000000;
        M64[D_SW][F_D | R_8] = 0x402010;
        M64[D_W][F_E | R_8] = 0x80808080;
        M64[D_E][F_E | R_8] = 0x8080800000000000;
        M64[D_S][F_E | R_8] = 0x7f00000000;
        M64[D_SE][F_E | R_8] = 0x1020400000000000;
        M64[D_SW][F_E | R_8] = 0x40201008;
        M64[D_W][F_F | R_8] = 0x8080808080;
        M64[D_E][F_F | R_8] = 0x8080000000000000;
        M64[D_S][F_F | R_8] = 0x7f0000000000;
        M64[D_SE][F_F | R_8] = 0x2040000000000000;
        M64[D_SW][F_F | R_8] = 0x4020100804;
        M64[D_W][F_G | R_8] = 0x808080808080;
        M64[D_E][F_G | R_8] = 0x8000000000000000;
        M64[D_S][F_G | R_8] = 0x7f000000000000;
        M64[D_SE][F_G | R_8] = 0x4000000000000000;
        M64[D_SW][F_G | R_8] = 0x402010080402;
        M64[D_W][F_H | R_8] = 0x80808080808080;
        M64[D_S][F_H | R_8] = 0x7f00000000000000;
        M64[D_SW][F_H | R_8] = 0x40201008040201;
        M64[D_E][F_A | R_7] = 0x4040404040404000;
        M64[D_S][F_A | R_7] = 0x3f;
        M64[D_N][F_A | R_7] = 0x80;
        M64[D_SE][F_A | R_7] = 0x1020408102000;
        M64[D_NE][F_A | R_7] = 0x8000;
        M64[D_W][F_B | R_7] = 0x40;
        M64[D_E][F_B | R_7] = 0x4040404040400000;
        M64[D_S][F_B | R_7] = 0x3f00;
        M64[D_N][F_B | R_7] = 0x8000;
        M64[D_NW][F_B | R_7] = 0x80;
        M64[D_SE][F_B | R_7] = 0x102040810200000;
        M64[D_SW][F_B | R_7] = 0x20;
        M64[D_NE][F_B | R_7] = 0x800000;
        M64[D_W][F_C | R_7] = 0x4040;
        M64[D_E][F_C | R_7] = 0x4040404040000000;
        M64[D_S][F_C | R_7] = 0x3f0000;
        M64[D_N][F_C | R_7] = 0x800000;
        M64[D_NW][F_C | R_7] = 0x8000;
        M64[D_SE][F_C | R_7] = 0x204081020000000;
        M64[D_SW][F_C | R_7] = 0x2010;
        M64[D_NE][F_C | R_7] = 0x80000000;
        M64[D_W][F_D | R_7] = 0x404040;
        M64[D_E][F_D | R_7] = 0x4040404000000000;
        M64[D_S][F_D | R_7] = 0x3f000000;
        M64[D_N][F_D | R_7] = 0x80000000;
        M64[D_NW][F_D | R_7] = 0x800000;
        M64[D_SE][F_D | R_7] = 0x408102000000000;
        M64[D_SW][F_D | R_7] = 0x201008;
        M64[D_NE][F_D | R_7] = 0x8000000000;
        M64[D_W][F_E | R_7] = 0x40404040;
        M64[D_E][F_E | R_7] = 0x4040400000000000;
        M64[D_S][F_E | R_7] = 0x3f00000000;
        M64[D_N][F_E | R_7] = 0x8000000000;
        M64[D_NW][F_E | R_7] = 0x80000000;
        M64[D_SE][F_E | R_7] = 0x810200000000000;
        M64[D_SW][F_E | R_7] = 0x20100804;
        M64[D_NE][F_E | R_7] = 0x800000000000;
        M64[D_W][F_F | R_7] = 0x4040404040;
        M64[D_E][F_F | R_7] = 0x4040000000000000;
        M64[D_S][F_F | R_7] = 0x3f0000000000;
        M64[D_N][F_F | R_7] = 0x800000000000;
        M64[D_NW][F_F | R_7] = 0x8000000000;
        M64[D_SE][F_F | R_7] = 0x1020000000000000;
        M64[D_SW][F_F | R_7] = 0x2010080402;
        M64[D_NE][F_F | R_7] = 0x80000000000000;
        M64[D_W][F_G | R_7] = 0x404040404040;
        M64[D_E][F_G | R_7] = 0x4000000000000000;
        M64[D_S][F_G | R_7] = 0x3f000000000000;
        M64[D_N][F_G | R_7] = 0x80000000000000;
        M64[D_NW][F_G | R_7] = 0x800000000000;
        M64[D_SE][F_G | R_7] = 0x2000000000000000;
        M64[D_SW][F_G | R_7] = 0x201008040201;
        M64[D_NE][F_G | R_7] = 0x8000000000000000;
        M64[D_W][F_H | R_7] = 0x40404040404040;
        M64[D_S][F_H | R_7] = 0x3f00000000000000;
        M64[D_N][F_H | R_7] = 0x8000000000000000;
        M64[D_NW][F_H | R_7] = 0x80000000000000;
        M64[D_SW][F_H | R_7] = 0x20100804020100;
        M64[D_E][F_A | R_6] = 0x2020202020202000;
        M64[D_S][F_A | R_6] = 0x1f;
        M64[D_N][F_A | R_6] = 0xc0;
        M64[D_SE][F_A | R_6] = 0x10204081000;
        M64[D_NE][F_A | R_6] = 0x804000;
        M64[D_W][F_B | R_6] = 0x20;
        M64[D_E][F_B | R_6] = 0x2020202020200000;
        M64[D_S][F_B | R_6] = 0x1f00;
        M64[D_N][F_B | R_6] = 0xc000;
        M64[D_NW][F_B | R_6] = 0x40;
        M64[D_SE][F_B | R_6] = 0x1020408100000;
        M64[D_SW][F_B | R_6] = 0x10;
        M64[D_NE][F_B | R_6] = 0x80400000;
        M64[D_W][F_C | R_6] = 0x2020;
        M64[D_E][F_C | R_6] = 0x2020202020000000;
        M64[D_S][F_C | R_6] = 0x1f0000;
        M64[D_N][F_C | R_6] = 0xc00000;
        M64[D_NW][F_C | R_6] = 0x4080;
        M64[D_SE][F_C | R_6] = 0x102040810000000;
        M64[D_SW][F_C | R_6] = 0x1008;
        M64[D_NE][F_C | R_6] = 0x8040000000;
        M64[D_W][F_D | R_6] = 0x202020;
        M64[D_E][F_D | R_6] = 0x2020202000000000;
        M64[D_S][F_D | R_6] = 0x1f000000;
        M64[D_N][F_D | R_6] = 0xc0000000;
        M64[D_NW][F_D | R_6] = 0x408000;
        M64[D_SE][F_D | R_6] = 0x204081000000000;
        M64[D_SW][F_D | R_6] = 0x100804;
        M64[D_NE][F_D | R_6] = 0x804000000000;
        M64[D_W][F_E | R_6] = 0x20202020;
        M64[D_E][F_E | R_6] = 0x2020200000000000;
        M64[D_S][F_E | R_6] = 0x1f00000000;
        M64[D_N][F_E | R_6] = 0xc000000000;
        M64[D_NW][F_E | R_6] = 0x40800000;
        M64[D_SE][F_E | R_6] = 0x408100000000000;
        M64[D_SW][F_E | R_6] = 0x10080402;
        M64[D_NE][F_E | R_6] = 0x80400000000000;
        M64[D_W][F_F | R_6] = 0x2020202020;
        M64[D_E][F_F | R_6] = 0x2020000000000000;
        M64[D_S][F_F | R_6] = 0x1f0000000000;
        M64[D_N][F_F | R_6] = 0xc00000000000;
        M64[D_NW][F_F | R_6] = 0x4080000000;
        M64[D_SE][F_F | R_6] = 0x810000000000000;
        M64[D_SW][F_F | R_6] = 0x1008040201;
        M64[D_NE][F_F | R_6] = 0x8040000000000000;
        M64[D_W][F_G | R_6] = 0x202020202020;
        M64[D_E][F_G | R_6] = 0x2000000000000000;
        M64[D_S][F_G | R_6] = 0x1f000000000000;
        M64[D_N][F_G | R_6] = 0xc0000000000000;
        M64[D_NW][F_G | R_6] = 0x408000000000;
        M64[D_SE][F_G | R_6] = 0x1000000000000000;
        M64[D_SW][F_G | R_6] = 0x100804020100;
        M64[D_NE][F_G | R_6] = 0x4000000000000000;
        M64[D_W][F_H | R_6] = 0x20202020202020;
        M64[D_S][F_H | R_6] = 0x1f00000000000000;
        M64[D_N][F_H | R_6] = 0xc000000000000000;
        M64[D_NW][F_H | R_6] = 0x40800000000000;
        M64[D_SW][F_H | R_6] = 0x10080402010000;
        M64[D_E][F_A | R_5] = 0x1010101010101000;
        M64[D_S][F_A | R_5] = 0xf;
        M64[D_N][F_A | R_5] = 0xe0;
        M64[D_SE][F_A | R_5] = 0x102040800;
        M64[D_NE][F_A | R_5] = 0x80402000;
        M64[D_W][F_B | R_5] = 0x10;
        M64[D_E][F_B | R_5] = 0x1010101010100000;
        M64[D_S][F_B | R_5] = 0xf00;
        M64[D_N][F_B | R_5] = 0xe000;
        M64[D_NW][F_B | R_5] = 0x20;
        M64[D_SE][F_B | R_5] = 0x10204080000;
        M64[D_SW][F_B | R_5] = 0x8;
        M64[D_NE][F_B | R_5] = 0x8040200000;
        M64[D_W][F_C | R_5] = 0x1010;
        M64[D_E][F_C | R_5] = 0x1010101010000000;
        M64[D_S][F_C | R_5] = 0xf0000;
        M64[D_N][F_C | R_5] = 0xe00000;
        M64[D_NW][F_C | R_5] = 0x2040;
        M64[D_SE][F_C | R_5] = 0x1020408000000;
        M64[D_SW][F_C | R_5] = 0x804;
        M64[D_NE][F_C | R_5] = 0x804020000000;
        M64[D_W][F_D | R_5] = 0x101010;
        M64[D_E][F_D | R_5] = 0x1010101000000000;
        M64[D_S][F_D | R_5] = 0xf000000;
        M64[D_N][F_D | R_5] = 0xe0000000;
        M64[D_NW][F_D | R_5] = 0x204080;
        M64[D_SE][F_D | R_5] = 0x102040800000000;
        M64[D_SW][F_D | R_5] = 0x80402;
        M64[D_NE][F_D | R_5] = 0x80402000000000;
        M64[D_W][F_E | R_5] = 0x10101010;
        M64[D_E][F_E | R_5] = 0x1010100000000000;
        M64[D_S][F_E | R_5] = 0xf00000000;
        M64[D_N][F_E | R_5] = 0xe000000000;
        M64[D_NW][F_E | R_5] = 0x20408000;
        M64[D_SE][F_E | R_5] = 0x204080000000000;
        M64[D_SW][F_E | R_5] = 0x8040201;
        M64[D_NE][F_E | R_5] = 0x8040200000000000;
        M64[D_W][F_F | R_5] = 0x1010101010;
        M64[D_E][F_F | R_5] = 0x1010000000000000;
        M64[D_S][F_F | R_5] = 0xf0000000000;
        M64[D_N][F_F | R_5] = 0xe00000000000;
        M64[D_NW][F_F | R_5] = 0x2040800000;
        M64[D_SE][F_F | R_5] = 0x408000000000000;
        M64[D_SW][F_F | R_5] = 0x804020100;
        M64[D_NE][F_F | R_5] = 0x4020000000000000;
        M64[D_W][F_G | R_5] = 0x101010101010;
        M64[D_E][F_G | R_5] = 0x1000000000000000;
        M64[D_S][F_G | R_5] = 0xf000000000000;
        M64[D_N][F_G | R_5] = 0xe0000000000000;
        M64[D_NW][F_G | R_5] = 0x204080000000;
        M64[D_SE][F_G | R_5] = 0x800000000000000;
        M64[D_SW][F_G | R_5] = 0x80402010000;
        M64[D_NE][F_G | R_5] = 0x2000000000000000;
        M64[D_W][F_H | R_5] = 0x10101010101010;
        M64[D_S][F_H | R_5] = 0xf00000000000000;
        M64[D_N][F_H | R_5] = 0xe000000000000000;
        M64[D_NW][F_H | R_5] = 0x20408000000000;
        M64[D_SW][F_H | R_5] = 0x8040201000000;
        M64[D_E][F_A | R_4] = 0x808080808080800;
        M64[D_S][F_A | R_4] = 0x7;
        M64[D_N][F_A | R_4] = 0xf0;
        M64[D_SE][F_A | R_4] = 0x1020400;
        M64[D_NE][F_A | R_4] = 0x8040201000;
        M64[D_W][F_B | R_4] = 0x8;
        M64[D_E][F_B | R_4] = 0x808080808080000;
        M64[D_S][F_B | R_4] = 0x700;
        M64[D_N][F_B | R_4] = 0xf000;
        M64[D_NW][F_B | R_4] = 0x10;
        M64[D_SE][F_B | R_4] = 0x102040000;
        M64[D_SW][F_B | R_4] = 0x4;
        M64[D_NE][F_B | R_4] = 0x804020100000;
        M64[D_W][F_C | R_4] = 0x808;
        M64[D_E][F_C | R_4] = 0x808080808000000;
        M64[D_S][F_C | R_4] = 0x70000;
        M64[D_N][F_C | R_4] = 0xf00000;
        M64[D_NW][F_C | R_4] = 0x1020;
        M64[D_SE][F_C | R_4] = 0x10204000000;
        M64[D_SW][F_C | R_4] = 0x402;
        M64[D_NE][F_C | R_4] = 0x80402010000000;
        M64[D_W][F_D | R_4] = 0x80808;
        M64[D_E][F_D | R_4] = 0x808080800000000;
        M64[D_S][F_D | R_4] = 0x7000000;
        M64[D_N][F_D | R_4] = 0xf0000000;
        M64[D_NW][F_D | R_4] = 0x102040;
        M64[D_SE][F_D | R_4] = 0x1020400000000;
        M64[D_SW][F_D | R_4] = 0x40201;
        M64[D_NE][F_D | R_4] = 0x8040201000000000;
        M64[D_W][F_E | R_4] = 0x8080808;
        M64[D_E][F_E | R_4] = 0x808080000000000;
        M64[D_S][F_E | R_4] = 0x700000000;
        M64[D_N][F_E | R_4] = 0xf000000000;
        M64[D_NW][F_E | R_4] = 0x10204080;
        M64[D_SE][F_E | R_4] = 0x102040000000000;
        M64[D_SW][F_E | R_4] = 0x4020100;
        M64[D_NE][F_E | R_4] = 0x4020100000000000;
        M64[D_W][F_F | R_4] = 0x808080808;
        M64[D_E][F_F | R_4] = 0x808000000000000;
        M64[D_S][F_F | R_4] = 0x70000000000;
        M64[D_N][F_F | R_4] = 0xf00000000000;
        M64[D_NW][F_F | R_4] = 0x1020408000;
        M64[D_SE][F_F | R_4] = 0x204000000000000;
        M64[D_SW][F_F | R_4] = 0x402010000;
        M64[D_NE][F_F | R_4] = 0x2010000000000000;
        M64[D_W][F_G | R_4] = 0x80808080808;
        M64[D_E][F_G | R_4] = 0x800000000000000;
        M64[D_S][F_G | R_4] = 0x7000000000000;
        M64[D_N][F_G | R_4] = 0xf0000000000000;
        M64[D_NW][F_G | R_4] = 0x102040800000;
        M64[D_SE][F_G | R_4] = 0x400000000000000;
        M64[D_SW][F_G | R_4] = 0x40201000000;
        M64[D_NE][F_G | R_4] = 0x1000000000000000;
        M64[D_W][F_H | R_4] = 0x8080808080808;
        M64[D_S][F_H | R_4] = 0x700000000000000;
        M64[D_N][F_H | R_4] = 0xf000000000000000;
        M64[D_NW][F_H | R_4] = 0x10204080000000;
        M64[D_SW][F_H | R_4] = 0x4020100000000;
        M64[D_E][F_A | R_3] = 0x404040404040400;
        M64[D_S][F_A | R_3] = 0x3;
        M64[D_N][F_A | R_3] = 0xf8;
        M64[D_SE][F_A | R_3] = 0x10200;
        M64[D_NE][F_A | R_3] = 0x804020100800;
        M64[D_W][F_B | R_3] = 0x4;
        M64[D_E][F_B | R_3] = 0x404040404040000;
        M64[D_S][F_B | R_3] = 0x300;
        M64[D_N][F_B | R_3] = 0xf800;
        M64[D_NW][F_B | R_3] = 0x8;
        M64[D_SE][F_B | R_3] = 0x1020000;
        M64[D_SW][F_B | R_3] = 0x2;
        M64[D_NE][F_B | R_3] = 0x80402010080000;
        M64[D_W][F_C | R_3] = 0x404;
        M64[D_E][F_C | R_3] = 0x404040404000000;
        M64[D_S][F_C | R_3] = 0x30000;
        M64[D_N][F_C | R_3] = 0xf80000;
        M64[D_NW][F_C | R_3] = 0x810;
        M64[D_SE][F_C | R_3] = 0x102000000;
        M64[D_SW][F_C | R_3] = 0x201;
        M64[D_NE][F_C | R_3] = 0x8040201008000000;
        M64[D_W][F_D | R_3] = 0x40404;
        M64[D_E][F_D | R_3] = 0x404040400000000;
        M64[D_S][F_D | R_3] = 0x3000000;
        M64[D_N][F_D | R_3] = 0xf8000000;
        M64[D_NW][F_D | R_3] = 0x81020;
        M64[D_SE][F_D | R_3] = 0x10200000000;
        M64[D_SW][F_D | R_3] = 0x20100;
        M64[D_NE][F_D | R_3] = 0x4020100800000000;
        M64[D_W][F_E | R_3] = 0x4040404;
        M64[D_E][F_E | R_3] = 0x404040000000000;
        M64[D_S][F_E | R_3] = 0x300000000;
        M64[D_N][F_E | R_3] = 0xf800000000;
        M64[D_NW][F_E | R_3] = 0x8102040;
        M64[D_SE][F_E | R_3] = 0x1020000000000;
        M64[D_SW][F_E | R_3] = 0x2010000;
        M64[D_NE][F_E | R_3] = 0x2010080000000000;
        M64[D_W][F_F | R_3] = 0x404040404;
        M64[D_E][F_F | R_3] = 0x404000000000000;
        M64[D_S][F_F | R_3] = 0x30000000000;
        M64[D_N][F_F | R_3] = 0xf80000000000;
        M64[D_NW][F_F | R_3] = 0x810204080;
        M64[D_SE][F_F | R_3] = 0x102000000000000;
        M64[D_SW][F_F | R_3] = 0x201000000;
        M64[D_NE][F_F | R_3] = 0x1008000000000000;
        M64[D_W][F_G | R_3] = 0x40404040404;
        M64[D_E][F_G | R_3] = 0x400000000000000;
        M64[D_S][F_G | R_3] = 0x3000000000000;
        M64[D_N][F_G | R_3] = 0xf8000000000000;
        M64[D_NW][F_G | R_3] = 0x81020408000;
        M64[D_SE][F_G | R_3] = 0x200000000000000;
        M64[D_SW][F_G | R_3] = 0x20100000000;
        M64[D_NE][F_G | R_3] = 0x800000000000000;
        M64[D_W][F_H | R_3] = 0x4040404040404;
        M64[D_S][F_H | R_3] = 0x300000000000000;
        M64[D_N][F_H | R_3] = 0xf800000000000000;
        M64[D_NW][F_H | R_3] = 0x8102040800000;
        M64[D_SW][F_H | R_3] = 0x2010000000000;
        M64[D_E][F_A | R_2] = 0x202020202020200;
        M64[D_S][F_A | R_2] = 0x1;
        M64[D_N][F_A | R_2] = 0xfc;
        M64[D_SE][F_A | R_2] = 0x100;
        M64[D_NE][F_A | R_2] = 0x80402010080400;
        M64[D_W][F_B | R_2] = 0x2;
        M64[D_E][F_B | R_2] = 0x202020202020000;
        M64[D_S][F_B | R_2] = 0x100;
        M64[D_N][F_B | R_2] = 0xfc00;
        M64[D_NW][F_B | R_2] = 0x4;
        M64[D_SE][F_B | R_2] = 0x10000;
        M64[D_SW][F_B | R_2] = 0x1;
        M64[D_NE][F_B | R_2] = 0x8040201008040000;
        M64[D_W][F_C | R_2] = 0x202;
        M64[D_E][F_C | R_2] = 0x202020202000000;
        M64[D_S][F_C | R_2] = 0x10000;
        M64[D_N][F_C | R_2] = 0xfc0000;
        M64[D_NW][F_C | R_2] = 0x408;
        M64[D_SE][F_C | R_2] = 0x1000000;
        M64[D_SW][F_C | R_2] = 0x100;
        M64[D_NE][F_C | R_2] = 0x4020100804000000;
        M64[D_W][F_D | R_2] = 0x20202;
        M64[D_E][F_D | R_2] = 0x202020200000000;
        M64[D_S][F_D | R_2] = 0x1000000;
        M64[D_N][F_D | R_2] = 0xfc000000;
        M64[D_NW][F_D | R_2] = 0x40810;
        M64[D_SE][F_D | R_2] = 0x100000000;
        M64[D_SW][F_D | R_2] = 0x10000;
        M64[D_NE][F_D | R_2] = 0x2010080400000000;
        M64[D_W][F_E | R_2] = 0x2020202;
        M64[D_E][F_E | R_2] = 0x202020000000000;
        M64[D_S][F_E | R_2] = 0x100000000;
        M64[D_N][F_E | R_2] = 0xfc00000000;
        M64[D_NW][F_E | R_2] = 0x4081020;
        M64[D_SE][F_E | R_2] = 0x10000000000;
        M64[D_SW][F_E | R_2] = 0x1000000;
        M64[D_NE][F_E | R_2] = 0x1008040000000000;
        M64[D_W][F_F | R_2] = 0x202020202;
        M64[D_E][F_F | R_2] = 0x202000000000000;
        M64[D_S][F_F | R_2] = 0x10000000000;
        M64[D_N][F_F | R_2] = 0xfc0000000000;
        M64[D_NW][F_F | R_2] = 0x408102040;
        M64[D_SE][F_F | R_2] = 0x1000000000000;
        M64[D_SW][F_F | R_2] = 0x100000000;
        M64[D_NE][F_F | R_2] = 0x804000000000000;
        M64[D_W][F_G | R_2] = 0x20202020202;
        M64[D_E][F_G | R_2] = 0x200000000000000;
        M64[D_S][F_G | R_2] = 0x1000000000000;
        M64[D_N][F_G | R_2] = 0xfc000000000000;
        M64[D_NW][F_G | R_2] = 0x40810204080;
        M64[D_SE][F_G | R_2] = 0x100000000000000;
        M64[D_SW][F_G | R_2] = 0x10000000000;
        M64[D_NE][F_G | R_2] = 0x400000000000000;
        M64[D_W][F_H | R_2] = 0x2020202020202;
        M64[D_S][F_H | R_2] = 0x100000000000000;
        M64[D_N][F_H | R_2] = 0xfc00000000000000;
        M64[D_NW][F_H | R_2] = 0x4081020408000;
        M64[D_SW][F_H | R_2] = 0x1000000000000;
        M64[D_E][F_A | R_1] = 0x101010101010100;
        M64[D_N][F_A | R_1] = 0xfe;
        M64[D_NE][F_A | R_1] = 0x8040201008040200;
        M64[D_W][F_B | R_1] = 0x1;
        M64[D_E][F_B | R_1] = 0x101010101010000;
        M64[D_N][F_B | R_1] = 0xfe00;
        M64[D_NW][F_B | R_1] = 0x2;
        M64[D_NE][F_B | R_1] = 0x4020100804020000;
        M64[D_W][F_C | R_1] = 0x101;
        M64[D_E][F_C | R_1] = 0x101010101000000;
        M64[D_N][F_C | R_1] = 0xfe0000;
        M64[D_NW][F_C | R_1] = 0x204;
        M64[D_NE][F_C | R_1] = 0x2010080402000000;
        M64[D_W][F_D | R_1] = 0x10101;
        M64[D_E][F_D | R_1] = 0x101010100000000;
        M64[D_N][F_D | R_1] = 0xfe000000;
        M64[D_NW][F_D | R_1] = 0x20408;
        M64[D_NE][F_D | R_1] = 0x1008040200000000;
        M64[D_W][F_E | R_1] = 0x1010101;
        M64[D_E][F_E | R_1] = 0x101010000000000;
        M64[D_N][F_E | R_1] = 0xfe00000000;
        M64[D_NW][F_E | R_1] = 0x2040810;
        M64[D_NE][F_E | R_1] = 0x804020000000000;
        M64[D_W][F_F | R_1] = 0x101010101;
        M64[D_E][F_F | R_1] = 0x101000000000000;
        M64[D_N][F_F | R_1] = 0xfe0000000000;
        M64[D_NW][F_F | R_1] = 0x204081020;
        M64[D_NE][F_F | R_1] = 0x402000000000000;
        M64[D_W][F_G | R_1] = 0x10101010101;
        M64[D_E][F_G | R_1] = 0x100000000000000;
        M64[D_N][F_G | R_1] = 0xfe000000000000;
        M64[D_NW][F_G | R_1] = 0x20408102040;
        M64[D_NE][F_G | R_1] = 0x200000000000000;
        M64[D_W][F_H | R_1] = 0x1010101010101;
        M64[D_N][F_H | R_1] = 0xfe00000000000000;
        M64[D_NW][F_H | R_1] = 0x2040810204080;   

        M64[D_ST][F_A | R_1] = 0x0000000000000302;
        M64[D_ST][F_A | R_2] = 0x0000000000000705;
        M64[D_ST][F_A | R_8] = 0x000000000000c040;
        M64[D_ST][F_B | R_8] = 0x0000000000c040c0;
        M64[D_ST][F_H | R_8] = 0x40c0000000000000;
        M64[D_ST][F_H | R_2] = 0x0507000000000000;
        M64[D_ST][F_H | R_1] = 0x0203000000000000;
        M64[D_ST][F_B | R_1] = 0x0000000000030203;
        M64[D_ST][F_B | R_2] = 0x0000000000070507; 

        // TODO:: calculate M64 hash and check in initialization to avoid random tampering

    }


}




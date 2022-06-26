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
    uint8 public constant M_DEAD = 0x00 << 6;
    uint8 public constant M_SET = 0x01 << 6;
    uint8 public constant M_PINNED = 0x02 << 6;
    uint8 public constant M_IMP = 0x03 << 6;
    //-----------------------------------------------------------------
    // Piece data masks
    uint8 public constant PC_FILE_MASK = 0x38;
    uint8 public constant PC_RANK_MASK = 0x07;
    uint8 public constant PC_COORD_MASK = 0x3F;
    //-----------------------------------------------------------------
    // MASKS64 for visibility updates
    uint8 public constant MASK_MESH = 0;
    uint8 public constant MASK_KING_CASTLE = 1;
    uint8 public constant MASK_ROOK = 2;
    uint8 public constant MASK_BISHOP = 3;
    uint8 public constant MASK_KNIGHT = 4;
    uint8 public constant MASK_PAWN_WHITE = 7;
    uint8 public constant MASK_PAWN_BLACK = 8;
    uint64[9] public MASKS64;
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
    uint64[] public visibility;

    // piece to pieces
    uint32[] public engagements;

    // showing whether a square is filled or not
    uint64 public board64W;
    uint64 public board64B;


    uint private unlocked = 1;
    uint16[] private moves;

    mapping(uint8 => mapping (uint8 => uint64)) public MASKS;



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
    constructor() public {
        lobby = msg.sender;
        name = "gary";
    
        // setting the board pieces

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
        // whiteOnBoard 64bit, each bit shows whether a white piece fills a square or not
        // same for black
        // board = whiteOnBoard + blackOnBoard;

        // whiteOnBoard =
        whiteOnBoard |= (1 << F_A | R_1); whiteOnBoard |= (1 << F_A | R_2);
        whiteOnBoard |= (1 << F_B | R_1); whiteOnBoard |= (1 << F_B | R_2);
        whiteOnBoard |= (1 << F_C | R_1); whiteOnBoard |= (1 << F_C | R_2);
        whiteOnBoard |= (1 << F_D | R_1); whiteOnBoard |= (1 << F_D | R_2);
        whiteOnBoard |= (1 << F_E | R_1); whiteOnBoard |= (1 << F_E | R_2);
        whiteOnBoard |= (1 << F_F | R_1); whiteOnBoard |= (1 << F_F | R_2);
        whiteOnBoard |= (1 << F_G | R_1); whiteOnBoard |= (1 << F_G | R_2);
        whiteOnBoard |= (1 << F_H | R_1); whiteOnBoard |= (1 << F_H | R_2);

        // blackOnBoard =
        blackOnBoard |= (1 << F_A | R_7); blackOnBoard |= (1 << F_A | R_8);
        blackOnBoard |= (1 << F_B | R_7); blackOnBoard |= (1 << F_B | R_8);
        blackOnBoard |= (1 << F_C | R_7); blackOnBoard |= (1 << F_C | R_8);
        blackOnBoard |= (1 << F_D | R_7); blackOnBoard |= (1 << F_D | R_8);
        blackOnBoard |= (1 << F_E | R_7); blackOnBoard |= (1 << F_E | R_8);
        blackOnBoard |= (1 << F_F | R_7); blackOnBoard |= (1 << F_F | R_8);
        blackOnBoard |= (1 << F_G | R_7); blackOnBoard |= (1 << F_G | R_8);
        blackOnBoard |= (1 << F_H | R_7); blackOnBoard |= (1 << F_H | R_8);

        MASKS64[I_FILE] = 0x0000000F;
        MASKS64[I_RANK] = 0x11111111;
        MASKS64[I_DI_P] = 0x00000000;
        MASKS64[I_DI_N] = 0x00000000;

    }
    //-----------------------------------------------------------------
    //-----------------------------------------------------------------
    //-----------------------------------------------------------------
    //                     [[MATH FUNCTION]]
    //-----------------------------------------------------------------

    //-----------------------------------------------------------------
    function _msb64(uint64 x) private{
        uint8[] bval = [ 0,1,2,2,3,3,3,3,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5];
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
    function _lsb64(uint64 x) private{
        /*Returns the index, counting from 0, of the
        least significant set bit in `x`.
        */
        return _msb64(x & -x);
    }
    //-----------------------------------------------------------------
    //                     [[PRIVATE FUNCTION]]
    //-----------------------------------------------------------------
    function _mask_direction(uint8 square, uint8 direction, uint64 block64){
        uint8 lsb = _lsb64(block64);
        uint8 msb = _msb64(block64);
        uint8 sq_id = SQUARE_IDS[square];

        if(sq_id >= msb){
            // directions: NorthWest, West, SouthWest, South    
            return MASKS[direction][SQUARE_ARRAY[msb]]; //^ (1 << msb)    
        }else{
            // directions: SouthEast, East, NorthEast, North
            return MASKS[direction][SQUARE_ARRAY[lsb]]; //^ (1 << lsb)
        }
    }
    //-----------------------------------------------------------------
    // called once by the lobby at time of deployment
    function _initialize(address _player1, address _player2, uint8 meta) private {
        white = _player1;
        black = _player2;
        turn = white;
        state = 0x10;
        emit GameStarted(white, black, meta);
    }
    //-----------------------------------------------------------------
    //                     [[VISIBILITY FUNCTIONS]]
    //-----------------------------------------------------------------
    function _pawn_white(uint8 _sq) private returns (uint64){

        uint8 r = (_sq % 8);
        uint8 f = ((_sq - r) % 8);
        uint64 mask = 0x00;
 
        require(r!=0, 'ChessTable: FATAL. PAWN_WHITE');

        if(r == 1){
            mask = mask | (0x03 << (((f) * 8) + (r + 1)));
        }  
        else if(r < 7){
            mask = mask | (0x01 << (((f) * 8) + (r + 1)));
        }
        else{
            // TODO:: implement pawn improvement
            require(1==0, 'ChessTable: IMP ERROR');
        }

        if(f == 0){
            mask = mask | (0x01 << (((f + 1) * 8) + (r + 1)));
        }
        else if (f == 7){
            mask = mask | (0x01 << (((f - 1) * 8) + (r + 1)));
        }
        else{
            mask = mask | (0x01 << (((f + 1) * 8) + (r + 1)));
            mask = mask | (0x01 << (((f - 1) * 8) + (r + 1)));
        }

        return mask;
    }
    //-----------------------------------------------------------------
    function _pawn_black(uint8 _sq) private returns (uint64){

        uint8 r = (_sq % 8);
        uint8 f = ((_sq - r) % 8);
        uint64 mask = 0x00;
        require(r != 7, 'ChessTable: FATAL. PAWN_WHITE');

        if(r == 6){
            mask = mask | (0x03 << (((f) * 8) + (r + 1)));
        }  
        else if(r != 0){
            mask = mask | (0x01 << (((f) * 8) + (r + 1)));
        }
        else{
            // TODO:: implement pawn improvement
            require(1==0, 'ChessTable: IMP ERROR');
        }

        if(f == 0){
            mask = mask | (0x01 << (((f + 1) * 8) + (r - 1)));
        }
        else if (f == 7){
            mask = mask | (0x01 << (((f - 1) * 8) + (r - 1)));
        }
        else{
            mask = mask | (0x01 << (((f + 1) * 8) + (r - 1)));
            mask = mask | (0x01 << (((f - 1) * 8) + (r - 1)));
        }

        return mask;
    }
    //-----------------------------------------------------------------
    function _knight(uint8 _sq) private returns (uint64){
        uint8 r = (_sq % 8);
        uint8 f = ((_sq - r) % 8);
        uint64 mask = 0x00;

        if((r + 1 == (r + 1) % 8) && (f - 2 == (f - 2) % 8)){
            mask |= 1 << ((r + 1) + (8 * (f - 2)));
        }

        if((r - 1 == (r - 1) % 8) && (f + 2 == (f + 2) % 8)){
            mask |= 1 << ((r - 1) + (8 * (f + 2)));
        }

        if((r + 1 == (r + 1) % 8)  && (f + 2 == (f + 2) % 8)){
            mask |= 1 << ((r + 1) + (8 * (f + 2)));
        }

        if((r - 1 == (r - 1) % 8) && (f - 2 == (f - 2) % 8)){
            mask |= 1 << ((r - 1) + (8 * (f - 2)));
        }

        if((r - 2 == (r - 2) % 8) && (f - 1 == (f - 1) % 8)){
            mask |= 1 << ((r - 2) + (8 * (f - 1)));
        }

        if((r + 2 == (r + 2) % 8) && (f - 1 == (f - 1) % 8)){
            mask |= 1 << ((r + 2) + (8 * (f - 1)));
        }

        if((r - 2 == (r - 2) % 8) && (f + 1 == (f + 1) % 8)){
            mask |= 1 << ((r - 2) + (8 * (f + 1)));
        }

        if((r + 2 == (r + 2) % 8) && (f + 1 == (f + 1) % 8)){
            mask |= 1 << ((r + 2) + (8 * (f + 1)));
        }

        return mask;
    }
    //-----------------------------------------------------------------
    function _bishop(uint64 board64, uint8 _sq) private returns (uint64){
        // NE:4, NW:5, SE:6, SW:7

        uint64 ne = MASKS[4][_sq];
        uint64 ne_obs = board64 & ne;
        if(ne_obs != 0x00){
            ne = ne & (~ mask_direction(_sq, 4, ne_obs));
        }

        uint64 nw = MASKS[5][_sq];
        uint64 nw_obs = board64 & nw;
        if(nw_obs != 0x00){
            nw = nw & (~ mask_direction(_sq, 5, nw_obs));
        }

        uint64 se = MASKS[6][_sq];
        uint64 se_obs = board64 & se;
        if(se_obs != 0x00){
            se = se & (~ mask_direction(_sq, 6, se_obs));
        }

        uint64 sw = MASKS[7][_sq];
        uint64 sw_obs = board64 & sw;
        if(sw_obs != 0x00){
            sw = sw & (~ mask_direction(_sq, 7, sw_obs));
        }

        return ne | nw | se | sw;
    }
    //-----------------------------------------------------------------
    function _rook(uint64 board64, uint8 _sq) private returns (uint64){
        // N:0, S:1, E:2, W:3
        uint64 north = MASKS[0][_sq];
        uint64 north_obs = board64 & north;
        if(north_obs != 0x00){
            north = north & (~ mask_direction(_sq, 0, north_obs));
        }

        uint64 south = MASKS[1][_sq];
        uint64 south_obs = board64 & south;
        if(south_obs != 0x00){
            south = south & (~ mask_direction(_sq, 1, south_obs));
        }

        uint64 east = MASKS[2][_sq];
        uint64 east_obs = board64 & east;
        if(east_obs != 0x00){
            east = east & (~ mask_direction(_sq, 2, east_obs));
        }

        uint64 west = MASKS[3][_sq];
        uint64 west_obs = board64 & west;
        if(west_obs != 0x00){
            west = west & (~ mask_direction(_sq, 3, west_obs));
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
        uint8 f = ((_sq - r) % 8);
        uint64 mask = 0x00;
        // '*A1': 0x0000000000000302,0
        // '*A2': 0x0000000000000705,1
        // '*A8': 0x000000000000c040,2
        // '*B8': 0x0000000000c040c0,3
        // '*H8': 0x40c0000000000000,4
        // '*H2': 0x0507000000000000,5
        // '*H1': 0x0203000000000000,6
        // '*B1': 0x0000000000030203,7
        // '*B2': 0x0000000000070507,8
        if(MASKS[9][f * 8 + r] != 0){
            return MASKS[9][f * 8 + r];
        }
        else{
            if(r == 0){
                return (MASKS[9][7] << (8 * (f - 1)));
            }
            else if(r == 7){
                return (MASKS[9][3] << (8 * (f - 1)));
            }
            else if(f == 0){
                return (MASKS[9][1] << (r - 1));
            }
            else if(f == 7){
                return (MASKS[9][5] << (r - 1));
            }
            else{
                return (MASKS[9][8] << ((r - 1) + (8 * (f - 1))));
            }
        }
    }
    //-----------------------------------------------------------------
    function _reloadVisibility(uint64 _block64, uint8 _piece, uint8 _sq) private{
        // TODO:: make sure _piece is in legal range
        require(_piece < PIECE_COUNT, "ChessTable, PIECE_OUT_OF_RANGE");
        require(_sq < SQUARE_COUNT, "ChessTable, SQUARE_OUT_OF_RANGE");
        uint64 new_vis;

        if(_piece >= PIECE_IDS['W_P_A']){
            if(_piece % 2 == 0){
                new_vis = pawn_white(_sq);
            }
            else{
                new_vis = pawn_black(_sq);
            }
        }
        else if(_piece >= PIECE_IDS['W_N_B']){
            new_vis = _knight(_sq);
        }
        else if _piece >= PIECE_IDS['W_B_C']){
            new_vis = _bishop(board64, _sq);
        }
        else if _piece >= PIECE_IDS['W_R_A']){
            new_vis = _rook(board64, _sq);
        }
        else if _piece >= PIECE_IDS['W_Q']){
            new_vis = _queen(board64, _sq);
        }
        else{
            new_vis = _king(_sq);
        }

        return new_vis
    }
    //-----------------------------------------------------------------
    function _move(address _player, uint8 _piece, uint8 _action) private{
        uint64 pieceB64;
        if(_piece % 2 == 0){
            pieceB64 = board64W;
        }
        else{
            pieceB64 = board64B;
        }

        uint64 to_sq = _action & MASK128_POSITION;

        // is the square visible to the moved piece?
        require(((visibility[_piece] & (~pieceB64)) >> to_sq) % 2 == 1, "ChessTable: ILLEGAL_MOVE");

        uint64 from_sq = (board128 >> (_piece * 8)) & MASK128_POSITION;

        // Updating board64
        if(_piece % 2 == 0){
            board64W = board64W & ~(1 << from_sq);
            board64W = board64W | (1 << to_sq);
        }
        else{
            board64B = board64B & ~(1 << from_sq);
            board64B = board64B | (1 << to_sq);
        }
        board64 = board64W | board64B;

        // updating board128
        uint8 new_state = ((M_SET | to_sq) << (_piece * 8));
        _updatePiece(_piece, new_state);

        // Reloading the visibility of the moved piece
        visibility[_piece] = _reloadVisibility(board64, board128,_piece, to_sq);

        // Making squares beyond from_sq visible to engaged pieces
        start_index = _piece * PIECE_COUNT;
        sub_engagements = engagements >> start_index;
        for i in range(PIECE_COUNT):
            if sub_engagements % 2 == 1:
                pc_sq = (board128 >> (i * 8)) & MASK128_POSITION
                visibility[i] = _reloadVisibility(board64, board128, i, pc_sq)
            sub_engagements = sub_engagements >> 1

        // Reset engagements of the moved piece
        engagements = reset_piece_engagements(engagements, _piece, 0)

        i_piece = 0
        opp_vis = 0x00

        // Keeping kings position in mind
        if _piece % 2 == 0:
            king_sq = board128 & MASK128_POSITION
        else:
            king_sq = (board128 >> 8) & MASK128_POSITION

        // Loop over all pieces
        while(i_piece >= 0 and i_piece <= PIECE_COUNT - 1):
            // opponent total visibility calculation
            if (_piece % 2 == 0 and i_piece % 2 == 1) or (_piece % 2 == 1 and i_piece % 2 == 0) :
                opp_vis = opp_vis | visibility[i_piece]

            // for all pieces except the moved piece
            if i_piece != _piece:
                # i_piece square calculation
                i_sq = (board128 >> (i_piece * 8)) & MASK128_POSITION

                // Update dead piece state
                if i_sq == to_sq:
                    new_state = M_DEAD << (i_piece * 8)
                    board128 = update_piece128(board128, i_piece, new_state)
                else:
                    ipc_mode = (board128 >> (i_piece * 8)) & MASK128_MODE

                    // Adding post-move _piece to i_piece engagements
                    if((visibility[i_piece]) >> to_sq)  % 2 == 1 and ipc_mode != 0:
                        // update engagement
                        engagements = set_engagement(engagements, _piece, i_piece, 1)

                        // Making squares beyond to_sq invisible to i_piece
                        visibility[i_piece] = _reloadVisibility(board64, board128, i_piece, i_sq)

                        // removing the broken engagements
                        sub_engagements = engagements >> i_piece
                        for j_piece in range(32):
                            if sub_engagements % 2 == 1:
                                j_sq = (board128 >> (j_piece * 8)) & MASK128_POSITION
                                if(visibility[i_piece] >> j_sq) % 2 == 0:
                                    engagements = set_engagement(engagements, j_piece, i_piece, 0)
                            sub_engagements = sub_engagements >> 32
                    
                    // Adding post-move _piece to i_piece engagements
                    if ((visibility[_piece]) >> i_sq) % 2 == 1 and ipc_mode != 0:
                        engagements = set_engagement(engagements, i_piece, _piece, 1)

            i_piece = i_piece + 1

        // player's king must be safe post-move
        if (opp_vis >> king_sq) % 2 == 1:
            raise Exception("ChessCore: KING_IS_CHECK")

        // Checking white's checkmate
        if _piece % 2 == 1 and (visibility[0] & (~board64W)) == 0 and (board128 >> 7) % 2 == 1 :
            # black won
            print("BLACK WON!! not implemented")

        // Checking black's checkmate
        if _piece % 2 == 0 and (visibility[1] & (~board64B)) == 0 and (board128 >> 15) % 2 == 1 :
            # white won
            print("WHITE WON!! not implemented")

        // lastMove = _piece << 8 | _action; 
        // moves.push(lastMove);

        // Changing the turn
        // TODO:: it can be done through flipping the addresses too.
        turn = moves.length % 2 == 0 ? white : black;

        emit PlayerMoved(_player, _piece, _action);
    }

    //-----------------------------------------------------------------
    //-----------------------------------------------------------------
    //-----------------------------------------------------------------
    //                      [[PUBLIC FUNCTION]]
    //-----------------------------------------------------------------

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
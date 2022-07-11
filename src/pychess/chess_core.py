from src.pychess.chess_consts import MASK256_FILE, MASK256_RANK, MASK256_POSITION, MASK256_MODE, MASKS
from src.pychess.chess_consts import M_DEAD, M_SET, M_PINNED, M_IMP, PIECE_COUNT, SQUARE_IDS, SQUARE_ARRAY
from src.helpers.chess_helpers import print_board, print_engagements, build_mask, PIECE_CODES, PIECE_IDS, RANKS, FILES, FILE_CODES, RANK_CODES
from src.logger import lprint
##########################################################
def msb64(x):
    """ Returns the index, counting from 0, of the
    most significant set bit in `x` that is 64-bit. """
    bval = [ 0,1,2,2,3,3,3,3,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
    base = 0
    if (x & 0xFFFFFFFF00000000 != 0): 
        base = base + 32 # (64/2)
        x = x >> 32 # (64/2)
    if (x & 0x00000000FFFF0000 != 0):
        base = base + 16 # (64/4)
        x = x >> 16 # (64/4)
    if (x & 0x000000000000FF00 != 0):
        base = base + 8 # (64/8)
        x = x >> 8 # (64/8)
    if (x & 0x00000000000000F0 != 0):
        base = base + 4 # (64/16)
        x = x >> 4 # (64/16)
    return (base + bval[x] - 1) # -1 to convert to index
##########################################################
def lsb64(x):
    """Returns the index, counting from 0, of the
    least significant set bit in `x`. """
    return msb64(x & -x)
##########################################################
def mask_direction(square, direction, block64):
    lsb = lsb64(block64)
    msb = msb64(block64)

    sq_id = SQUARE_IDS[square]

    if sq_id >= msb :
        # directions: NorthWest, West, SouthWest, South    
        return MASKS[direction][SQUARE_ARRAY[msb]]   
    else:
        # directions: SouthEast, East, NorthEast, North
        return MASKS[direction][SQUARE_ARRAY[lsb]]
##########################################################
def pawn_white(_sq):
    r = (_sq % 8)
    f = (_sq // 8)
    mask = 0x00

    if r == 0:
        raise Exception("White pawn on RANK#1")
    elif r == 1:  
        mask = mask | (0x03 << (((f) * 8) + (r + 1)))
    elif r < 7:
        mask = mask | (0x01 << (((f) * 8) + (r + 1)))
    else:
        print("White Pawn IMP not implemeted")    

    if f == 0 :
        mask = mask | (0x01 << (((f + 1) * 8) + (r + 1)))
    elif f == 7:
        mask = mask | (0x01 << (((f - 1) * 8) + (r + 1)))
    else:
        mask = mask | (0x01 << (((f + 1) * 8) + (r + 1)))
        mask = mask | (0x01 << (((f - 1) * 8) + (r + 1)))

    return mask
##########################################################
def pawn_black(_sq):
    f = (_sq // 8)
    r = (_sq % 8)

    mask = 0x00

    if r == 7:
        raise Exception("Black pawn on RANK#8")
    elif r == 6:  
        mask = mask | (0x03 << (((f) * 8) + (r - 2)))
    elif r > 0:
        mask = mask | (0x01 << (((f) * 8) + (r - 1)))
    else:
        print("Black Pawn IMP not implemeted")    

    if f == 0 :
        mask = mask | (0x01 << (((f + 1) * 8) + (r - 1)))
    elif f == 7:
        mask = mask | (0x01 << (((f - 1) * 8) + (r - 1)))
    else:
        mask = mask | (0x01 << (((f + 1) * 8) + (r - 1)))
        mask = mask | (0x01 << (((f - 1) * 8) + (r - 1)))

    return mask
##########################################################
def rook(board64, _sq):
    _sq = SQUARE_ARRAY[_sq]

    north = MASKS["N"][_sq]
    north_obs = board64 & north
    if north_obs != 0x00:
        north = north & (~ mask_direction(_sq, "N", north_obs))

    south = MASKS["S"][_sq]
    # print("    ")
    # print_board(south)
    south_obs = board64 & south
    # print_board(south_obs)
    if south_obs != 0x00:
        south = south & (~ mask_direction(_sq, "S", south_obs))
    # print_board(south)

    east = MASKS["E"][_sq]
    east_obs = board64 & east
    if east_obs != 0x00:
        east = east & (~ mask_direction(_sq, "E", east_obs))

    west = MASKS["W"][_sq]
    west_obs = board64 & west
    if west_obs != 0x00:
        west = west & (~ mask_direction(_sq, "W", west_obs))

    return north | south | east | west
##########################################################
def bishop(board64, _sq):
    _sq = SQUARE_ARRAY[_sq]

    ne = MASKS["NE"][_sq]
    ne_obs = board64 & ne
    if ne_obs != 0x00:
        ne = ne & (~ mask_direction(_sq, "NE", ne_obs))

    nw = MASKS["NW"][_sq]
    nw_obs = board64 & nw
    if nw_obs != 0x00:
        nw = nw & (~ mask_direction(_sq, "NW", nw_obs))

    se = MASKS["SE"][_sq]
    se_obs = board64 & se
    if se_obs != 0x00:
        se = se & (~ mask_direction(_sq, "SE", se_obs))

    sw = MASKS["SW"][_sq]
    sw_obs = board64 & sw
    if sw_obs != 0x00:
        sw = sw & (~ mask_direction(_sq, "SW", sw_obs))

    return ne | nw | se | sw
##########################################################
def queen(board64, _sq):
    return bishop(board64, _sq) | rook(board64, _sq)
##########################################################
def king(_sq):
    f_code = FILE_CODES[(_sq // 8)]
    r_code = RANK_CODES[(_sq % 8)]
    raw_vis = 0x00
    if f"*{f_code}{r_code}" in MASKS.keys():
        raw_vis = MASKS[f"*{f_code}{r_code}"]
    else:
        if RANKS[r_code] == 0:
            raw_vis = (MASKS["*B1"] << (8 * (FILES[f_code] - 1)))
        elif RANKS[r_code] == 7:
            raw_vis = (MASKS["*B8"] << (8 * (FILES[f_code] - 1)))
        elif FILES[f_code] == 0:
            raw_vis = (MASKS["*A2"] << (RANKS[r_code] - 1))
        elif FILES[f_code] == 7:
            raw_vis = (MASKS["*H2"] << (RANKS[r_code] - 1))
        else:
            raw_vis = (MASKS["*B2"] << ((RANKS[r_code] - 1) + (8 * (FILES[f_code] - 1))))
    return raw_vis
##########################################################
def knight(_sq):
    _sq = SQUARE_ARRAY[_sq]

    f_code = _sq[0]
    r_code = _sq[1]
    mask = 0x0000000000000000

    if RANKS[r_code] + 1 == (RANKS[r_code] + 1) % 8  and FILES[f_code] - 2 == (FILES[f_code] - 2) % 8:
        mask = mask | (1 << ((RANKS[r_code] + 1) + (8 * (FILES[f_code] - 2))))

    if RANKS[r_code] - 1 == (RANKS[r_code] - 1) % 8  and FILES[f_code] + 2 == (FILES[f_code] + 2) % 8:
        mask = mask | (1 << ((RANKS[r_code] - 1) + (8 * (FILES[f_code] + 2))))

    if RANKS[r_code] + 1 == (RANKS[r_code] + 1) % 8  and FILES[f_code] + 2 == (FILES[f_code] + 2) % 8:
        mask = mask | (1 << ((RANKS[r_code] + 1) + (8 * (FILES[f_code] + 2))))

    if RANKS[r_code] - 1 == (RANKS[r_code] - 1) % 8  and FILES[f_code] - 2 == (FILES[f_code] - 2) % 8:
        mask = mask | (1 << ((RANKS[r_code] - 1) + (8 * (FILES[f_code] - 2))))

    if RANKS[r_code] - 2 == (RANKS[r_code] - 2) % 8  and FILES[f_code] - 1 == (FILES[f_code] - 1) % 8:
        mask = mask | (1 << ((RANKS[r_code] - 2) + (8 * (FILES[f_code] - 1))))

    if RANKS[r_code] + 2 == (RANKS[r_code] + 2) % 8  and FILES[f_code] - 1 == (FILES[f_code] - 1) % 8:
        mask = mask | (1 << ((RANKS[r_code] + 2) + (8 * (FILES[f_code] - 1))))

    if RANKS[r_code] - 2 == (RANKS[r_code] - 2) % 8  and FILES[f_code] + 1 == (FILES[f_code] + 1) % 8:
        mask = mask | (1 << ((RANKS[r_code] - 2) + (8 * (FILES[f_code] + 1))))

    if RANKS[r_code] + 2 == (RANKS[r_code] + 2) % 8  and FILES[f_code] + 1 == (FILES[f_code] + 1) % 8:
        mask = mask | (1 << ((RANKS[r_code] + 2) + (8 * (FILES[f_code] + 1))))

    return mask
##########################################################
def _reloadVisibility(board64, pieces256, _piece, _sq):
    # TODO:: make sure piece is in legal range
    new_vis = 0x000000000000000

    if _piece >= PIECE_IDS['W_P_A']:
        if _piece % 2 == 0 :
            new_vis = pawn_white(_sq)
        else:
            new_vis = pawn_black(_sq)
    elif _piece >= PIECE_IDS['W_N_B']:
        new_vis = knight(_sq)
    elif _piece >= PIECE_IDS['W_B_C']:
        new_vis = bishop(board64, _sq)
    elif _piece >= PIECE_IDS['W_R_A']:
        new_vis = rook(board64, _sq)
    elif _piece >= PIECE_IDS['W_Q']:
        new_vis = queen(board64, _sq)
    else:
        new_vis = king(_sq)

    return new_vis
##########################################################
def update_piece256(pieces256, _piece, _state):
    piece_mask = (0xFF << (_piece * 8))
    pieces256 = pieces256 & (~piece_mask) # clean previous piece state
    pieces256 = pieces256 | _state # shoving the modified piece byte in
    return pieces256
##########################################################
def set_engagement(engagements, _f_piece, _t_piece, _value):
    if _value == 0:
        engagements[_f_piece] = engagements[_f_piece] & ~(1<<  _t_piece)
    else:
        engagements[_f_piece] = engagements[_f_piece] |  (1<<  _t_piece)
    return engagements
##########################################################
def reset_piece_engagements(engagements, _piece):
    engagements[_piece] = 0    
    return engagements
##########################################################
def move(meta, board64W, board64B, pieces256, engagements, visibility, _piece, _action):

    if _piece % 2 == 0:
        pc_board64 = board64W
    else:
        pc_board64 = board64B

    to_sq = _action & MASK256_POSITION

    # is game finished?
    if meta["is_white_checkmate"] == 1:
        raise Exception("WHITE IS CHECKMATE")

    if meta["is_black_checkmate"] == 1:
        raise Exception("BLACK IS CHECKMATE")

    # is the square visible to the moved piece?
    if ((visibility[_piece] & (~pc_board64)) >> to_sq) % 2 != 1 and visibility[_piece] != 0 : # TODO:: remove second condition [IMPRTANT]
        raise Exception("ILLEGAL_MOVE")

    from_sq = (pieces256 >> (_piece * 8)) & MASK256_POSITION

    # Updating board64
    if _piece % 2 == 0:
        if from_sq != 0 : # TODO:: REMOVE, it is for     ing
            board64W = board64W & ~(1 << from_sq)
        board64W = board64W | (1 << to_sq)

    else:
        if from_sq != 0 : # TODO:: REMOVE, it is for     ing
            board64B = board64B & ~(1 << from_sq)
        board64B = board64B | (1 << to_sq)
    board64 = board64W | board64B

    # updating pieces256
    new_state = ((M_SET | to_sq) << (_piece * 8))
    pieces256 = update_piece256(pieces256, _piece, new_state)

    # Reloading the visibility of the moved piece
    visibility[_piece] = _reloadVisibility(board64, pieces256,_piece, to_sq)

    # Making squares beyond from_sq visible to engaged pieces
    sub_engagements = engagements[_piece]
    for i in range(PIECE_COUNT):
        if sub_engagements % 2 == 1:
            pc_sq = (pieces256 >> (i * 8)) & MASK256_POSITION
            visibility[i] = _reloadVisibility(board64, pieces256, i, pc_sq)
        sub_engagements = sub_engagements >> 1

    # Reset engagements of the moved piece
    engagements = reset_piece_engagements(engagements, _piece)

    i_piece = 0
    opp_vis = 0x00
    self_vis = 0x00
    opp_king = 0x00
    self_king = 0x00

    # Keeping kings positions in mind
    if _piece % 2 == 0:
        self_king = pieces256 & MASK256_POSITION
        opp_king = (pieces256 >> 8) & MASK256_POSITION
    else:
        opp_king = pieces256 & MASK256_POSITION
        self_king = (pieces256 >> 8) & MASK256_POSITION


    # Loop over all pieces
    while(i_piece >= 0 and i_piece <= PIECE_COUNT - 1):

        # total visibility calculation
        if (_piece % 2 == 0 and i_piece % 2 == 1) or (_piece % 2 == 1 and i_piece % 2 == 0) :
            opp_vis = opp_vis | visibility[i_piece]
        else:
            self_vis = self_vis | visibility[i_piece]

        # for all pieces except the moved piece
        if i_piece != _piece:
            # i_piece square calculation
            i_sq = (pieces256 >> (i_piece * 8)) & MASK256_POSITION

            # Update dead piece state
            if i_sq == to_sq:
                new_state = M_DEAD << (i_piece * 8)
                pieces256 = update_piece256(pieces256, i_piece, new_state)
            else:
                ipc_mode = (pieces256 >> (i_piece * 8)) & MASK256_MODE

                # Adding post-move _piece to i_piece engagements
                if((visibility[i_piece]) >> to_sq)  % 2 == 1 and ipc_mode != 0:
                    # update engagement
                    engagements = set_engagement(engagements, _piece, i_piece, 1)

                    # Making squares beyond to_sq invisible to i_piece
                    visibility[i_piece] = _reloadVisibility(board64, pieces256, i_piece, i_sq)
                    # print_board(visibility[i_piece])

                    # removing the broken engagements
                    for j_piece in range(32):
                        if (engagements[j_piece] >> i_piece) % 2 == 1:
                            j_sq = (pieces256 >> (j_piece * 8)) & MASK256_POSITION
                            if(visibility[i_piece] >> j_sq) % 2 == 0:
                                engagements = set_engagement(engagements, j_piece, i_piece, 0)
                
                # Adding post-move _piece to i_piece engagements
                if ((visibility[_piece]) >> i_sq) % 2 == 1 and ipc_mode != 0:
                    engagements = set_engagement(engagements, i_piece, _piece, 1)

        i_piece = i_piece + 1

    # calculating checks
    if _piece % 2 == 0:
        if (self_vis >> opp_king) % 2 == 1:
            meta["is_black_check"] = 1
        else:
            meta["is_black_check"] = 0
    else:
        if (self_vis >> opp_king) % 2 == 1:
            meta["is_white_check"] = 1
        else:
            meta["is_white_check"] = 0

    # player's king must be safe post-move
    if (opp_vis >> self_king) % 2 == 1:
        raise Exception("ChessCore: KING_IS_CHECK")


    if meta["turn"] == 0:
        meta["turn"] = 1
    else:
        meta["turn"] = 0

    # Checking white's checkmate
    if _piece % 2 == 1 and meta["is_white_check"] == 1 and (visibility[0] & (~opp_vis) & (~board64W)) == 0:
        # black won
        meta["is_white_checkmate"] = 1
        lprint("ChessCore: BLACK WON!!")

    # Checking black's checkmate
    if _piece % 2 == 0 and meta["is_black_check"] == 1 and (visibility[1] & (~opp_vis) & (~board64B)) == 0:
        # white won
        meta["is_black_checkmate"] = 1
        lprint("ChessCore: WHITE WON!!")

    return meta, board64W, board64B, pieces256, engagements, visibility
##########################################################

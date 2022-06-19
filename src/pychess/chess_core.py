from src.pychess.chess_consts import MASK128_FILE, MASK128_RANK, MASK128_POSITION, MASK128_MODE, MASKS
from src.pychess.chess_consts import M_DEAD, M_SET, M_PINNED, M_IMP, PIECE_COUNT, SQUARE_IDS, SQUARE_DIAGS, SQUARE_ARRAY
from src.pychess.chess_utils import print_board, build_mask, PIECE_CODES, PIECE_IDS, RANKS, FILES, FILE_CODES, RANK_CODES
##########################################################
def ffs(x):
    """Returns the index, counting from 0, of the
    least significant set bit in `x`.
    """
    return (x & -x).bit_length() - 1
##########################################################
def msb64(x):
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
def mask_direction(square, direction, block64):
    lsb = ffs(block64)
    msb = msb64(block64)
    sq_id = SQUARE_IDS[square]
    # print(lsb)
    # print(msb)
    # print(sq_id)

    if sq_id >= msb :
        # directions: NorthWest, West, SouthWest, South    
        return MASKS[direction][SQUARE_ARRAY[msb]] #^ (1 << msb)    
    else:
        # directions: SouthEast, East, NorthEast, North
        return MASKS[direction][SQUARE_ARRAY[lsb]] #^ (1 << lsb)
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
    if f"*{f_code}{r_code}" in MASKS.keys():
        return MASKS[f"*{f_code}{r_code}"]
    else:
        if RANKS[r_code] == 0:
            return (MASKS["*B1"] << (8 * (FILES[f_code] - 1)))
        elif RANKS[r_code] == 7:
            return (MASKS["*B8"] << (8 * (FILES[f_code] - 1)))
        elif FILES[f_code] == 0:
            return (MASKS["*A2"] << (RANKS[r_code] - 1))
        elif FILES[f_code] == 7:
            return (MASKS["*H2"] << (RANKS[r_code] - 1))
        else:
            return (MASKS["*B2"] << ((RANKS[r_code] - 1) + (8 * (FILES[f_code] - 1))))
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
def _reloadVisibility(board64, board128, _piece, _sq):
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
def update_piece128(board128, _piece, _state):
    piece_mask = (0xFF << (_piece * 8))
    board128 = board128 & (~piece_mask) # clean previous piece state
    board128 = board128 | _state # shoving the modified piece byte in
    return board128
##########################################################
def set_engagement(engagements, _f_piece, _t_piece, _value):
    if _value == 0:
        engagements = engagements & ~(1<< (_f_piece * 32 + _t_piece))
    else:
        engagements = engagements |  (1<< (_f_piece * 32 + _t_piece))
    return engagements
##########################################################
def reset_piece_engagements(engagements, _piece, _direction):
    if _direction == 0:
        engagements = engagements & ~( 0xFFFFFFFF << _piece)        
    else:
        # TODO:: wrong
        for i in range(32):
            engagements = engagements & ~( 0x00000001 << (i * 32 + _piece))
    return engagements
##########################################################
def move(board64W, board64B, board128, engagements, visibility, _piece, _action):

    if _piece % 2 == 0:
        pc_board64 = board64W
    else:
        pc_board64 = board64B

    to_sq = _action & MASK128_POSITION

    # is the square visible to the moved piece?
    # require((visibility[_piece] >> to_sq) % 2 == 1, "ChessTable: ILLEGAL_MOVE");
    if ((visibility[_piece] & (~pc_board64)) >> to_sq) % 2 != 1 and visibility[_piece] != 0 : # TODO:: remove second condition [IMPRTANT]
        raise Exception("ILLEGAL_MOVE")

    from_sq = (board128 >> (_piece * 8)) & MASK128_POSITION

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

    # updating board128
    new_state = ((M_SET | to_sq) << (_piece * 8))
    board128 = update_piece128(board128, _piece, new_state)

    # Reloading the visibility of the moved piece
    visibility[_piece] = _reloadVisibility(board64, board128,_piece, to_sq)
    print_board(visibility[_piece])

    # Making squares beyond from_sq visible to engaged pieces
    # for pc in engagements[_piece]:
    #     pc_sq = (board128 >> (pc * 8)) & MASK128_POSITION
    #     visibility[pc] = _reloadVisibility(board64, board128, pc, pc_sq)

    # update engagements
    engagements = reset_piece_engagements(engagements, _piece, 0)
    # engagements[_piece] = 0x00000000000000000000000000000000

    i_piece = 0
    opp_vis = 0x00

    # Keeping kings position in mind
    if _piece % 2 == 0:
        king_sq = board128 & MASK128_POSITION
    else:
        king_sq = (board128 >> 8) & MASK128_POSITION

    # Loop over all pieces
    while(i_piece >= 0 and i_piece <= PIECE_COUNT - 1):

        # opponent total visibility calculation
        if (_piece % 2 == 0 and i_piece % 2 == 1) or (_piece % 2 == 1 and i_piece % 2 == 0) :
            opp_vis = opp_vis | visibility[i_piece]

        # for all pieces except the moved piece
        if i_piece != _piece:
            # i_piece square calculation
            i_sq = (board128 >> (i_piece * 8)) & MASK128_POSITION

            # Update dead piece state
            if i_sq == to_sq:
                new_state = M_DEAD << (i_piece * 8)
                board128 = update_piece128(board128, i_piece, new_state)
            else:
                ipc_mode = (board128 >> (i_piece * 8)) & MASK128_MODE

                # Adding post-move _piece to i_piece engagements
                if((visibility[i_piece]) >> to_sq)  % 2 == 1 and ipc_mode != 0:
                    # update engagement
                    set_engagement(engagements, _piece, i_piece, 1)

                    # Making squares beyond to_sq invisible to i_piece
                    visibility[i_piece] = _reloadVisibility(board64, board128, i_piece, i_sq)
                    print_board(visibility[i_piece])

                    # removing the broken engagements
                    # for j_piece in engagements_1[i_piece]:
                    #     j_sq = (board128 >> (j_piece * 8)) & MASK128_POSITION
                    #     if(visibility[i_piece] >> j_sq) % 2 != 1:
                    #         set_engagement(_piece, i_piece, 0)
                    #         engagements[i_piece].remove(j_piece)
                    #        # engagements_1[j_piece].remove(i_piece)
                
                # Adding post-move _piece to i_piece engagements
                # print(f"mode: {ipc_mode}")
                if ((visibility[_piece]) >> i_sq) % 2 == 1 and ipc_mode != 0:
                    set_engagement(engagements, i_piece, _piece, 1)

        i_piece = i_piece + 1

    # player's king must be safe post-move
    if opp_vis >> king_sq % 2 == 1:
        raise Exception("ChessCore: KING_IS_CHECK")

    # Checking white's checkmate
    if _piece % 2 == 1 and visibility[0] == 0 and (board128 >> 7) % 2 == 1 :
        # black won
        print("BLACK WON!! not implemented")

    # Checking black's checkmate
    if _piece % 2 == 0 and visibility[1] == 0 and (board128 >> 15) % 2 == 1 :
        # white won
        print("WHITE WON!! not implemented")
    return board64W, board64B, board128, engagements, visibility
##########################################################

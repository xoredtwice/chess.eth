
MASK128_FILE = 0x38
MASK128_RANK = 0x07
MASK128_POSITION = 0x3F

from src.pychess.chess_consts import MASK128_FILE, MASK128_RANK, MASK128_POSITION, MASKS
from src.pychess.chess_consts import M_DEAD, M_SET, M_PINNED, M_IMP, PIECE_COUNT, SQUARE_IDS, SQUARE_DIAGS, SQUARE_ARRAY
from src.pychess.chess_utils import print_board, build_mask, PIECE_CODES, PIECE_IDS, RANKS, FILES, FILE_CODES, RANK_CODES
##########################################################
def is_power_of_two(n):
    return (n != 0) and (n & (n-1) == 0)
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
    if (x and 0xFFFFFFFF00000000): 
        base = base + 16 #(64/4)
        x = x >> 32 #(64/2)
    if (x and 0x00000000FFFF0000):
        base = base + 8 #(64/8)
        x = x >> 16 #(64/4)
    if (x and 0x0000000000000FF00):
        base = base + 4 #(64/16)
        x = x >> 8 #64/8
    if (x and 0x000000000000000F0):
        base = base + 2 #(64/32)
        x = x >> 4 #64/16

    return (base + bval[x])
##########################################################
def mask_direction(square, direction, block64):
    # square = SQUARE_ARRAY[square]
    lsb = ffs(block64)
    msb = msb64(block64)
    # print(lsb)
    # print(msb)
    # print_board(MASKS[direction][square])
    # print_board(MASKS[direction][SQUARE_ARRAY[lsb]])
    sq_id = SQUARE_IDS[square]
    # print(sq_id)

    if sq_id > msb :
        # directions: NorthWest, West, SouthWest, South    
        return MASKS[direction][SQUARE_ARRAY[msb]] #^ (1 << msb)    
    else:
        # directions: SouthEast, East, NorthEast, North
        return MASKS[direction][SQUARE_ARRAY[lsb]] #^ (1 << lsb)
##########################################################
def pawn_white(board64, _sq):
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

    return mask & (~board64)
##########################################################
def pawn_black(board64, _sq):
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

    return mask & (~board64)
##########################################################
def rook(board64, _sq):
    _sq = SQUARE_ARRAY[_sq]

    north = MASKS["N"][_sq]
    north_obs = board64 & north
    if north_obs != 0x00:
        north = north & (~ mask_direction(_sq, "N", north_obs))

    south = MASKS["S"][_sq]
    south_obs = board64 & south
    if south_obs != 0x00:
        south = south & (~ mask_direction(_sq, "S", south_obs))

    east = MASKS["E"][_sq]
    east_obs = board64 & east
    if east_obs != 0x00:
        east = east & (~ mask_direction(_sq, "E", east_obs))

    west = MASKS["W"][_sq]
    # print_board(west)
    west_obs = board64 & west
    # print_board(west_obs)
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
def king(board64, sq):
    f_code = FILE_CODES[(sq // 8)]
    r_code = RANK_CODES[(sq % 8)]
    if f"*{f_code}{r_code}" in MASKS.keys():
        return MASKS[f"*{f_code}{r_code}"]
    else:
        if RANKS[r_code] == 0:
            return (MASKS["*B1"] << (8 * (FILES[f_code] - 1))) & (~board64)
        elif RANKS[r_code] == 7:
            return (MASKS["*B8"] << (8 * (FILES[f_code] - 1))) & (~board64)
        elif FILES[f_code] == 0:
            return (MASKS["*A2"] << (RANKS[r_code] - 1)) & (~board64)
        elif FILES[f_code] == 7:
            return (MASKS["*H2"] << (RANKS[r_code] - 1)) & (~board64)
        else:
            return (MASKS["*B2"] << ((RANKS[r_code] - 1) + (8 * (FILES[f_code] - 1)))) & (~board64)
##########################################################
def knight(board64, _sq):
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

    return mask & ~board64
##########################################################
def _reloadVisibility(board64, board128, _piece, _position):

    new_vis = 0x000000000000000    
    if _piece >= PIECE_IDS['W_P_A']:
        if _piece % 2 == 0 :
            new_vis = pawn_white(board64, _position)
        else:
            new_vis = pawn_black(board64, _position)
    elif _piece >= PIECE_IDS['W_N_B']:
        new_vis = knight(board64, _position)
    elif _piece >= PIECE_IDS['W_B_C']:
        new_vis = bishop(board64, _position)
    elif _piece >= PIECE_IDS['W_R_A']:
        new_vis = rook(board64, _position)
    elif _piece >= PIECE_IDS['W_Q']:
        new_vis = queen(board64, _position)
    else:
        new_vis = king(board64, _position)

    return new_vis
##########################################################
def move(board64W, board64B, board128, engagements, visibility, _piece, _action):
    # parsing from and to squares 
    # print(_piece)

    if _piece % 2 == 0:
    	pc_board64 = board64W
    else:
    	pc_board64 = board64B

    from_sq = (board128 >> (_piece * 8)) & MASK128_POSITION
    to_sq = _action & MASK128_POSITION
    # print(from_sq)
    # print(to_sq)
    # is the square visible to the moved piece?
    # require((visibility[_piece] >> to_sq) % 2 == 1, "ChessTable: ILLEGAL_MOVE");
    if ((visibility[_piece] & (~pc_board64)) >> to_sq) % 2 != 1 and visibility[_piece] != 0 : # TODO:: remove second condition [IMPRTANT]
        raise Exception("ILLEGAL_MOVE")

    if _piece % 2 == 0:
        if from_sq != 0 : # TODO:: REMOVE, it is for testing
            board64W = board64W & ~(1 << from_sq)
        board64W = board64W | (1 << to_sq)

    else:
        if from_sq != 0 : # TODO:: REMOVE, it is for testing
            board64B = board64B & ~(1 << from_sq)
        board64B = board64B | (1 << to_sq)
    board64 = board64W | board64B
    # Reloading the visibility of the moved piece
    visibility[_piece] = _reloadVisibility(board64, board128,_piece, to_sq)
    print_board(visibility[_piece])
    # updating board128
    new_state = ((M_SET | to_sq) << (_piece * 8))
    piece_mask = (0xFF << (_piece * 8))
    board128 = board128 & (~piece_mask) # clean previous piece state
    board128 = board128 | new_state # shoving the modified piece byte in

    # Updating board64
    # print(board64)

    # print(board64)

    # TODO:: update DEAD pieces

    # update engagements and visibility
    new_engagement = 0x00

    # Making squares beyond from_sq visible to i_piece
    for pc in engagements[_piece]:
        pc_sq = (board128 >> (pc * 8)) & MASK128_POSITION
        visibility[pc] = _reloadVisibility(board64, board128, pc, pc_sq)

    engagements[_piece] = []
    i_piece = 0
    while(i_piece >= 0 and i_piece <= PIECE_COUNT - 1):

        # Finding post-move engaged pieces
        if((visibility[i_piece]) >> to_sq)  % 2 == 1:
            # update engagement
            engagements[_piece].append(i_piece)

            # Making squares beyond to_sq invisible to i_piece
            i_sq = (board128 >> (i_piece * 8)) & MASK128_POSITION
            print("EE")
            print(i_sq)
            print("PRE")
            print_board(pc_board64)
            visibility[i_piece] = _reloadVisibility(board64, board128, i_piece, i_sq)
            print_board(visibility[i_piece])
        ipc_sq = (board128 >> (i_piece * 8)) & MASK128_POSITION
        print(ipc_sq)
        if ((visibility[_piece]) >> ipc_sq) % 2 == 1:
            engagements[i_piece].append(_piece)
        i_piece = i_piece + 1

    return board64W, board64B, board128, engagements, visibility
##########################################################

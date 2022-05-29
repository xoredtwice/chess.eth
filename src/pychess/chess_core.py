from src.pychess.chess_consts import PC_FILE_MASK, PC_RANK_MASK, PC_COORD_MASK, MASK
from src.pychess.chess_consts import M_DEAD, M_SET, M_PINNED, M_IMP, PIECE_COUNT, SQUARE_IDS, SQUARE_DIAGS, SQUARE_ARRAY
from src.pychess.chess_consts import PIECE_CODES, RANKS, FILES
from src.pychess.chess_utils import print_board, build_mask
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
    	base = base + 32 #(64/2)
    	x = x >> 32 #(64/2)
    if (x and 0x00000000FFFF0000):
    	base = base + 16 #(64/4)
    	x = x >> 16 #(64/4)
    if (x and 0x0000000000000FF00):
    	base = base + 8 #64/8
    	x = x >> 8 #64/8
    if (x and 0x000000000000000F0):
    	base = base + 4 #64/16
    	x = x >> 4 #64/16

    return base + bval[x]
##########################################################
def mask_direction(square, direction, block64):
	lsb = ffs(block64)
	msb = msb64(block64)
	if MASK[direction][square] <= MASK[direction][SQUARE_ARRAY[lsb]] :
		# directions: NorthWest, West, SouthWest, South	
		return MASK[direction][SQUARE_ARRAY[msb]] ^ (1 << msb)	
	else:
		# directions: SouthEast, East, NorthEast, North
		return MASK[direction][SQUARE_ARRAY[lsb]] ^ (1 << lsb)
##########################################################
def mesh_n(sq, n):
	f = FILES[sq[0]]
	r = RANKS[sq[1]]
	if (f-n) % 8 == (f-n) :
		left = MASKS[FILE_CODES[f-n]]
	else:
		left = 0x00
		
	if (f+n) % 8 == (f+n) :
		right = MASKS[FILE_CODES[f+n]]
	else:
		right = 0x00
		
	if (r-n) % 8 == (r-n) :
		down = MASKS[RANK_CODES[r-n]]
	else:
		down = 0x00
		
	if (r+n) % 8 == (r+n) :
		up = MASKS[RANK_CODES[r+n]]
	else:
		up = 0x00
		
	return left | right | up | down
##########################################################
def pawn_white(board64, _sq):
	r = RANKS[_sq[1]]
	f = FILES[_sq[0]]
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
	r = RANKS[_sq[1]]
	f = FILES[_sq[0]]
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
	# if the is no piece detected in vis
	north = 0x00
	south = 0x00
	west = 0x00
	east = 0x00
	sq_id = SQUARE_IDS[_sq]

	north_obs = board64 & MASK["N"][_sq]
	if north_obs == 0x00:
		north = MASK["N"][_sq]
	else:
		north = MASK["N"][_sq] & (~ mask_direction(_sq, "N", north_obs))

	south_obs = board64 & MASK["S"][_sq]
	if south_obs == 0x00:
		south = MASK["S"][_sq]
	else:
		south = MASK["S"][_sq] & (~ mask_direction(_sq, "S", south_obs))

	east_obs = board64 & MASK["E"][_sq]
	if east_obs == 0x00:
		east = MASK["E"][_sq]
	else:
		east = MASK["E"][_sq] & (~ mask_direction(_sq, "E", east_obs))

	west_obs = board64 & MASK["W"][_sq]
	if west_obs == 0x00:
		west = MASK["W"][_sq]
	else:
		west = MASK["W"][_sq] & (~ mask_direction(_sq, "W", west_obs))


	return north | south | east | west
##########################################################
def rook_n(sq, n):
	return rook(sq) & mesh_n(sq, n)
##########################################################
def bishop(board64, _sq):
	sq_id = SQUARE_IDS[_sq]

	# if the is no piece detected in vis
	ne = 0x00
	nw = 0x00
	se = 0x00
	sw = 0x00

	ne_obs = board64 & MASK["NE"][_sq]
	if ne_obs == 0x00:
		ne = MASK["NE"][_sq]
	else:
		ne = MASK["NE"][_sq] & (~ mask_direction(_sq, "NE", ne_obs))

	nw_obs = board64 & MASK["NW"][_sq]
	if nw_obs == 0x00:
		nw = MASK["NW"][_sq]
	else:
		nw = MASK["NW"][_sq] & (~ mask_direction(_sq, "NW", nw_obs))

	se_obs = board64 & MASK["SE"][_sq]
	if se_obs == 0x00:
		se = MASK["SE"][_sq]
	else:
		se = MASK["SE"][_sq] & (~ mask_direction(_sq, "SE", se_obs))

	sw_obs = board64 & MASK["SW"][_sq]
	if sw_obs == 0x00:
		sw = MASK["SW"][_sq]
	else:
		sw = MASK["SW"][_sq] & (~ mask_direction(_sq, "SW", sw_obs))

	return ne | nw | se | sw
##########################################################
def bishop_n(sq, n):
	return bishop(sq) & mesh_n(sq, n)
##########################################################
def queen(board64, _sq):
	return bishop(board64, _sq) | rook(board64, _sq)
##########################################################
def queen_n(sq, n):
	return bishop_n(sq, n) | rook_n(sq, n)
##########################################################
def king(board64, sq):
	f_code = sq[0]
	r_code = sq[1]
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

	# return mesh_n(sq, 2) & (~(queen_n(sq, 2)))
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
	elif _piece >= PIECE_IDS['W_Q_A']:
		new_vis = queen(board64, _position)
	else:
		new_vis = king(board64, _position)

	return new_vis
##########################################################
def move(board64, board128, engagements, visibility, _piece, _action):
	
	# parsing from and to squares 

    from_sq = (board128 >> (piece * 8)) & MASK128_POSITION
    to_sq = _action & MASK128_POSITION

    # is the square visible to the moved piece?
    # require((visibility[_piece] >> to_sq) % 2 == 1, "ChessTable: ILLEGAL_MOVE");
    if (visibility[_piece] >> to_sq) % 2 != 1:
    	raise Exception("ILLEGAL_MOVE")

    # updating the board partially
    new_state = ((uint256)(M_SET | to_sq) << (_piece * 8))
    piece_mask = (0xFF << (_piece * 8))
    board128 = board128 & (~piece_mask) # clean previous piece state
    board128 = board128 | newPieceState # shoving the modified piece byte in

    # TODO:: update DEAD pieces

    # update engagements and visibility
    new_engagement = 0x00
    i_piece = PIECE_COUNT - 1
    while(i_piece >= 0 and i_piece <= PIECE_COUNT - 1):

        # Finding pre-move engaged pieces
        if(i_piece != _piece and (engagements[i_piece] >> _piece) % 2):
            # Making squares beyond from_sq visible to i_piece
            # _updateVisibility(i_piece, from_sq, true)
            visibility[i_piece] = _reloadVisibility(board64, board128,i_piece)
        

        # Finding post-move engaged pieces
        if((visibility[i_piece] >> to_sq) % 2 == 1):
            # update engagement
            new_engagement = new_engagement | 1
            engagements[i_piece] = engagements[i_piece] | (1 << _piece)

            # Making squares beyond to_sq invisible to i_piece
            # _updateVisibility(i_piece, to_sq, false)
            visibility[i_piece] = _reloadVisibility(board64, board128,i_piece)

        new_engagement = new_engagement << 1
        i_piece = i_piece - 1
    # setting engagements of the moved piece
    engagements[_piece] = new_engagement

    # Reloading the visibility of the moved piece
    _reloadVisibility(board64, board128,_piece)
    return board64, board128, engagements, visibility
##########################################################

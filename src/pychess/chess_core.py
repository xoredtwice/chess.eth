from src.pychess.chess_consts import PC_FILE_MASK, PC_RANK_MASK, PC_COORD_MASK, MASK
from src.pychess.chess_consts import M_DEAD, M_SET, M_PINNED, M_IMP, PIECE_COUNT, SQUARE_IDS, SQUARE_DIAGS, SQUARE_ARRAY
from src.pychess.chess_consts import PIECE_CODES
##########################################################
def is_power_of_two(n):
    return (n != 0) and (n & (n-1) == 0)
##########################################################
def find_blockage_in_direction(direction, block_points):
	result = []
	binary = bin(block_points)[:1:-1]
	i = 0
	for x in range(len(binary)):
		if int(binary[x]):
			result.append(i)
		i = i + 1
	blockage = 0x0000000000000000
	for i in result:
		blockage = blockage | MASK[direction][SQUARE_ARRAY[i]]

	return blockage
##########################################################
def build_mask(squares):
	mask = 0x0000000000000000
	for sq in squares:
		if sq in SQUARE_IDS.keys():
			mask = mask | (1 << SQUARE_IDS[sq])
	return mask
##########################################################
def build_state(sq):
	f_code = sq[0]
	r_code = sq[1]
	return (FILES[f_code] << 3) + RANKS[r_code]
##########################################################
def parse_visibility(vis):
	view = 	[[" "," "," "," "," "," "," "," "],
			 [" "," "," "," "," "," "," "," "],
			 [" "," "," "," "," "," "," "," "],
			 [" "," "," "," "," "," "," "," "],
			 [" "," "," "," "," "," "," "," "],
			 [" "," "," "," "," "," "," "," "],
			 [" "," "," "," "," "," "," "," "],
			 [" "," "," "," "," "," "," "," "]]

	i = 0
	while vis != 0 and i < 64:
		sq_state = vis % 2
		vis = vis // 2
		sq_rank = i % 8
		sq_file = i // 8
		if sq_state != 0 :
			view[7-sq_rank][sq_file] = "X"
		i = i + 1
	return view

##########################################################
def print_board(view):
	# combining parse_v9isibility with print_board for easier coding
	if not isinstance(view, list):
		view = parse_visibility(view)
	i = 8
	print("******************")
	for rank in view:
		s = str(i) + "|" 
		for sq in rank:
			s = s + sq + "|"
		print(s)
		i = i - 1
	print("  a b c d e f g h ")
	print("******************")

##########################################################
def parse_board(board):
	pieces = {}
	view = 	[[" "," "," "," "," "," "," "," "],
			 [" "," "," "," "," "," "," "," "],
			 [" "," "," "," "," "," "," "," "],
			 [" "," "," "," "," "," "," "," "],
			 [" "," "," "," "," "," "," "," "],
			 [" "," "," "," "," "," "," "," "],
			 [" "," "," "," "," "," "," "," "],
			 [" "," "," "," "," "," "," "," "]]

	for i in range(len(PIECE_CODES)):
		sq = board % 256
		r = sq % 8
		sq = sq >> 3 
		f = sq % 8
		m = sq >> 3 
		if m != 0 :
			pieces[PIECE_CODES[i]] = FILE_CODES[f] + RANK_CODES[r]
			print(i)
			print(PIECE_CODES[i][:3])
			print(PIECE_UNICODES[PIECE_CODES[i][:3]])
			print(PIECE_UNICODES["B_P"])
			print()
			view[7-r][f] = PIECE_UNICODES[PIECE_CODES[i][:3]]
		else :
			pieces[PIECE_CODES[i]] = "X"
		board = board >> 8;

	return pieces, view
##########################################################
def mesh1(sq):
	f_code = sq[0]
	r_code = sq[1]
	if f"*{f_code}{r_code}" in MASKS.keys():
		return MASKS[f"*{f_code}{r_code}"]
	else:
		if RANKS[r_code] == 0:
			return MASKS["*B1"] << (8 * (FILES[f_code] - 1))
		elif RANKS[r_code] == 7:
			return MASKS["*B8"] << (8 * (FILES[f_code] - 1))
		elif FILES[f_code] == 0:
			return MASKS["*A2"] << (RANKS[r_code] - 1)
		elif FILES[f_code] == 7:
			return MASKS["*H2"] << (RANKS[r_code] - 1)
		else:
			return MASKS["*B2"] << ((RANKS[r_code] - 1) + (8 * (FILES[f_code] - 1)))
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
def pawn_white(sq):
	squares = []
	f_code = sq[0]
	r_code = sq[1]
	print(f"Visibility of WHITE PAWN in File:{f_code}, Rank:{r_code}")
	r = RANKS[r_code]
	f = FILES[f_code]
	
	r1 = r + 1
	r2 = r + 2
	
	f1 = f + 1
	f_1 = f - 1
	
	if r1 % 8 == r1:
		if f_1 % 8 == f_1 :
			squares.append(FILE_CODES[f_1] + RANK_CODES[r1])

		squares.append(FILE_CODES[f] + RANK_CODES[r1])
		
		if f1 % 8 == f1 :
			squares.append(FILE_CODES[f1] + RANK_CODES[r1])

	if r == 1 :
		squares.append(FILE_CODES[f] + RANK_CODES[3])

	return build_mask(squares)
##########################################################
def rook(board64, _sq):
	print(f"ROOK in:{_sq}")
	print("Board state: ")
	print_board(board64)

	# if the is no piece detected in vis
	north = 0x00
	south = 0x00
	west = 0x00
	east = 0x00

	north_obs = board64 & MASK["N"][_sq]
	if north_obs == 0x00:
		north = MASK["N"][_sq]
	else:
		north = MASK["N"][_sq] & (~ find_blockage_in_direction("N", north_obs))

	south_obs = board64 & MASK["S"][_sq]
	if board64 & MASK["S"][_sq] == 0x00:
		south = MASK["S"][_sq]
	else:
		south = MASK["S"][_sq] & (~ find_blockage_in_direction("S", south_obs))

	east_obs = board64 & MASK["E"][_sq]
	if board64 & MASK["E"][_sq] == 0x00:
		east = MASK["E"][_sq]
	else:
		east = MASK["E"][_sq] & (~ find_blockage_in_direction("E", east_obs))

	west_obs = board64 & MASK["W"][_sq]
	if board64 & MASK["W"][_sq] == 0x00:
		west = MASK["W"][_sq]
	else:
		west = MASK["W"][_sq] & (~ find_blockage_in_direction("W", west_obs))


	return north | south | east | west
##########################################################
def rook_n(sq, n):
	return rook(sq) & mesh_n(sq, n)
##########################################################
def bishop(board64, _sq):
	print(f"BISHOP in:{_sq}")
	print("Board state: ")
	print_board(board64)

	# if the is no piece detected in vis
	ne = 0x00
	nw = 0x00
	se = 0x00
	sw = 0x00

	ne_obs = board64 & MASK["NE"][_sq]
	if ne_obs == 0x00:
		ne = MASK["NE"][_sq]
	else:
		ne = MASK["NE"][_sq] & (~ find_blockage_in_direction("NE", ne_obs))

	nw_obs = board64 & MASK["S"][_sq]
	if board64 & MASK["NW"][_sq] == 0x00:
		nw = MASK["NW"][_sq]
	else:
		nw = MASK["NW"][_sq] & (~ find_blockage_in_direction("NW", nw_obs))

	se_obs = board64 & MASK["SE"][_sq]
	if board64 & MASK["SE"][_sq] == 0x00:
		se = MASK["SE"][_sq]
	else:
		se = MASK["SE"][_sq] & (~ find_blockage_in_direction("SE", se_obs))

	sw_obs = board64 & MASK["SW"][_sq]
	if board64 & MASK["SW"][_sq] == 0x00:
		sw = MASK["SW"][_sq]
	else:
		sw = MASK["SW"][_sq] & (~ find_blockage_in_direction("SW", sw_obs))


	return ne | nw | se | sw
##########################################################
def bishop_n(sq, n):
	return bishop(sq) & mesh_n(sq, n)
##########################################################
def queen(board64, _sq):
	return bishop(board64, _sq) ^ rook(board64, _sq)
##########################################################
def queen_n(sq, n):
	return bishop_n(sq, n) | rook_n(sq, n)
##########################################################
def king(sq):
	return bishop_n(sq, 1) | rook_n(sq, 1)
##########################################################
def knight(sq):
	# return mesh_n(sq, 2) & (~(queen_n(sq, 2)))
	f_code = sq[0]
	r_code = sq[1]
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
def _reloadVisibility(board64, board128, _piece, _position):
	
	if _piece >= PIECE_IDS['W_P_A']:
		if _piece % 2 == 0 :
			raw_vis = pawn_white(_position) & (~(board64)) # buggy for RANK2
		else:
			raw_vis = pawn_black(_position) & (~(board64)) # buggy for RANK7
	elif _piece >= PIECE_IDS['W_N_B']:
		raw_vis = knight(_position) & (~(board64))
	elif _piece >= PIECE_IDS['W_B_C']:
		raw_vis = 0x000000000000000
		for i in range(8):
			raw_vis = raw_vis | ( bishop_n(i+1))

	elif _piece >= PIECE_IDS['W_R_A']:
		raw_vis = rook(_position)
	elif _piece >= PIECE_IDS['W_Q_A']:
		raw_vis = queen(_position)
	else:
		raw_vis = king(_position) & (~(board64))

	new_vis = 0x000000000000000


	

	print("Not implemented")
	return new_vis
##########################################################
def move(board64, board128, engagements, visibility, _piece, _action):
	
	# parsing from and to squares 

    from_sq = (board128 >> (piece * 8)) & MASK128_POSITION
    to_sq = _action & PC_COORD_MASK

    # is the square visible to the moved piece?
    # require((visibility[_piece] >> to_sq) % 2 == 1, "ChessTable: ILLEGAL_MOVE");
    if (visibility[_piece] >> to_sq) % 2 != 1:
    	raise Exception("ILLEGAL_MOVE")


    # updating the board partially
    new_state = ((uint256)(M_SET | to_sq) << (_piece * 8))
    piece_mask = (0xFF << (_piece * 8))
    board128 &= (~piece_mask) # clean previous piece state
    board |= newPieceState # shoving the modified piece byte in

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
def set_initial_board():
	visibilities = [0x00] * 32
	engagements = [0x00] * 32
	board64 = 0x00
	board128 = 0x00

	# setting 32 pieces one by one and updating the states and testing
	
	# setting white pawns
	for i in range(8):
		updated_piece = PIECE_IDS[f'W_P_{FILE_CODES[i]}']
		updated_state = build_state(f"{FILE_CODES[i]}2")
		board64, board128, engagements,visibilities = move(board64, board128, engagements,visibilities, updated_piece, updated_state)

	# setting black pawns
	for i in range(8):
		updated_piece = PIECE_IDS[f'B_P_{FILE_CODES[i]}']
		updated_state = build_state(f"{FILE_CODES[i]}7")
		board64, board128, engagements,visibilities = move(board64, board128, engagements,visibilities, updated_piece, updated_state)

##########################################################
# TEST SCRIPTS


#set_initial_board()
# build_8way_masks()

# print_board(bishop("F5"))

# print_board(queen("D7"))

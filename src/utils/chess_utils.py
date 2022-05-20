
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


def is_power_of_two(n):
    return (n != 0) and (n & (n-1) == 0)

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

def rook(board64, _sq):
	print(f"ROOK in:{_sq}")

	# if the is no piece detected in vis
	north = 0x00
	south = 0x00
	west = 0x00
	east = 0x00

	north_obs = board64 & MASK["N"][_sq]
	if north_obs == 0x00:
		north = MASK["N"][_sq]
	else:
		north =


	if board64 & MASK["S"][_sq] == 0x00:
		south = MASK["S"][_sq]
	else:

	if board64 & MASK["E"][_sq] == 0x00:
		east = MASK["E"][_sq]
	else:

	if board64 & MASK["W"][_sq] == 0x00:
		west = MASK["W"][_sq]
	else:


	return north | south | east | west

def rook_n(sq, n):
	return rook(sq) & mesh_n(sq, n)

def bishop(sq):
	print(f"BISHOP in:{sq}")
	return MASK["NE"][sq] | MASK["SW"][sq] | MASK["NW"][sq] | MASK["SE"][sq]

def bishop_n(sq, n):
	return bishop(sq) & mesh_n(sq, n)

def queen(sq):
	return bishop(sq) ^ rook(sq)

def queen_n(sq, n):
	return bishop_n(sq, n) | rook_n(sq, n)

def king(sq):
	return bishop_n(sq, 1) | rook_n(sq, 1)

def knight(sq):
	# return mesh_n(sq, 2) & (~(queen_n(sq, 2)))
	f_code = sq[0]
	r_code = sq[1]
	mask = 0x0000000000000000

	if RANKS[r_code] - 1 == (RANKS[r_code] - 1) % 8  and FILES[f_code] - 2 == (FILES[f_code] - 2) % 8:
		mask = mask | (1 << ((RANKS[r_code] - 1) + (8 * (FILES[f_code] - 2))))

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

def build_8way_masks():
	for sq in SQUARE_IDS.keys():
		f_code = sq[0]
		r_code = sq[1]
		d_codes = SQUARE_DIAGS[sq]
		d1_code = f"+{(d_codes % 16)}"
		d2_code = f"-{(d_codes // 16)}"		
		# print(f"Visibility of File:{f_code}, Rank:{r_code}")
		# print(f"Visibility of  D+:{d1_code}, D-:{d2_code}")

		m = {}
		sqm = build_mask([sq])
		m["W"] = MASKS[r_code] & ((1 << SQUARE_IDS[sq]) - 1 )
		m["E"] = MASKS[r_code] & (~m["W"]) & (~sqm)

		m["S"] = MASKS[f_code] & ((1 << SQUARE_IDS[sq]) - 1 )
		m["N"] = MASKS[f_code] & (~m["S"]) & (~sqm)

		m["NW"] = MASKS[d1_code] & ((1 << SQUARE_IDS[sq]) - 1 )
		m["SE"] = MASKS[d1_code] & (~m["NW"]) & (~sqm)

		m["SW"] = MASKS[d2_code] & ((1 << SQUARE_IDS[sq]) - 1 )
		m["NE"] = MASKS[d2_code] & (~m["SW"]) & (~sqm)
		for direction in m.keys():
			print(f"MASK['{direction}']['{sq}'] = {hex(m[direction])}")
			# print_board(m[direction])


def build_mask(squares):
	mask = 0x0000000000000000
	for sq in squares:
		if sq in SQUARE_IDS.keys():
			mask = mask | (1 << SQUARE_IDS[sq])
	return mask

def build_state(sq):
	f_code = sq[0]
	r_code = sq[1]
	return (FILES[f_code] << 3) + RANKS[r_code]

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

def build_diagonal_masks():
	d1 = build_mask(["A1"])
	# print_board(parse_visibility(d1))
	print(f"'+1' : {hex(d1)},")

	d2 = d1
	di = 2
	for i in range(7):
		d2 = (d2 | (0x80 << (i*8))) << 1
		# print_board(parse_visibility(d2))
		print(f"'+{di}' : {hex(d2)},")
		di = di + 1

	for i in range(7):
		d2 = (d2 & ~(0x80 << (i*8))) << 1
		# print_board(parse_visibility(d2))
		print(f"'+{di}' : {hex(d2)},")
		di = di + 1

	d16 = build_mask(["H1"])
	# print_board(parse_visibility(d16))
	print(f"'-1': {hex(d2)},")

	d2 = d16
	di = 2
	for i in range(7):
		d2 = (d2  << 1) | (0x01 << ((6-i)*8))
		# print_board(parse_visibility(d2))
		print(f"'-{di}': {hex(d2)},")
		di = di + 1

	for i in range(7):
		d2 = (d2 << 1) & ~(0x101010101010101)
		# print_board(parse_visibility(d2))
		print(f"'-{di}': {hex(d2)},")
		di = di + 1

def build_mesh1_masks():
	# A1
	mask = build_mask(["A2", "B2", "B1"])
	# print_board(parse_visibility(mask))
	print(f"'*A1' : {hex(mask)},")

	# A2
	mask = build_mask(["A1", "B1", "B2", "B3", "A3"])
	# print_board(parse_visibility(mask))
	print(f"'*A2' : {hex(mask)},")

	# A8
	mask = build_mask(["A7", "B7", "B8"])
	# print_board(parse_visibility(mask))
	print(f"'*A8' : {hex(mask)},")

	# B8
	mask = build_mask(["A8", "A7", "B7", "C7", "C8"])
	# print_board(parse_visibility(mask))
	print(f"'*B8' : {hex(mask)},")

	# H8
	mask = build_mask(["H7", "G7", "G8"])
	# print_board(parse_visibility(mask))
	print(f"'*H8' : {hex(mask)},")

	# H2
	mask = build_mask(["H1", "G1", "G2", "G3", "H3"])
	# print_board(parse_visibility(mask))
	print(f"'*H2' : {hex(mask)},")

	# H1
	mask = build_mask(["H2", "G2", "G1"])
	# print_board(parse_visibility(mask))
	print(f"'*H1' : {hex(mask)},")

	# B1
	mask = build_mask(["A1", "A2", "B2", "C2", "C1"])
	# print_board(parse_visibility(mask))
	print(f"'*B1' : {hex(mask)},")


	# B2
	mask = build_mask(["A1", "A2", "A3", "B3", "C3", "C2", "C1", "B1"])
	# print_board(parse_visibility(mask))
	print(f"'*B2' : {hex(mask)},")
# build_diagonal_masks()
# build_mesh1_masks()

def king_tests():
	print_board(king("A4"))
	print_board(king("A5"))
	print_board(king("A7"))
	print_board(king("A8"))
	print_board(king("B8"))
	print_board(king("C8"))
	print_board(king("D8"))
	print_board(king("F8"))
	print_board(king("G8"))
	print_board(king("H8"))
	print_board(king("H7"))
	print_board(king("H6"))
	print_board(king("H3"))
	print_board(king("H2"))
	print_board(king("H1"))
	print_board(king("G1"))
	print_board(king("F1"))
	print_board(king("C1"))
	print_board(king("B1"))

	print_board(king("B2"))
	print_board(king("D4"))
	print_board(king("E4"))
	print_board(king("G6"))

def knight_tests():
	print("A4")
	print_board(knight("A4"))
	print("A5")
	print_board(knight("A5"))
	print("A7")
	print_board(knight("A7"))
	print("A8")
	print_board(knight("A8"))
	print("B8")
	print_board(knight("B8"))
	print("C8")
	print_board(knight("C8"))
	print("D8")
	print_board(knight("D8"))
	print("F8")
	print_board(knight("F8"))
	print("G8")
	print_board(knight("G8"))
	print("H8")
	print_board(knight("H8"))
	print("H7")
	print_board(knight("H7"))
	print("H6")
	print_board(knight("H6"))
	print("H3")
	print_board(knight("H3"))
	print("H2")
	print_board(knight("H2"))
	print("H1")
	print_board(knight("H1"))


PC_FILE_MASK = 0x38
PC_RANK_MASK = 0x07
PC_COORD_MASK = 0x3F
M_DEAD = 0x00 << 6
M_SET = 0x01 << 6
M_PINNED = 0x02 << 6
M_IMP = 0x03 << 6
PIECE_COUNT = 32

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



#set_initial_board()
# build_8way_masks()

print_board(bishop("F5"))
print_board(rook("B3"))
print_board(queen("D7"))

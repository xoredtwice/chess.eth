
SQUARE_IDS = {
	'A8':0X07, 'B8':0X0F, 'C8':0X17, 'D8':0X1F, 'E8':0X27, 'F8':0X2F, 'G8':0X37, 'H8':0X3F,
	'A7':0X06, 'B7':0X0E, 'C7':0X16, 'D7':0X1E, 'E7':0X26, 'F7':0X2E, 'G7':0X36, 'H7':0X3E,
	'A6':0X05, 'B6':0X0D, 'C6':0X15, 'D6':0X1D, 'E6':0X25, 'F6':0X2D, 'G6':0X35, 'H6':0X3D,
	'A5':0X04, 'B5':0X0C, 'C5':0X14, 'D5':0X1C, 'E5':0X24, 'F5':0X2C, 'G5':0X34, 'H5':0X3C,
	'A4':0X03, 'B4':0X0B, 'C4':0X13, 'D4':0X1B, 'E4':0X23, 'F4':0X2B, 'G4':0X33, 'H4':0X3B,
	'A3':0X02, 'B3':0X0A, 'C3':0X12, 'D3':0X1A, 'E3':0X22, 'F3':0X2A, 'G3':0X32, 'H3':0X3A,
	'A2':0X01, 'B2':0X09, 'C2':0X11, 'D2':0X19, 'E2':0X21, 'F2':0X29, 'G2':0X31, 'H2':0X39,
	'A1':0X00, 'B1':0X08, 'C1':0X10, 'D1':0X18, 'E1':0X20, 'F1':0X28, 'G1':0X30, 'H1':0X38
}


SQUARE_DIAGS = {
	'A8':0XF8, 'B8':0XE9, 'C8':0XDA, 'D8':0XCB, 'E8':0XBC, 'F8':0XAD, 'G8':0X9E, 'H8':0X8F,
	'A7':0XE7, 'B7':0XD8, 'C7':0XC9, 'D7':0XBA, 'E7':0XAB, 'F7':0X9C, 'G7':0X8D, 'H7':0X7E,
	'A6':0XD6, 'B6':0XC7, 'C6':0XB8, 'D6':0XA9, 'E6':0X9A, 'F6':0X8B, 'G6':0X7C, 'H6':0X6D,
	'A5':0XC5, 'B5':0XB6, 'C5':0XA7, 'D5':0X98, 'E5':0X89, 'F5':0X7A, 'G5':0X6B, 'H5':0X5C,
	'A4':0XB4, 'B4':0XA5, 'C4':0X96, 'D4':0X87, 'E4':0X78, 'F4':0X69, 'G4':0X5A, 'H4':0X4B,
	'A3':0XA3, 'B3':0X94, 'C3':0X85, 'D3':0X76, 'E3':0X67, 'F3':0X58, 'G3':0X49, 'H3':0X3A,
	'A2':0X92, 'B2':0X83, 'C2':0X74, 'D2':0X65, 'E2':0X56, 'F2':0X47, 'G2':0X38, 'H2':0X29,
	'A1':0X81, 'B1':0X72, 'C1':0X63, 'D1':0X54, 'E1':0X45, 'F1':0X36, 'G1':0X27, 'H1':0X18
}

PIECE_CODES =[
	'W_K',
	'B_K',
	'W_Q',
	'B_Q',
	'W_R_A',
	'B_R_A',
	'W_R_H',
	'B_R_H',
	'W_B_C',
	'B_B_C',
	'W_B_F',
	'B_B_F',
	'W_N_B',
	'B_N_B',
	'W_N_G',
	'B_N_G',
	'W_P_A',
	'B_P_A',
	'W_P_B',
	'B_P_B',
	'W_P_C',
	'B_P_C',
	'W_P_D',
	'B_P_D',
	'W_P_E',
	'B_P_E',
	'W_P_F',
	'B_P_F',
	'W_P_G',
	'B_P_G',
	'W_P_H',
	'B_P_H']

PIECE_IDS ={
	'W_K':0,
	'B_K':1,
	'W_Q':2,
	'B_Q':3,
	'W_R_A':4,
	'B_R_A':5,
	'W_R_H':6,
	'B_R_H':7,
	'W_B_C':8,
	'B_B_C':9,
	'W_B_F':10,
	'B_B_F':11,
	'W_N_B':12,
	'B_N_B':13,
	'W_N_G':14,
	'B_N_G':15,
	'W_P_A':16,
	'B_P_A':17,
	'W_P_B':18,
	'B_P_B':19,
	'W_P_C':20,
	'B_P_C':21,
	'W_P_D':22,
	'B_P_D':23,
	'W_P_E':24,
	'B_P_E':25,
	'W_P_F':26,
	'B_P_F':27,
	'W_P_G':28,
	'B_P_G':29,
	'W_P_H':30,
	'B_P_H':31}

PIECE_UNICODES = {
	"B_K": "\u2654",
	"B_Q": "\u2655",
	"B_R": "\u2656",
	"B_B": "\u2657",
	"B_N": "\u2658",
	"B_P": "\u2659",
	"W_K": "\u265A",
	"W_Q": "\u265B",
	"W_R": "\u265C",
	"W_B": "\u265D",
	"W_N": "\u265E",
	"W_P": "\u265F"
}
RANKS = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7}
FILES = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
RANK_CODES = ['1','2','3','4','5','6','7','8']
FILE_CODES = ['A','B','C','D','E','F','G','H']

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


MASKS = {
	"A"  : 0x00000000000000FF,
	"B"  : 0x000000000000FF00,
	"C"  : 0x0000000000FF0000,
	"D"  : 0x00000000FF000000,
	"E"  : 0x000000FF00000000,
	"F"  : 0x0000FF0000000000,
	"G"  : 0x00FF000000000000,
	"H"  : 0xFF00000000000000,
	"1"  : 0x0101010101010101,
	"2"  : 0x0202020202020202,
	"3"  : 0x0404040404040404,
	"4"  : 0x0808080808080808,
	"5"  : 0x1010101010101010,
	"6"  : 0x2020202020202020,
	"7"  : 0x4040404040404040,
	"8"  : 0x8080808080808080,
	'+1' : 0x0000000000000001,
	'+2' : 0x0000000000000102,
	'+3' : 0x0000000000010204,
	'+4' : 0x0000000001020408,
	'+5' : 0x0000000102040810,
	'+6' : 0x0000010204081020,
	'+7' : 0x0001020408102040,
	'+8' : 0x0102040810204080,
	'+9' : 0x0204081020408000,
	'+10': 0x0408102040800000,
	'+11': 0x0810204080000000,
	'+12': 0x1020408000000000,
	'+13': 0x2040800000000000,
	'+14': 0x4080000000000000,
	'+15': 0x8000000000000000,
	'-1' : 0x0100000000000000,
	'-2' : 0x0201000000000000,
	'-3' : 0x0402010000000000,
	'-4' : 0x0804020100000000,
	'-5' : 0x1008040201000000,
	'-6' : 0x2010080402010000,
	'-7' : 0x4020100804020100,
	'-8' : 0x8040201008040201,
	'-9' : 0x0080402010080402,
	'-10': 0x0000804020100804,
	'-11': 0x0000008040201008,
	'-12': 0x0000000080402010,
	'-13': 0x0000000000804020,
	'-14': 0x0000000000008040,
	'-15': 0x0000000000000080,
	'*A1': 0x0000000000000302,
	'*A2': 0x0000000000000705,
	'*A8': 0x000000000000c040,
	'*B8': 0x0000000000c040c0,
	'*H8': 0x40c0000000000000,
	'*H2': 0x0507000000000000,
	'*H1': 0x0203000000000000,
	'*B1': 0x0000000000030203,
	'*B2': 0x0000000000070507,
}



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

def rook(sq):
	f_code = sq[0]
	r_code = sq[1]
	print(f"Visibility of ROOK in File:{f_code}, Rank:{r_code}")

	return MASKS[r_code] ^ MASKS[f_code]

def rook_n(sq, n):
	return rook(sq) & mesh_n(sq, n)

def bishop(sq):
	d_codes = SQUARE_DIAGS[sq]
	d1_code = f"+{(d_codes % 16)}"
	d2_code = f"-{(d_codes // 16)}"
	print(f"Visibility of Bishop in D+:{d1_code}, D-:{d2_code}")

	return MASKS[d1_code] ^ MASKS[d2_code]

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

# def generate_visibility(board64, piece_id, from_sq, to_sq, from_vis):
# 	to_vis = from_vis
# 	if piece_id in PIECE_IDS.keys():
# 		if piece_id[2] == "K":

# 	return to_vis

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

def _reloadVisibility(board64, board128, i_piece):
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
    while(i_piece >= 0 && i_piece <= PIECE_COUNT - 1){

        # Finding pre-move engaged pieces
        if(i_piece != _piece && (engagements[i_piece] >> _piece) % 2){
            # Making squares beyond from_sq visible to i_piece
            # _updateVisibility(i_piece, from_sq, true)
            visibility[i_piece] = _reloadVisibility(board64, board128,i_piece)
        }

        # Finding post-move engaged pieces
        if((visibility[i_piece] >> to_sq) % 2 == 1){
            # update engagement
            new_engagement = new_engagement | 1
            engagements[i_piece] = engagements[i_piece] | (1 << _piece)

            # Making squares beyond to_sq invisible to i_piece
            # _updateVisibility(i_piece, to_sq, false)
            visibility[i_piece] = _reloadVisibility(board64, board128,i_piece)
        }

        new_engagement = new_engagement << 1
        i_piece = i_piece - 1;
    }
    # setting engagements of the moved piece
    engagements[_piece] = new_engagement

    # Reloading the visibility of the moved piece
    _reloadVisibility(board64, board128,_piece);


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


set_initial_board()
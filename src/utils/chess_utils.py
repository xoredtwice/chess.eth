
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

def print_board(view):
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

def shift_visibility(vis, direction):
	shifted = vis
	if direction == "L":
		shifted = shifted 
	elif direction == "R":
		shifted = shifted 
	elif direction == "U":
		shifted = shifted 
	elif direction == "D":
		shifted = shifted

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
	'-1' : 0x8000000000000000,
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
	'-15': 0x0000000000000080
}



# def mesh1(sq):
# 	f_code = sq[0]
# 	r_code = sq[1]
# 	if RANKS[r_code] == 0:
# 		if FILES[f_code] == 0:
			
# 		elif FILES[f_code] == 7:
# 		else:
# 	elif RANKS[r_code] == 7:
# 		if FILES[f_code] == 0:
# 		elif FILES[f_code] == 7:
# 		else:
# 	else:
# 		if FILES[f_code] == 0:
# 		elif FILES[f_code] == 7:
# 		else:

def rook(sq):
	f_code = sq[0]
	r_code = sq[1]
	print(f"Visibility of ROOK in File:{f_code}, Rank:{r_code}")

	return MASKS[r_code] ^ MASKS[f_code]

def bishop(sq):
	d_codes = SQUARE_DIAGS[sq]
	d1_code = f"+{(d_codes % 16)}"
	d2_code = f"-{(d_codes // 16)}"
	print(f"Visibility of Bishop in D+:{d1_code}, D-:{d2_code}")

	return MASKS[d1_code] ^ MASKS[d2_code]

def queen(sq):
	return bishop(sq) ^ rook(sq)

def king(sq):
	return queen(sq) & mesh1(sq)

def build_mask(squares):
	mask = 0x0000000000000000
	for sq in squares:
		if sq in SQUARE_IDS.keys():
			mask = mask | (1 << SQUARE_IDS[sq])
	return mask



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


# build_diagonal_masks()
# Testing rank change
# print_board(parse_visibility(king("E4")))
# print_board(parse_visibility(king("H8")))
# print_board(parse_visibility(pawn_white("H2")))
# print_board(parse_visibility(pawn_white("E3")))
print_board(parse_visibility(queen("A7")))

# print_board(parse_visibility(rook("D2")))



# d1 = build_mask(["H1"])
# print_board(parse_visibility(d1))
# print(hex(d1))

# d1 = build_mask(["A1", ""])
# print_board(parse_visibility(d1))
# print(d1)

# d1 = build_mask(["A1"])
# print_board(parse_visibility(d1))
# print(d1)

# Testing rank change
# print_board(parse_visibility(rook_vis >> 8))
# print_board(parse_visibility(rook_vis << 8))

# print("Rook Visibility")
# print_board(parse_visibility(rook_vis))



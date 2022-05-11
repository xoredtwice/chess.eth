
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

	return squares

def king(sq):
	squares = []
	f_code = sq[0]
	r_code = sq[1]
	print(f"Visibility of KING in File:{f_code}, Rank:{r_code}")
	r = RANKS[r_code]
	f = FILES[f_code]
	
	r1 = r + 1
	r_1 = r - 1
	
	f1 = f + 1
	f_1 = f - 1
	
	if r_1 % 8 == r_1:
		if f_1 % 8 == f_1 :
			squares.append(FILE_CODES[f_1] + RANK_CODES[r_1])
		
		squares.append(FILE_CODES[f] + RANK_CODES[r_1])

		if f1 % 8 == f1 :
			squares.append(FILE_CODES[f1] + RANK_CODES[r_1])

	if f_1 % 8 == f_1 :
		squares.append(FILE_CODES[f_1] + RANK_CODES[r])

	if f1 % 8 == f1 :
		squares.append(FILE_CODES[f1] + RANK_CODES[r])

	if r1 % 8 == r1:
		if f_1 % 8 == f_1 :
			squares.append(FILE_CODES[f_1] + RANK_CODES[r1])
		
		squares.append(FILE_CODES[f] + RANK_CODES[r1])

		if f1 % 8 == f1 :
			squares.append(FILE_CODES[f1] + RANK_CODES[r1])


	return squares


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

rook_vis = 0xFF80808080808080


# Testing rank change
print_board(parse_visibility(build_mask(king("E4"))))
print_board(parse_visibility(build_mask(king("H8"))))
print_board(parse_visibility(build_mask(pawn_white("H2"))))
print_board(parse_visibility(build_mask(pawn_white("E3"))))
print_board(parse_visibility(build_mask(pawn_white("D2"))))
# print_board(parse_visibility(rook_vis << 1))

# Testing rank change
# print_board(parse_visibility(rook_vis >> 8))
# print_board(parse_visibility(rook_vis << 8))

# print("Rook Visibility")
# print_board(parse_visibility(rook_vis))



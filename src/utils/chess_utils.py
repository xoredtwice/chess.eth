
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
MASK = {}
MASK['W'] = {}
MASK["E"] = {}
MASK["N"] = {}
MASK["S"] = {}
MASK["NE"]= {}
MASK["SE"]= {}
MASK["NW"]= {}
MASK["SW"]= {}

MASK['W']['A8'] = 0x0
MASK['E']['A8'] = 0x8080808080808000
MASK['S']['A8'] = 0x7f
MASK['N']['A8'] = 0x0
MASK['NW']['A8'] = 0x0
MASK['SE']['A8'] = 0x102040810204000
MASK['SW']['A8'] = 0x0
MASK['NE']['A8'] = 0x0
MASK['W']['B8'] = 0x80
MASK['E']['B8'] = 0x8080808080800000
MASK['S']['B8'] = 0x7f00
MASK['N']['B8'] = 0x0
MASK['NW']['B8'] = 0x0
MASK['SE']['B8'] = 0x204081020400000
MASK['SW']['B8'] = 0x40
MASK['NE']['B8'] = 0x0
MASK['W']['C8'] = 0x8080
MASK['E']['C8'] = 0x8080808080000000
MASK['S']['C8'] = 0x7f0000
MASK['N']['C8'] = 0x0
MASK['NW']['C8'] = 0x0
MASK['SE']['C8'] = 0x408102040000000
MASK['SW']['C8'] = 0x4020
MASK['NE']['C8'] = 0x0
MASK['W']['D8'] = 0x808080
MASK['E']['D8'] = 0x8080808000000000
MASK['S']['D8'] = 0x7f000000
MASK['N']['D8'] = 0x0
MASK['NW']['D8'] = 0x0
MASK['SE']['D8'] = 0x810204000000000
MASK['SW']['D8'] = 0x402010
MASK['NE']['D8'] = 0x0
MASK['W']['E8'] = 0x80808080
MASK['E']['E8'] = 0x8080800000000000
MASK['S']['E8'] = 0x7f00000000
MASK['N']['E8'] = 0x0
MASK['NW']['E8'] = 0x0
MASK['SE']['E8'] = 0x1020400000000000
MASK['SW']['E8'] = 0x40201008
MASK['NE']['E8'] = 0x0
MASK['W']['F8'] = 0x8080808080
MASK['E']['F8'] = 0x8080000000000000
MASK['S']['F8'] = 0x7f0000000000
MASK['N']['F8'] = 0x0
MASK['NW']['F8'] = 0x0
MASK['SE']['F8'] = 0x2040000000000000
MASK['SW']['F8'] = 0x4020100804
MASK['NE']['F8'] = 0x0
MASK['W']['G8'] = 0x808080808080
MASK['E']['G8'] = 0x8000000000000000
MASK['S']['G8'] = 0x7f000000000000
MASK['N']['G8'] = 0x0
MASK['NW']['G8'] = 0x0
MASK['SE']['G8'] = 0x4000000000000000
MASK['SW']['G8'] = 0x402010080402
MASK['NE']['G8'] = 0x0
MASK['W']['H8'] = 0x80808080808080
MASK['E']['H8'] = 0x0
MASK['S']['H8'] = 0x7f00000000000000
MASK['N']['H8'] = 0x0
MASK['NW']['H8'] = 0x0
MASK['SE']['H8'] = 0x0
MASK['SW']['H8'] = 0x40201008040201
MASK['NE']['H8'] = 0x0
MASK['W']['A7'] = 0x0
MASK['E']['A7'] = 0x4040404040404000
MASK['S']['A7'] = 0x3f
MASK['N']['A7'] = 0x80
MASK['NW']['A7'] = 0x0
MASK['SE']['A7'] = 0x1020408102000
MASK['SW']['A7'] = 0x0
MASK['NE']['A7'] = 0x8000
MASK['W']['B7'] = 0x40
MASK['E']['B7'] = 0x4040404040400000
MASK['S']['B7'] = 0x3f00
MASK['N']['B7'] = 0x8000
MASK['NW']['B7'] = 0x80
MASK['SE']['B7'] = 0x102040810200000
MASK['SW']['B7'] = 0x20
MASK['NE']['B7'] = 0x800000
MASK['W']['C7'] = 0x4040
MASK['E']['C7'] = 0x4040404040000000
MASK['S']['C7'] = 0x3f0000
MASK['N']['C7'] = 0x800000
MASK['NW']['C7'] = 0x8000
MASK['SE']['C7'] = 0x204081020000000
MASK['SW']['C7'] = 0x2010
MASK['NE']['C7'] = 0x80000000
MASK['W']['D7'] = 0x404040
MASK['E']['D7'] = 0x4040404000000000
MASK['S']['D7'] = 0x3f000000
MASK['N']['D7'] = 0x80000000
MASK['NW']['D7'] = 0x800000
MASK['SE']['D7'] = 0x408102000000000
MASK['SW']['D7'] = 0x201008
MASK['NE']['D7'] = 0x8000000000
MASK['W']['E7'] = 0x40404040
MASK['E']['E7'] = 0x4040400000000000
MASK['S']['E7'] = 0x3f00000000
MASK['N']['E7'] = 0x8000000000
MASK['NW']['E7'] = 0x80000000
MASK['SE']['E7'] = 0x810200000000000
MASK['SW']['E7'] = 0x20100804
MASK['NE']['E7'] = 0x800000000000
MASK['W']['F7'] = 0x4040404040
MASK['E']['F7'] = 0x4040000000000000
MASK['S']['F7'] = 0x3f0000000000
MASK['N']['F7'] = 0x800000000000
MASK['NW']['F7'] = 0x8000000000
MASK['SE']['F7'] = 0x1020000000000000
MASK['SW']['F7'] = 0x2010080402
MASK['NE']['F7'] = 0x80000000000000
MASK['W']['G7'] = 0x404040404040
MASK['E']['G7'] = 0x4000000000000000
MASK['S']['G7'] = 0x3f000000000000
MASK['N']['G7'] = 0x80000000000000
MASK['NW']['G7'] = 0x800000000000
MASK['SE']['G7'] = 0x2000000000000000
MASK['SW']['G7'] = 0x201008040201
MASK['NE']['G7'] = 0x8000000000000000
MASK['W']['H7'] = 0x40404040404040
MASK['E']['H7'] = 0x0
MASK['S']['H7'] = 0x3f00000000000000
MASK['N']['H7'] = 0x8000000000000000
MASK['NW']['H7'] = 0x80000000000000
MASK['SE']['H7'] = 0x0
MASK['SW']['H7'] = 0x20100804020100
MASK['NE']['H7'] = 0x0
MASK['W']['A6'] = 0x0
MASK['E']['A6'] = 0x2020202020202000
MASK['S']['A6'] = 0x1f
MASK['N']['A6'] = 0xc0
MASK['NW']['A6'] = 0x0
MASK['SE']['A6'] = 0x10204081000
MASK['SW']['A6'] = 0x0
MASK['NE']['A6'] = 0x804000
MASK['W']['B6'] = 0x20
MASK['E']['B6'] = 0x2020202020200000
MASK['S']['B6'] = 0x1f00
MASK['N']['B6'] = 0xc000
MASK['NW']['B6'] = 0x40
MASK['SE']['B6'] = 0x1020408100000
MASK['SW']['B6'] = 0x10
MASK['NE']['B6'] = 0x80400000
MASK['W']['C6'] = 0x2020
MASK['E']['C6'] = 0x2020202020000000
MASK['S']['C6'] = 0x1f0000
MASK['N']['C6'] = 0xc00000
MASK['NW']['C6'] = 0x4080
MASK['SE']['C6'] = 0x102040810000000
MASK['SW']['C6'] = 0x1008
MASK['NE']['C6'] = 0x8040000000
MASK['W']['D6'] = 0x202020
MASK['E']['D6'] = 0x2020202000000000
MASK['S']['D6'] = 0x1f000000
MASK['N']['D6'] = 0xc0000000
MASK['NW']['D6'] = 0x408000
MASK['SE']['D6'] = 0x204081000000000
MASK['SW']['D6'] = 0x100804
MASK['NE']['D6'] = 0x804000000000
MASK['W']['E6'] = 0x20202020
MASK['E']['E6'] = 0x2020200000000000
MASK['S']['E6'] = 0x1f00000000
MASK['N']['E6'] = 0xc000000000
MASK['NW']['E6'] = 0x40800000
MASK['SE']['E6'] = 0x408100000000000
MASK['SW']['E6'] = 0x10080402
MASK['NE']['E6'] = 0x80400000000000
MASK['W']['F6'] = 0x2020202020
MASK['E']['F6'] = 0x2020000000000000
MASK['S']['F6'] = 0x1f0000000000
MASK['N']['F6'] = 0xc00000000000
MASK['NW']['F6'] = 0x4080000000
MASK['SE']['F6'] = 0x810000000000000
MASK['SW']['F6'] = 0x1008040201
MASK['NE']['F6'] = 0x8040000000000000
MASK['W']['G6'] = 0x202020202020
MASK['E']['G6'] = 0x2000000000000000
MASK['S']['G6'] = 0x1f000000000000
MASK['N']['G6'] = 0xc0000000000000
MASK['NW']['G6'] = 0x408000000000
MASK['SE']['G6'] = 0x1000000000000000
MASK['SW']['G6'] = 0x100804020100
MASK['NE']['G6'] = 0x4000000000000000
MASK['W']['H6'] = 0x20202020202020
MASK['E']['H6'] = 0x0
MASK['S']['H6'] = 0x1f00000000000000
MASK['N']['H6'] = 0xc000000000000000
MASK['NW']['H6'] = 0x40800000000000
MASK['SE']['H6'] = 0x0
MASK['SW']['H6'] = 0x10080402010000
MASK['NE']['H6'] = 0x0
MASK['W']['A5'] = 0x0
MASK['E']['A5'] = 0x1010101010101000
MASK['S']['A5'] = 0xf
MASK['N']['A5'] = 0xe0
MASK['NW']['A5'] = 0x0
MASK['SE']['A5'] = 0x102040800
MASK['SW']['A5'] = 0x0
MASK['NE']['A5'] = 0x80402000
MASK['W']['B5'] = 0x10
MASK['E']['B5'] = 0x1010101010100000
MASK['S']['B5'] = 0xf00
MASK['N']['B5'] = 0xe000
MASK['NW']['B5'] = 0x20
MASK['SE']['B5'] = 0x10204080000
MASK['SW']['B5'] = 0x8
MASK['NE']['B5'] = 0x8040200000
MASK['W']['C5'] = 0x1010
MASK['E']['C5'] = 0x1010101010000000
MASK['S']['C5'] = 0xf0000
MASK['N']['C5'] = 0xe00000
MASK['NW']['C5'] = 0x2040
MASK['SE']['C5'] = 0x1020408000000
MASK['SW']['C5'] = 0x804
MASK['NE']['C5'] = 0x804020000000
MASK['W']['D5'] = 0x101010
MASK['E']['D5'] = 0x1010101000000000
MASK['S']['D5'] = 0xf000000
MASK['N']['D5'] = 0xe0000000
MASK['NW']['D5'] = 0x204080
MASK['SE']['D5'] = 0x102040800000000
MASK['SW']['D5'] = 0x80402
MASK['NE']['D5'] = 0x80402000000000
MASK['W']['E5'] = 0x10101010
MASK['E']['E5'] = 0x1010100000000000
MASK['S']['E5'] = 0xf00000000
MASK['N']['E5'] = 0xe000000000
MASK['NW']['E5'] = 0x20408000
MASK['SE']['E5'] = 0x204080000000000
MASK['SW']['E5'] = 0x8040201
MASK['NE']['E5'] = 0x8040200000000000
MASK['W']['F5'] = 0x1010101010
MASK['E']['F5'] = 0x1010000000000000
MASK['S']['F5'] = 0xf0000000000
MASK['N']['F5'] = 0xe00000000000
MASK['NW']['F5'] = 0x2040800000
MASK['SE']['F5'] = 0x408000000000000
MASK['SW']['F5'] = 0x804020100
MASK['NE']['F5'] = 0x4020000000000000
MASK['W']['G5'] = 0x101010101010
MASK['E']['G5'] = 0x1000000000000000
MASK['S']['G5'] = 0xf000000000000
MASK['N']['G5'] = 0xe0000000000000
MASK['NW']['G5'] = 0x204080000000
MASK['SE']['G5'] = 0x800000000000000
MASK['SW']['G5'] = 0x80402010000
MASK['NE']['G5'] = 0x2000000000000000
MASK['W']['H5'] = 0x10101010101010
MASK['E']['H5'] = 0x0
MASK['S']['H5'] = 0xf00000000000000
MASK['N']['H5'] = 0xe000000000000000
MASK['NW']['H5'] = 0x20408000000000
MASK['SE']['H5'] = 0x0
MASK['SW']['H5'] = 0x8040201000000
MASK['NE']['H5'] = 0x0
MASK['W']['A4'] = 0x0
MASK['E']['A4'] = 0x808080808080800
MASK['S']['A4'] = 0x7
MASK['N']['A4'] = 0xf0
MASK['NW']['A4'] = 0x0
MASK['SE']['A4'] = 0x1020400
MASK['SW']['A4'] = 0x0
MASK['NE']['A4'] = 0x8040201000
MASK['W']['B4'] = 0x8
MASK['E']['B4'] = 0x808080808080000
MASK['S']['B4'] = 0x700
MASK['N']['B4'] = 0xf000
MASK['NW']['B4'] = 0x10
MASK['SE']['B4'] = 0x102040000
MASK['SW']['B4'] = 0x4
MASK['NE']['B4'] = 0x804020100000
MASK['W']['C4'] = 0x808
MASK['E']['C4'] = 0x808080808000000
MASK['S']['C4'] = 0x70000
MASK['N']['C4'] = 0xf00000
MASK['NW']['C4'] = 0x1020
MASK['SE']['C4'] = 0x10204000000
MASK['SW']['C4'] = 0x402
MASK['NE']['C4'] = 0x80402010000000
MASK['W']['D4'] = 0x80808
MASK['E']['D4'] = 0x808080800000000
MASK['S']['D4'] = 0x7000000
MASK['N']['D4'] = 0xf0000000
MASK['NW']['D4'] = 0x102040
MASK['SE']['D4'] = 0x1020400000000
MASK['SW']['D4'] = 0x40201
MASK['NE']['D4'] = 0x8040201000000000
MASK['W']['E4'] = 0x8080808
MASK['E']['E4'] = 0x808080000000000
MASK['S']['E4'] = 0x700000000
MASK['N']['E4'] = 0xf000000000
MASK['NW']['E4'] = 0x10204080
MASK['SE']['E4'] = 0x102040000000000
MASK['SW']['E4'] = 0x4020100
MASK['NE']['E4'] = 0x4020100000000000
MASK['W']['F4'] = 0x808080808
MASK['E']['F4'] = 0x808000000000000
MASK['S']['F4'] = 0x70000000000
MASK['N']['F4'] = 0xf00000000000
MASK['NW']['F4'] = 0x1020408000
MASK['SE']['F4'] = 0x204000000000000
MASK['SW']['F4'] = 0x402010000
MASK['NE']['F4'] = 0x2010000000000000
MASK['W']['G4'] = 0x80808080808
MASK['E']['G4'] = 0x800000000000000
MASK['S']['G4'] = 0x7000000000000
MASK['N']['G4'] = 0xf0000000000000
MASK['NW']['G4'] = 0x102040800000
MASK['SE']['G4'] = 0x400000000000000
MASK['SW']['G4'] = 0x40201000000
MASK['NE']['G4'] = 0x1000000000000000
MASK['W']['H4'] = 0x8080808080808
MASK['E']['H4'] = 0x0
MASK['S']['H4'] = 0x700000000000000
MASK['N']['H4'] = 0xf000000000000000
MASK['NW']['H4'] = 0x10204080000000
MASK['SE']['H4'] = 0x0
MASK['SW']['H4'] = 0x4020100000000
MASK['NE']['H4'] = 0x0
MASK['W']['A3'] = 0x0
MASK['E']['A3'] = 0x404040404040400
MASK['S']['A3'] = 0x3
MASK['N']['A3'] = 0xf8
MASK['NW']['A3'] = 0x0
MASK['SE']['A3'] = 0x10200
MASK['SW']['A3'] = 0x0
MASK['NE']['A3'] = 0x804020100800
MASK['W']['B3'] = 0x4
MASK['E']['B3'] = 0x404040404040000
MASK['S']['B3'] = 0x300
MASK['N']['B3'] = 0xf800
MASK['NW']['B3'] = 0x8
MASK['SE']['B3'] = 0x1020000
MASK['SW']['B3'] = 0x2
MASK['NE']['B3'] = 0x80402010080000
MASK['W']['C3'] = 0x404
MASK['E']['C3'] = 0x404040404000000
MASK['S']['C3'] = 0x30000
MASK['N']['C3'] = 0xf80000
MASK['NW']['C3'] = 0x810
MASK['SE']['C3'] = 0x102000000
MASK['SW']['C3'] = 0x201
MASK['NE']['C3'] = 0x8040201008000000
MASK['W']['D3'] = 0x40404
MASK['E']['D3'] = 0x404040400000000
MASK['S']['D3'] = 0x3000000
MASK['N']['D3'] = 0xf8000000
MASK['NW']['D3'] = 0x81020
MASK['SE']['D3'] = 0x10200000000
MASK['SW']['D3'] = 0x20100
MASK['NE']['D3'] = 0x4020100800000000
MASK['W']['E3'] = 0x4040404
MASK['E']['E3'] = 0x404040000000000
MASK['S']['E3'] = 0x300000000
MASK['N']['E3'] = 0xf800000000
MASK['NW']['E3'] = 0x8102040
MASK['SE']['E3'] = 0x1020000000000
MASK['SW']['E3'] = 0x2010000
MASK['NE']['E3'] = 0x2010080000000000
MASK['W']['F3'] = 0x404040404
MASK['E']['F3'] = 0x404000000000000
MASK['S']['F3'] = 0x30000000000
MASK['N']['F3'] = 0xf80000000000
MASK['NW']['F3'] = 0x810204080
MASK['SE']['F3'] = 0x102000000000000
MASK['SW']['F3'] = 0x201000000
MASK['NE']['F3'] = 0x1008000000000000
MASK['W']['G3'] = 0x40404040404
MASK['E']['G3'] = 0x400000000000000
MASK['S']['G3'] = 0x3000000000000
MASK['N']['G3'] = 0xf8000000000000
MASK['NW']['G3'] = 0x81020408000
MASK['SE']['G3'] = 0x200000000000000
MASK['SW']['G3'] = 0x20100000000
MASK['NE']['G3'] = 0x800000000000000
MASK['W']['H3'] = 0x4040404040404
MASK['E']['H3'] = 0x0
MASK['S']['H3'] = 0x300000000000000
MASK['N']['H3'] = 0xf800000000000000
MASK['NW']['H3'] = 0x8102040800000
MASK['SE']['H3'] = 0x0
MASK['SW']['H3'] = 0x2010000000000
MASK['NE']['H3'] = 0x0
MASK['W']['A2'] = 0x0
MASK['E']['A2'] = 0x202020202020200
MASK['S']['A2'] = 0x1
MASK['N']['A2'] = 0xfc
MASK['NW']['A2'] = 0x0
MASK['SE']['A2'] = 0x100
MASK['SW']['A2'] = 0x0
MASK['NE']['A2'] = 0x80402010080400
MASK['W']['B2'] = 0x2
MASK['E']['B2'] = 0x202020202020000
MASK['S']['B2'] = 0x100
MASK['N']['B2'] = 0xfc00
MASK['NW']['B2'] = 0x4
MASK['SE']['B2'] = 0x10000
MASK['SW']['B2'] = 0x1
MASK['NE']['B2'] = 0x8040201008040000
MASK['W']['C2'] = 0x202
MASK['E']['C2'] = 0x202020202000000
MASK['S']['C2'] = 0x10000
MASK['N']['C2'] = 0xfc0000
MASK['NW']['C2'] = 0x408
MASK['SE']['C2'] = 0x1000000
MASK['SW']['C2'] = 0x100
MASK['NE']['C2'] = 0x4020100804000000
MASK['W']['D2'] = 0x20202
MASK['E']['D2'] = 0x202020200000000
MASK['S']['D2'] = 0x1000000
MASK['N']['D2'] = 0xfc000000
MASK['NW']['D2'] = 0x40810
MASK['SE']['D2'] = 0x100000000
MASK['SW']['D2'] = 0x10000
MASK['NE']['D2'] = 0x2010080400000000
MASK['W']['E2'] = 0x2020202
MASK['E']['E2'] = 0x202020000000000
MASK['S']['E2'] = 0x100000000
MASK['N']['E2'] = 0xfc00000000
MASK['NW']['E2'] = 0x4081020
MASK['SE']['E2'] = 0x10000000000
MASK['SW']['E2'] = 0x1000000
MASK['NE']['E2'] = 0x1008040000000000
MASK['W']['F2'] = 0x202020202
MASK['E']['F2'] = 0x202000000000000
MASK['S']['F2'] = 0x10000000000
MASK['N']['F2'] = 0xfc0000000000
MASK['NW']['F2'] = 0x408102040
MASK['SE']['F2'] = 0x1000000000000
MASK['SW']['F2'] = 0x100000000
MASK['NE']['F2'] = 0x804000000000000
MASK['W']['G2'] = 0x20202020202
MASK['E']['G2'] = 0x200000000000000
MASK['S']['G2'] = 0x1000000000000
MASK['N']['G2'] = 0xfc000000000000
MASK['NW']['G2'] = 0x40810204080
MASK['SE']['G2'] = 0x100000000000000
MASK['SW']['G2'] = 0x10000000000
MASK['NE']['G2'] = 0x400000000000000
MASK['W']['H2'] = 0x2020202020202
MASK['E']['H2'] = 0x0
MASK['S']['H2'] = 0x100000000000000
MASK['N']['H2'] = 0xfc00000000000000
MASK['NW']['H2'] = 0x4081020408000
MASK['SE']['H2'] = 0x0
MASK['SW']['H2'] = 0x1000000000000
MASK['NE']['H2'] = 0x0
MASK['W']['A1'] = 0x0
MASK['E']['A1'] = 0x101010101010100
MASK['S']['A1'] = 0x0
MASK['N']['A1'] = 0xfe
MASK['NW']['A1'] = 0x0
MASK['SE']['A1'] = 0x0
MASK['SW']['A1'] = 0x0
MASK['NE']['A1'] = 0x8040201008040200
MASK['W']['B1'] = 0x1
MASK['E']['B1'] = 0x101010101010000
MASK['S']['B1'] = 0x0
MASK['N']['B1'] = 0xfe00
MASK['NW']['B1'] = 0x2
MASK['SE']['B1'] = 0x0
MASK['SW']['B1'] = 0x0
MASK['NE']['B1'] = 0x4020100804020000
MASK['W']['C1'] = 0x101
MASK['E']['C1'] = 0x101010101000000
MASK['S']['C1'] = 0x0
MASK['N']['C1'] = 0xfe0000
MASK['NW']['C1'] = 0x204
MASK['SE']['C1'] = 0x0
MASK['SW']['C1'] = 0x0
MASK['NE']['C1'] = 0x2010080402000000
MASK['W']['D1'] = 0x10101
MASK['E']['D1'] = 0x101010100000000
MASK['S']['D1'] = 0x0
MASK['N']['D1'] = 0xfe000000
MASK['NW']['D1'] = 0x20408
MASK['SE']['D1'] = 0x0
MASK['SW']['D1'] = 0x0
MASK['NE']['D1'] = 0x1008040200000000
MASK['W']['E1'] = 0x1010101
MASK['E']['E1'] = 0x101010000000000
MASK['S']['E1'] = 0x0
MASK['N']['E1'] = 0xfe00000000
MASK['NW']['E1'] = 0x2040810
MASK['SE']['E1'] = 0x0
MASK['SW']['E1'] = 0x0
MASK['NE']['E1'] = 0x804020000000000
MASK['W']['F1'] = 0x101010101
MASK['E']['F1'] = 0x101000000000000
MASK['S']['F1'] = 0x0
MASK['N']['F1'] = 0xfe0000000000
MASK['NW']['F1'] = 0x204081020
MASK['SE']['F1'] = 0x0
MASK['SW']['F1'] = 0x0
MASK['NE']['F1'] = 0x402000000000000
MASK['W']['G1'] = 0x10101010101
MASK['E']['G1'] = 0x100000000000000
MASK['S']['G1'] = 0x0
MASK['N']['G1'] = 0xfe000000000000
MASK['NW']['G1'] = 0x20408102040
MASK['SE']['G1'] = 0x0
MASK['SW']['G1'] = 0x0
MASK['NE']['G1'] = 0x200000000000000
MASK['W']['H1'] = 0x1010101010101
MASK['E']['H1'] = 0x0
MASK['S']['H1'] = 0x0
MASK['N']['H1'] = 0xfe00000000000000
MASK['NW']['H1'] = 0x2040810204080
MASK['SE']['H1'] = 0x0
MASK['SW']['H1'] = 0x0
MASK['NE']['H1'] = 0x0


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
	return MASK["N"][_sq] | MASK["S"][_sq] | MASK["W"][_sq] | MASK["E"][_sq]

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

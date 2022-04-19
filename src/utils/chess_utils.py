
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

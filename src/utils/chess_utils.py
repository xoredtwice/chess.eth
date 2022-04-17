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

PIECE_UNICODES = {
	"W_K": "\u2654",
	"W_Q": "\u2655",
	"W_R": "\u2656",
	"W_B": "\u2657",
	"W_N": "\u2658",
	"W_P": "\u2659",
	"B_K": "\u265A",
	"B_Q": "\u265B",
	"B_R": "\u265C",
	"B_B": "\u265D",
	"B_N": "\u265E",
	"B_P": "\u265F"
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
			view[r][f] = PIECE_UNICODES[PIECE_CODES[i][:3]]
		else :
			pieces[PIECE_CODES[i]] = "X"
		board = board >> 8;

	return pieces, view

# isolating helper functions,
# These functions are not needed on smart contract
from src.pychess.chess_consts import SQUARE_IDS, M_SET
import pickle
import os
from pprint import pprint
from src.utils.logger import setup_logger, lprint, lsection
##########################################################

RANKS = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7}
FILES = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
RANK_CODES = ['1','2','3','4','5','6','7','8']
FILE_CODES = ['A','B','C','D','E','F','G','H']

PIECE_CODES = [
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
    'B_P_H':31
    }
##########################################################
def piece_to_piece_id(piece):
    if piece in PIECE_IDS.keys():
        return PIECE_IDS[piece]
    else:
        return -1
##########################################################
def print_engagements(engagements):
    s = "engagements: {\n"
    i_piece = 0
    j_piece = 0
    while engagements != 0:

        i_unicode = PIECE_UNICODES[PIECE_CODES[i_piece][:3]]
        i_code = PIECE_CODES[i_piece]

        j_unicode = PIECE_UNICODES[PIECE_CODES[engagements[i][j]][:3]]
        j_code = PIECE_CODES[engagements[i][j]]
        
        # there is an engagement from i_piece to j_piece
        if engagements % 2 == 1:
            s = s + f"\n{i_unicode}({i_code}) \t: ["
            s = s + f"{j_unicode}({j_code}), "

        engagements = engagements // 2
        i_piece = i_piece + 1
        if i_piece == 32:
            j_piece = j_piece + 1
            i_piece = 0
            s = s[:-2] + "]"
    lprint(s)

##########################################################
def print_game_state(turn, board64W, board64B, board128, engagements, visibility):
    print(f"Turn: {turn}")
    print_board(board64W)
    print_board(board64B)
    pieces, view = parse_board(board128)
    print_board(view)
    print_engagements(engagements)
##########################################################
def save_game_state(turn, board64W, board64B, board128, engagements, visibility):
    print("saving game state")
    game_state = {}
    game_state["turn"] = turn
    game_state["board64W"] = board64W
    game_state["board64B"] = board64B
    game_state["board128"] = board128
    game_state["engagements"] = engagements
    game_state["visibility"] = visibility
    with open('game_state.pickle', 'wb') as f:
        pickle.dump(game_state, f)
##########################################################
def load_game_state(pickle_path = 'game_state.pickle'):
    if os.path.exists(pickle_path):
        print("loading game state")
        with open(pickle_path, "rb") as f:
            game_state = pickle.load(f)
            turn = game_state["turn"]
            board64W = game_state["board64W"]
            board64B = game_state["board64B"]
            board128 = game_state["board128"]
            engagements = game_state["engagements"]
            visibility = game_state["visibility"]
    else:
        print("initiating game state")
        board64W = 0x00
        board64B = 0x00
        board128 = 0x00
        engagements = 0x00000000000000000000000000000000
        visibility = [0x00] * 32
        turn = 0
    return turn, board64W, board64B, board128, engagements, visibility
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
    return M_SET + (FILES[f_code] << 3) + RANKS[r_code]
##########################################################
def parse_visibility(vis):
    view =  [[" "," "," "," "," "," "," "," "],
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
    lprint("******************")
    for rank in view:
        s = str(i) + "|" 
        for sq in rank:
            s = s + sq + "|"
        lprint(s)
        i = i - 1
    lprint("  a b c d e f g h ")
    lprint("******************")

##########################################################
def parse_board(board):
    pieces = {}
    view =  [[" "," "," "," "," "," "," "," "],
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
            # print(i)
            # print(PIECE_CODES[i][:3])
            # print(PIECE_UNICODES[PIECE_CODES[i][:3]])
            # print(PIECE_UNICODES["B_P"])
            # print()
            view[7-r][f] = PIECE_UNICODES[PIECE_CODES[i][:3]]
        else :
            pieces[PIECE_CODES[i]] = "X"
        board = board >> 8;

    return pieces, view
##########################################################
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
            lprint(f"MASK['{direction}']['{sq}'] = {hex(m[direction])}")
            # print_board(m[direction])
##########################################################
def build_diagonal_masks():
    d1 = build_mask(["A1"])
    # print_board(parse_visibility(d1))
    lprint(f"'+1' : {hex(d1)},")

    d2 = d1
    di = 2
    for i in range(7):
        d2 = (d2 | (0x80 << (i*8))) << 1
        # print_board(parse_visibility(d2))
        lprint(f"'+{di}' : {hex(d2)},")
        di = di + 1

    for i in range(7):
        d2 = (d2 & ~(0x80 << (i*8))) << 1
        # print_board(parse_visibility(d2))
        lprint(f"'+{di}' : {hex(d2)},")
        di = di + 1

    d16 = build_mask(["H1"])
    # print_board(parse_visibility(d16))
    lprint(f"'-1': {hex(d2)},")

    d2 = d16
    di = 2
    for i in range(7):
        d2 = (d2  << 1) | (0x01 << ((6-i)*8))
        # print_board(parse_visibility(d2))
        lprint(f"'-{di}': {hex(d2)},")
        di = di + 1

    for i in range(7):
        d2 = (d2 << 1) & ~(0x101010101010101)
        # print_board(parse_visibility(d2))
        lprint(f"'-{di}': {hex(d2)},")
        di = di + 1

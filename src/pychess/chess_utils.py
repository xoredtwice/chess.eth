# isolating helper functions,
# These functions are not needed on smart contract
from src.pychess.chess_consts import SQUARE_IDS
import pickle
import os
##########################################################
def save_game_state(board64, board128, engagements, visibility)
    print("saving game state")
    game_state = {}
    game_state["board64"] = board64
    game_state["board128"] = board128
    game_state["engagements"] = engagements
    game_state["visibility"] = visibility
    with open('game_state.pickle', 'wb') as f:
        pickle.dump(game_state, f)
##########################################################
def load_game_state(pickle_path = 'game_state.pickle')
    if os.path.exists(pickle_path):
        print("loading game state")
        with open(pickle_path) as f:
            game_state = pickle.load(f)
            board64 = game_state["board64"]
            board128 = game_state["board128"]
            engagements = game_state["engagements"]
            visibility = game_state["visibility"]
    else:
        print("initiating game state")
        board64 = 0x00
        board128 = 0x00
        engagements = {}
        visibility = {}
    return board64, board128, engagements, visibility
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
##########################################################
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

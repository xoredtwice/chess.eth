
def is_check():
    print("not implemented")

def is_mate():
    print("not implemented")

def is_draw():
    print("not implemented")

def end_game():
    print("not implemented")

def update_threat_map(new_move)
    print("not implemented")

    # 64 places, 8*8 bit threat map

def move(address, new_move):
    print("Not implemented")
    if is_move_valid(new_move):
        do_move(new_move)
        update_threat_map(new_move)
        if is_mate() or is_draw():
            end_game()
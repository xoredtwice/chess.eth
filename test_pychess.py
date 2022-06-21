import os
import sys
import argparse
import pathlib
import json

from src.utils.logger import setup_logger, lprint, lsection
from src.utils.yaml_wrapper import load_configuration
from src.pychess.chess_core import rook, bishop, queen, pawn_white, pawn_black, knight, move
from src.pychess.chess_consts import SQUARE_IDS
from src.pychess.chess_utils import print_board, build_mask, load_game_state, save_game_state, piece_to_piece_id, build_state, parse_board, print_game_state
############################################################################33

root_path = str(pathlib.Path(__file__).parent.resolve())

parser = argparse.ArgumentParser(description='Testing Python version of chess.eth')
parser.add_argument('-f', dest='conf_path', type=ascii, default=os.path.join(root_path, "conf", "00_default_configuration.yaml"),
                    help='configuration YAML file path')
parser.add_argument('-c', dest='command', type=ascii, default='move',
                    help='list of tests used for engine developement')
parser.add_argument('-p', dest='piece', type=ascii, default='queen',
                    help='the piece to move.')
parser.add_argument('-s', dest='square', type=ascii, default="E4",
                    help='The square to place the piece in.')
args = parser.parse_args()

conf = load_configuration(os.path.abspath(args.conf_path[1:-1]))

log_path = os.path.join(root_path, "log")
if not os.path.exists(log_path):
    os.makedirs(log_path)
setup_logger(log_path, conf["id"])

square = args.square[1:-1]
square = SQUARE_IDS[square]
piece = args.piece[1:-1]
if "'visibility'" in args.command:
    # board64 = build_mask(["B1", "C1"])

    lsection(f"[[Testing Visibility of {args.piece} in {args.square}]]")
    # print("Board state: ")
    # print_board(board64)

    vis64 = 0x00
    if "'rook'" in args.piece:
        vis64 = rook(board64, square)
    if "'bishop'" in args.piece:
        vis64 = bishop(board64, square)
    if "'queen'" in args.piece:
        vis64 = queen(board64, square)
    if "'pawnw'" in args.piece:
        vis64 = pawn_white(square)
    if "'pawnb'" in args.piece:
        vis64 = pawn_black(square)
    if "'king'" in args.piece:
        vis64 = king(square)
    if "'knight'" in args.piece:
        vis64 = knight(square)

    print("Visibility: ")
    print_board(vis64)
elif "'move'" in args.command:
    turn, board64W, board64B, board128, engagements, visibility = load_game_state()

    lsection(f"[[Testing Move of {args.piece} to {args.square}]]")

    piece_id = piece_to_piece_id(args.piece[1:-1])
    state = build_state(args.square[1:-1])
    print(f"piece_id:{piece_id}, state:{state}")

    # print("Pre-move state")
    # print_game_state(board64W, board64B, board128, engagements, visibility)

    board64W, board64B, board128, engagements, visibility = move(board64W, board64B, board128, engagements, visibility, piece_id, state)
    print("Post-move state")
    print_game_state(turn, board64W, board64B, board128, engagements, visibility)

    turn = ~ turn
    save_game_state(turn, board64W, board64B, board128, engagements, visibility)
elif "'clear'" in args.command:
    lsection(f"[[Clearing the state]]")
    if os.path.exists(conf["pychess"]["state-file"]):
        os.remove(conf["pychess"]["state-file"])

############################################################################33

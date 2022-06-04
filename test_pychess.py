import os
import sys
import argparse
import pathlib
import json

from src.utils.logger import setup_logger, lprint, lsection
from src.utils.yaml_wrapper import load_configuration
from src.pychess.chess_core import rook, bishop, queen, pawn_white, pawn_black, move
from src.pychess.chess_utils import print_board, build_mask, load_game_state, save_game_state, piece_to_piece_id, build_state, parse_board
############################################################################33

root_path = str(pathlib.Path(__file__).parent.resolve())

parser = argparse.ArgumentParser(description='Testing Python version of chess.eth')
parser.add_argument('-f', dest='conf_path', type=ascii, default=os.path.join(root_path, "conf", "00_default_configuration.yaml"),
                    help='configuration YAML file path')
parser.add_argument('-t', dest='test', type=ascii, default='move',
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
piece = args.piece[1:-1]
if "'visibility'" in args.test:
	board64 = build_mask(["F3", "E3", "C5"])

	lsection(f"[[Testing Visibility of {args.piece} in {args.square}]]")
	print("Board state: ")
	print_board(board64)

	vis64 = 0x00
	if "'rook'" in args.piece:
		vis64 = rook( board64, square)
	if "'bishop'" in args.piece:
		vis64 = bishop(board64, square)
	if "'queen'" in args.piece:
		vis64 = queen(board64, square)
	if "'pawnw'" in args.piece:
		vis64 = pawn_white(board64, square)
	if "'pawnb'" in args.piece:
		vis64 = pawn_black(board64, square)
	if "'king'" in args.piece:
		vis64 = king(board64, square)
	if "'knight'" in args.piece:
		vis64 = knight(board64, square)

	print("Visibility: ")
	print_board(vis64)
elif "'move'" in args.test:
	board64, board128, engagements, visibility = load_game_state()

	lsection(f"[[Testing Move of {args.piece} to {args.square}]]")

	piece_id = piece_to_piece_id(args.piece[1:-1])
	state = build_state(args.square[1:-1])
	print(f"piece_id:{piece_id}, state:{state}")
	print("Pre-move board64")
	print_board(board64)
	print("Pre-move board128")
	pieces, view = parse_board(board128)
	print_board(view)


	board64, board128, engagements, visibility = move(board64, board128, engagements, visibility, piece_id, state)

	print("post-move board64")
	print_board(board64)
	print("post-move board128")
	pieces, view = parse_board(board128)
	print_board(view)

	save_game_state(board64, board128, engagements, visibility)

############################################################################33

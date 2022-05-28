import os
import sys
import argparse
import pathlib
import json

from src.utils.logger import setup_logger, lprint, lsection
from src.utils.yaml_wrapper import load_configuration
from src.pychess.chess_core import rook, bishop, queen, pawn_white, pawn_black
from src.pychess.chess_utils import print_board, build_mask
############################################################################33

root_path = str(pathlib.Path(__file__).parent.resolve())

parser = argparse.ArgumentParser(description='Testing Python version of chess.eth')
parser.add_argument('-f', dest='conf_path', type=ascii, default=os.path.join(root_path, "conf", "00_default_configuration.yaml"),
                    help='configuration YAML file path')
parser.add_argument('-p', dest='piece', type=ascii, default='queen',
                    help='list of tests used for engine developement')
parser.add_argument('-s', dest='square', type=ascii, default="E4",
                    help='The square to place the piece in.')
args = parser.parse_args()

conf = load_configuration(os.path.abspath(args.conf_path[1:-1]))

log_path = os.path.join(root_path, "log")
if not os.path.exists(log_path):
	os.makedirs(log_path)
setup_logger(log_path, conf["id"])

square = args.square[1:-1]
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
############################################################################33

import os
import sys
import argparse
import pathlib
import json

from src.utils.logger import setup_logger, lprint, lsection
from src.utils.yaml_wrapper import load_configuration
from src.pychess.chess_core import rook, bishop
from src.pychess.chess_utils import print_board, build_mask
############################################################################33

root_path = str(pathlib.Path(__file__).parent.resolve())

parser = argparse.ArgumentParser(description='Testing Python version of chess.eth')
parser.add_argument('-f', dest='conf_path', type=ascii, default=os.path.join(root_path, "conf", "00_default_configuration.yaml"),
                    help='configuration YAML file path')
parser.add_argument('-c', dest='commands', type=ascii, nargs='+',
                    default='rook',
                    help='list of tests used for engine developement')

args = parser.parse_args()

conf = load_configuration(os.path.abspath(args.conf_path[1:-1]))

log_path = os.path.join(root_path, "log")
if not os.path.exists(log_path):
	os.makedirs(log_path)
setup_logger(log_path, conf["id"])

if "'rook'" in args.commands:
	lsection("[[ROOK TEST]]")
	print_board(rook( build_mask(["F3"]), "B3"))
if "'bishop'" in args.commands:
	lsection("[[BISHOP TEST]]")
	print_board(bishop( build_mask(["F3", "C4"]), "B3"))
############################################################################33

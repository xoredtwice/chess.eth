import os
import sys
import argparse
import pathlib
import json

from src.utils.logger import setup_logger, lprint, lsection
from src.utils.yaml_wrapper import load_configuration
from src.run.s0_prepare import s0_create_chess_project, s0_create_token_project
from src.run.s1_compile import s1_compile_chess_project, s1_compile_token_project
from src.run.s2_deploy import s2_deploy_chess_project, s2_deploy_token_project
from src.run.s3_simulate import s3_simulate_chess
############################################################################33

root_path = str(pathlib.Path(__file__).parent.resolve())

parser = argparse.ArgumentParser(description='Chess.eth local runner')
parser.add_argument('-f', dest='conf_path', type=ascii, default=os.path.join(root_path, "conf", "00_default_configuration.yaml"),
                    help='configuration YAML file path')
parser.add_argument('-c', dest='commands', type=ascii, nargs='+',
                    default='all',
                    help='list of commands to execute from: create, compile, deploy and simulate.')

args = parser.parse_args()

conf = load_configuration(os.path.abspath(args.conf_path[1:-1]))

log_path = os.path.join(root_path, "log")
if not os.path.exists(log_path):
	os.makedirs(log_path)
setup_logger(log_path, conf["id"])

receipts = {}

if "'create'" in args.commands or "'all'" in args.commands:
	lsection("[[CREATE]]")
	build_path = os.path.join(root_path, "build")
	if not os.path.exists(build_path):
		os.makedirs(build_path)
	s0_create_token_project(root_path)
	s0_create_chess_project(root_path, "chess")
	lprint("Create step completed!")

if "'compile'" in args.commands or "'all'" in args.commands:
	lsection("[[COMPILE]]")
	s1_compile_token_project(root_path)
	s1_compile_chess_project(root_path, "chess")
	lprint("Compile step completed!")

if "'deploy'" in args.commands or "'all'" in args.commands:
	lsection("[[DEPLOY]]")
	for token in conf["tokens"]:
		receipts[token["name"]] = s2_deploy_token_project(root_path, conf["network"], token)
	receipts["chess"] = s2_deploy_chess_project(root_path, conf["network"], conf["chess"], receipts[conf["tokens"][0]["name"]])

	receipts_path = os.path.join(root_path, "build", "deploy_receipts.json")
	receipts_file = open(receipts_path, "w")
	json.dump(receipts, receipts_file,  default=lambda o: o.__dict__, indent=4)
	receipts_file.close()
	lprint("Deploy step completed! Receipts have been saved into " + str(receipts_path))

if "'simulate'" in args.commands or "'all'" in args.commands:
	lsection("[[SIMULATE]]")
	s3_simulate_chess(root_path, conf)
############################################################################33

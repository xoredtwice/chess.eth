import json
from pprint import pprint
from web3 import Web3

from solcx import compile_standard, install_solc
import os
from dotenv import load_dotenv
import pathlib
import shutil

from brownie import *
import subprocess
from tempfile import mkstemp
from shutil import move, copymode
from run.utils.utils import replace_in_file
from run.utils.logger import lprint, lsection
#*******************************************************************************
def s1_compile_token_project(root_path):
    lsection("[Compiling shared subprojects]",1)

    # Compiling ERC20 project
    erc20_path = os.path.join(root_path, "build", "erc20")
    lprint("changing directory to " + erc20_path)
    os.chdir(erc20_path)
    subprocess.run(["brownie", "compile", "all"])
#*******************************************************************************
def s1_compile_chess_project(root_path, project_name):
    project_path = os.path.join(root_path, "build", project_name)

    lsection("[Compiling exchange subprojects]", 1)

    # Compiling core project
    core_path = os.path.join(project_path, "core")
    lprint("changing directory to " + core_path)
    os.chdir(core_path)
    subprocess.run(["brownie", "compile", "all"])

if __name__ == "__main__":
    s1_compile_exchange()

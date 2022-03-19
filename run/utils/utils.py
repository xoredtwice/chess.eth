from tempfile import mkstemp
from shutil import move, copymode
import os
import json
from pprint import pprint
from brownie import Contract
from web3 import Web3
#*******************************************************************************
def replace_in_file(filepath, current_text, new_text):
   fd, abspath = mkstemp()
   with os.fdopen(fd,'w') as file1:
       with open(filepath,'r') as file0:
           for line in file0:
               file1.write(line.replace(current_text, new_text))
   copymode(filepath, abspath)
   os.remove(filepath)
   move(abspath, filepath)
#*******************************************************************************
def get_brownie_provider(compiled_path, contract_filename, deploy_address, owner_address):
    with open(compiled_path, "r") as file:
        compiled_sol = json.load(file)
    compiled_abi = compiled_sol["abi"]
    return Contract.from_abi(contract_filename[-4], deploy_address, abi = compiled_abi, owner = owner_address)

#*******************************************************************************
def load_web3_environment(network):
    ###############################################################################
    # Preparing environment
    ################################################################################
    connection_string = "http://"+ network["host"] + ":" + network["port"]
    w3 = Web3(Web3.HTTPProvider(connection_string))

    pprint(network["accounts"])

    # Submit the transaction that deploys the contract
    chain_id = int(network["chain-id"])

    return w3, chain_id, network["accounts"]

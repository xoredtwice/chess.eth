import os
import json
from pprint import pprint
from brownie import Contract
from web3 import Web3
#*******************************************************************************
def get_brownie_provider(compiled_path, contract_filename, deploy_address, owner_address):
    with open(compiled_path, "r") as file:
        compiled_sol = json.load(file)
    compiled_abi = compiled_sol["abi"]
    return Contract.from_abi(contract_filename[-4], deploy_address, abi = compiled_abi, owner = owner_address)
#*******************************************************************************
def load_web3_environment(network):
    connection_string = "http://"+ network["host"] + ":" + network["port"]
    w3 = Web3(Web3.HTTPProvider(connection_string))
    # Submit the transaction that deploys the contract
    chain_id = int(network["chain-id"])

    return w3, chain_id, network["accounts"]
#*******************************************************************************
# def read_pieces():

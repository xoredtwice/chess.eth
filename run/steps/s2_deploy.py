import json
from pprint import pprint
from web3 import Web3
import os
import pathlib
import shutil
from run.utils.logger import lprint, lsection
#*******************************************************************************
#*******************************************************************************
#*******************************************************************************
def load_deploy_environment(network):
    ###############################################################################
    # Preparing environment
    ################################################################################
    connection_string = "http://"+ network["host"] + ":" + network["port"]
    w3 = Web3(Web3.HTTPProvider(connection_string))

    lprint("Using Account_00 for deployment")
    my_key = network["accounts"][0]["private"]
    my_address = network["accounts"][0]["address"]

    lprint("private: " + my_key)
    lprint("address: " + my_address)

    # Submit the transaction that deploys the contract
    chain_id = int(network["chain-id"])

    return w3, chain_id, my_key, my_address
#*******************************************************************************
def s2_deploy_token_project(root_path, network, token):
    lsection("[ERC20 Deploy script]", 1)

    w3, chain_id, private_key, my_address = load_deploy_environment(network)

    nonce = w3.eth.getTransactionCount(my_address)
    build_path = os.path.join(root_path, "build")

    token_name = token["name"]
    token_symbol = token["symbol"]

    lprint("Deploying token " + token_name + "(" + token_symbol + ")")
    
    erc20_path = os.path.join(build_path, "erc20", "build", "contracts", "ERC20.json")
    with open(erc20_path, "r") as file:
        compiled_erc20 = json.load(file)

    erc20_bytecode = compiled_erc20["bytecode"]
    erc20_abi = compiled_erc20["abi"]
    ##############################################################################
    token_contract = w3.eth.contract(abi=erc20_abi, bytecode=erc20_bytecode)
    token_transaction = token_contract.constructor(token_name, token_symbol).buildTransaction(
        {"gasPrice": w3.eth.gas_price, "chainId": chain_id, "from": my_address, "nonce": nonce}
    )

    token_signed_txn = w3.eth.account.sign_transaction(token_transaction, private_key=private_key)
    token_tx_hash = w3.eth.send_raw_transaction(token_signed_txn.rawTransaction)
    token_receipt = w3.eth.wait_for_transaction_receipt(token_tx_hash)

    lprint("Token" + token_name + f" deployed to: {token_receipt.contractAddress}")

    return token_receipt
#*******************************************************************************
def s2_deploy_chess_project(root_path, network, chess, token_receipt):
    lsection(f"[Chess Deploy script]", 1)

    w3, chain_id, private_key, my_address = load_deploy_environment(network)
    nonce = w3.eth.getTransactionCount(my_address)

    chess_path = os.path.join(root_path, "build", "chess")

    ################################################################################
    # deploying uni-core 
    ################################################################################
    lprint(f"Deploying chess.lobby ...")

    lobby_path = os.path.join(chess_path, "core", "build", "contracts", "ChessLobby.json")
    with open(lobby_path, "r") as file:
        compiled_lobby = json.load(file)

    lobby_bytecode = compiled_lobby["bytecode"]
    lobby_abi = compiled_lobby["abi"]

    lobby_contract = w3.eth.contract(abi=lobby_abi, bytecode=lobby_bytecode)
    lobby_transaction = lobby_contract.constructor(my_address).buildTransaction(
        {"gasPrice": w3.eth.gas_price, "chainId": chain_id, "from": my_address, "nonce": nonce}
    )
    lobby_signed_txn = w3.eth.account.sign_transaction(lobby_transaction, private_key=private_key)
    lobby_tx_hash = w3.eth.send_raw_transaction(lobby_signed_txn.rawTransaction)
    lobby_receipt = w3.eth.wait_for_transaction_receipt(lobby_tx_hash)

    lprint(f"chess.lobby has been deployed to {lobby_receipt.contractAddress}")

    receipts = {}
    receipts["LOBBY"] = lobby_receipt

    return receipts

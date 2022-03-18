import json
from pprint import pprint
import web3
from web3 import Web3
import os
import pathlib
import shutil
import time
import eth_event
import traceback
from brownie import *
from scripts.utils.utils import get_brownie_provider
from scripts.utils.logger import lprint, lsection
from run.utils.utils import load_web3_environment
#*******************************************************************************
#*******************************************************************************
def s3_simulate_game_initialization(root_path, network, receipts, tokens):
    build_path = os.path.join(root_path, "build")

    w3, chain_id, private_key, my_address = load_web3_environment(network)

    # pprint(receipts)
    for key in receipts:
        lprint(key + " @ " + receipts[key]["contractAddress"])

    t1_address = receipts[tokens[0]["name"]]["contractAddress"]

    ###############################################################################
    # Minting tokens
    ################################################################################
    erc20_path = os.path.join(build_path, "erc20", "build", "contracts", "ERC20.json")
    t1_provider = get_brownie_provider(erc20_path, "ERC20.sol", t1_address, my_address)
    ##############################################################################
    try:

        t1_name = t1_provider.name()
        t1_mint_amount = w3.toWei(exchange["initial-mint"][0], 'ether')

        lprint("\nMinting " + str(t1_mint_amount) + "  of " + t1_name + " for: " + str(my_address))

        t1_provider.mint(my_address, t1_mint_amount)
        t1_mint_result = t1_provider.balanceOf(my_address)

        lprint("Minted " + str(t1_mint_result) + " " + t1_name+ " for: " + str(my_address))
    except Exception as ex:
        lprint("Exception in sending t1.mint")
        lprint(ex)
        lprint(history[-1].call_trace(True))
    
    # ###############################################################################
    # # Sitting with two different addresses
    # ################################################################################
    lprint("\n\nlobby.sitAndWait()")
    # factory_path = os.path.join(build_path, exchange["name"], "core", "build", "contracts", "UniswapV2Factory.json")
    # factory_provider = get_brownie_provider(factory_path, "UniswapV2Factory.sol", receipts["FACTORY"]["contractAddress"], my_address)
    # # ################################################################################
    # try:
    #     cp_tx = factory_provider.createPair(t1_address, t2_address)
    #     lprint(str(cp_tx.events["PairCreated"]) + "\n")
    #     pair_address = cp_tx.events["PairCreated"]["pair"]
    # except Exception as ex:
    #     lprint("Exception in sending factory.createPair")
    #     lprint(ex)
    #     lprint(history[-1].call_trace(True))
    # ###############################################################################
    #  transferring initial tokens to players
    # ################################################################################
    # try:
    #     lprint("\n\nt1.approve()")
    #     t1_approve_amount = w3.toWei(exchange["approvals"][0], 'ether')
    #     uni_r2_address = receipts["ROUTER_02"]["contractAddress"]
    #     a1_tx = t1_provider.approve(uni_r2_address, t1_approve_amount)
    #     lprint(str(a1_tx.events["Approval"]) + "\n")
    # except Exception as ex:
    #     lprint("Exception in sending Approve")
    #     lprint(ex)
    #     lprint(history[-1].call_trace(True))
    # ###############################################################################
    #  Sending pair.getReserves()
    # ################################################################################
    # lprint("\n\npair.getReserves()")
    # try:
    #     lprint("Generated pair address: " + str(pair_address))
    #     pair_path = os.path.join(build_path, exchange["name"], "core", "build", "contracts", "UniswapV2Pair.json")
    #     pair_provider = get_brownie_provider(pair_path, "UniswapV2Pair.sol", pair_address, my_address)
        
    #     reserves = pair_provider.getReserves()

    #     lprint("pair.getReserves() -> " + str(reserves))
    # except Exception as ex:
    #     lprint("Exception in sending pair.getReserves()")
    #     lprint(ex)
    #     lprint(history[-1].call_trace(True))

def s3_simulate_chess(root_path, conf):
    ###############################################################################
    # Preparing environment
    ################################################################################
    network.connect('development')

    receipts_path = os.path.join(root_path, "build", "deploy_receipts.json")

    lprint("\nLoading receipts from " + str(receipts_path))
    receipts_file = open(receipts_path, "r")
    receipts = json.load(receipts_file)
    receipts_file.close()

    s3_simulate_game_initialization(root_path, conf["network"] receipts)



if __name__ == "__main__":
    s3_simulate_experiment(None)

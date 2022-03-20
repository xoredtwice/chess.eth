import json
from pprint import pprint
import os
import pathlib
import shutil
import time
import eth_event
import traceback
import brownie
from run.utils.utils import get_brownie_provider, load_web3_environment
from run.utils.logger import lprint, lsection, lexcept
#*******************************************************************************
#*******************************************************************************
def s3_simulate_game_initialization(root_path, network, receipts, tokens, players):
    build_path = os.path.join(root_path, "build")

    w3, chain_id, accounts = load_web3_environment(network)
    brownie.network.gas_price(10)
    brownie.network.gas_limit(7000000)

    house_address = accounts[0]['address']
    house_private = accounts[0]['private']

    p1_address = accounts[1]['address']
    p1_private = accounts[1]['private']

    p2_address = accounts[2]['address']
    p2_private = accounts[2]['private']


    token_address = receipts[tokens[0]["name"]]["contractAddress"]
    erc20_path = os.path.join(build_path, "erc20", "build", "contracts", "ERC20.json")
    token_provider = get_brownie_provider(erc20_path, "ERC20.sol", token_address, house_address)
    p1_token_provider = get_brownie_provider(erc20_path, "ERC20.sol", token_address, p1_address)
    p2_token_provider = get_brownie_provider(erc20_path, "ERC20.sol", token_address, p2_address)

    token_name = token_provider.name()
    token_mint_amount = w3.toWei(tokens[0]["initial-mint"], 'kwei')

    lobby_path = os.path.join(build_path, "chess", "core", "build", "contracts", "ChessLobby.json")
    p1_lobby_provider = get_brownie_provider(lobby_path, "ChessLobby.sol", receipts["chess"]["LOBBY"]["contractAddress"], p1_address)
    p2_lobby_provider = get_brownie_provider(lobby_path, "ChessLobby.sol", receipts["chess"]["LOBBY"]["contractAddress"], p2_address)

    p1_token_amount = w3.toWei(players[0]['initial-token'], 'kwei')
    p1_deposit_amount = w3.toWei(1, 'kwei')
    p2_token_amount = w3.toWei(players[1]['initial-token'], 'kwei')
    p2_deposit_amount = w3.toWei(1, 'kwei')

    ###############################################################################
    # Minting tokens
    ###############################################################################
    try:
        lsection("[HOUSE calls chessToken.mint()]", 1)
        lprint("Minting " + str(token_mint_amount) + "  of " + token_name + " for: " + str(house_address))
        mint_tx = token_provider.mint(house_address, token_mint_amount)
        lprint(str(mint_tx.events["Transfer"]) + "\n")
    except Exception as ex:
        lprint("Exception in sending token.mint")
        lexcept(ex, True)
    ###############################################################################
    # transferring initial tokens to players
    ################################################################################
    try:
        lsection("[HOUSE calls chessToken.transfer(PLAYER1])", 1)
        p1_tr_tx = token_provider.transfer(p1_address, p1_token_amount)
        lprint(str(p1_tr_tx.events["Transfer"]) + "\n")
    except Exception as ex:
        lprint(f"Exception in sending token.transfer({p1_address},{p1_token_amount})")
        lexcept(ex, True)

    try:
        lsection("[HOUSE calls chessToken.transfer(PLAYER2)]", 1)
        p2_tr_tx = token_provider.transfer(p2_address, p2_token_amount)
        lprint(str(p2_tr_tx.events["Transfer"]) + "\n")
    except Exception as ex:
        lprint(f"Exception in sending token.transfer({p2_address},{p2_token_amount})")
        lexcept(ex, True)

    # ###############################################################################
    #  player1 sends approve and deposits
    # ################################################################################
    try:
        lsection("[PLAYER1 calls token.approve(HOUSE, amount)]",1)
        p1_ap_tx = p1_token_provider.approve(house_address, p1_deposit_amount)
        lprint(str(p1_ap_tx.events["Approval"]) + "\n")
    except Exception as ex:
        lprint(f"Exception in sending token.approve({p1_address},{p1_token_amount})")
        lexcept(ex, True)

    try:
        lsection("[PLAYER1 calls lobby.deposit(amount)]", 1)
        p1_dp_tx = p1_lobby_provider.deposit(p1_deposit_amount)
        lprint(str(p1_dp_tx.events["PlayerDeposited"]) + "\n")
    except Exception as ex:
        lprint(f"Exception in sending lobby({p1_deposit_amount})")
        lexcept(ex, True)

    # ###############################################################################
    #  player2 sends approve and deposits
    # ################################################################################
    try:
        lsection("[PLAYER2 calls token.approve(HOUSE, amount)]",1)
        p2_ap_tx = p2_token_provider.approve(house_address, p2_deposit_amount)
        lprint(str(p2_ap_tx.events["Approval"]) + "\n")
    except Exception as ex:
        lprint(f"Exception in sending token.approve({p2_address},{p2_token_amount})")
        lexcept(ex, True)

    try:
        lsection("[PLAYER2 calls lobby.deposit(amount)]", 1)
        p2_dp_tx = p2_lobby_provider.deposit(p2_deposit_amount)
        lprint(str(p2_dp_tx.events["PlayerDeposited"]) + "\n")
    except Exception as ex:
        lprint(f"Exception in sending lobby({p2_deposit_amount})")
        lexcept(ex, True)
    # ###############################################################################
    # # Sitting with player1 and player2
    # ################################################################################
    # lprint("player1 calls lobby.sitAndWait()")
    # lobby_path = os.path.join(build_path, "chess", "core", "build", "contracts", "ChessLobby.json")
    # # ################################################################################
    # try:
    #     p1_game_options = 0
    #     cp_tx = p1_lobby_provider.sitAndWait(p1_game_options)
    #     lprint(str(cp_tx.events["PlayerSit"]) + "\n")
    # except Exception as ex:
    #     lprint("Exception in sending lobby.sitAndWait() by player1")
    #     lprint(ex)
    #     lprint(history[-1].call_trace(True))

    # lprint("player2 calls lobby.sitAndWait()")
    # p2_lobby_provider = get_brownie_provider(lobby_path, "ChessLobby.sol", receipts["chess"]["LOBBY"]["contractAddress"], p2_address)
    # # ################################################################################
    # try:
    #     p2_game_options = 0
    #     p2_sit_tx = p2_lobby_provider.sitAndWait(p2_game_options)
    #     lprint(str(p2_sit_tx.events["PlayerSit"]) + "\n")
    # except Exception as ex:
    #     lprint("Exception in sending lobby.sitAndWait() by player1")
    #     lprint(ex)
    #     lprint(history[-1].call_trace(True))

def s3_simulate_chess(root_path, conf):
    ###############################################################################
    # Preparing environment
    ################################################################################
    brownie.network.connect('development')
    receipts_path = os.path.join(root_path, "build", "deploy_receipts.json")

    lprint("\nLoading receipts from " + str(receipts_path))
    receipts_file = open(receipts_path, "r")
    receipts = json.load(receipts_file)
    receipts_file.close()

    s3_simulate_game_initialization(root_path, conf["network"], receipts, conf["tokens"], conf["chess"]["players"])

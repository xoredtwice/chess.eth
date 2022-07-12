import os
import json
from pprint import pprint
from brownie import Contract
from web3 import Web3
from src.logger import lprint, lsection, lexcept
from src.helpers.chess_helpers import parse_board, print_board, PIECE_IDS
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
def send_move(player_address, player_provider, piece, action):
    try:
        tx = player_provider.move(piece, action);
        return json.dumps(dict(tx.events['PlayerMoved']), indent=4)
    except Exception as ex:
        lprint(f"Exception in sending move() by {player_address}")
        # lexcept(ex, True)
        return None
#*******************************************************************************
def read_boards(player_address, player_provider):
    try:
        return player_provider.board64W(), player_provider.board64B();
    except Exception as ex:
        lprint(f"Exception in sending table.board64W() or table.board64B() by {player_address}")
        # lexcept(ex, True)
        return None
#*******************************************************************************
def read_pieces(player_address, player_provider):
    try:
        return player_provider.pieces();
    except Exception as ex:
        lprint(f"Exception in sending table.pieces() by {player_address}")
        # lexcept(ex, True)
        return None
#*******************************************************************************
def send_move_and_read(player_tag, player_address, player_provider, piece, action):

    lsection(f"[{player_tag} sends {hex(piece)},{hex(action)}]", 1)

    ev = send_move(player_address, player_provider, piece, action)
    lprint(f"[EVENT] ChessTable.PlayerMoved: {ev}")

    lsection(f"[{player_tag} reads the pieces]", 1)
    pieces256 = read_pieces(player_address, player_provider)
    lprint(f"pieces value: {hex(pieces256)}")
    pieces, view = parse_board(pieces256)
    lprint(f"parsed pieces:{pieces}")
    print_board(view)

    board64W, board64B = read_boards(player_address, player_provider)

    # print_board(board64W)
    # print_board(board64B)
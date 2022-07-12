import json
import os
import brownie
from src.web3 import get_brownie_provider, load_web3_environment, send_move_and_read
from src.logger import lprint, lsection, lexcept
from src.helpers.chess_helpers import parse_board, print_board, PIECE_IDS, square_id
from pprint import pprint
#*******************************************************************************
#*******************************************************************************
def s3_simulate_game_initialization(root_path, network, receipts, tokens, players):
    build_path = os.path.join(root_path, "build")

    w3, chain_id, accounts = load_web3_environment(network)
    brownie.network.gas_price(10)
    brownie.network.gas_limit(700000000)

    house_address = accounts[0]['address']
    house_private = accounts[0]['private']

    p1_address = accounts[1]['address']
    p1_private = accounts[1]['private']

    p2_address = accounts[2]['address']
    p2_private = accounts[2]['private']

    lobby_address = receipts["chess"]["LOBBY"]["contractAddress"]


    token_address = receipts[tokens[0]["name"]]["contractAddress"]
    erc20_path = os.path.join(build_path, "erc20", "build", "contracts", "ERC20.json")
    token_provider = get_brownie_provider(erc20_path, "ERC20.sol", token_address, house_address)
    p1_token_provider = get_brownie_provider(erc20_path, "ERC20.sol", token_address, p1_address)
    p2_token_provider = get_brownie_provider(erc20_path, "ERC20.sol", token_address, p2_address)

    token_name = token_provider.name()
    token_mint_amount = w3.toWei(tokens[0]["initial-mint"], 'kwei')

    lobby_path = os.path.join(build_path, "chess", "core", "build", "contracts", "ChessLobby.json")
    p1_lobby_provider = get_brownie_provider(lobby_path, "ChessLobby.sol", lobby_address, p1_address)
    p2_lobby_provider = get_brownie_provider(lobby_path, "ChessLobby.sol", lobby_address, p2_address)

    p1_token_amount = w3.toWei(players[0]['initial-token'], 'kwei')
    p1_deposit_amount = w3.toWei(1, 'kwei')
    p2_token_amount = w3.toWei(players[1]['initial-token'], 'kwei')
    p2_deposit_amount = w3.toWei(1, 'kwei')

    p1_game_options = 0
    p2_game_options = 0

    ###############################################################################
    # Minting tokens
    ###############################################################################
    try:
        lsection("[HOUSE calls chessToken.mint()]", 1)
        lprint("Minting " + str(token_mint_amount) + "  of " + token_name + " for: " + str(house_address))
        mint_tx = token_provider.mint(house_address, token_mint_amount)
        lprint(f"[EVENT] ChessToken.Transfer: {json.dumps(dict(mint_tx.events['Transfer']), indent=4)}")
    except Exception as ex:
        lprint("Exception in sending token.mint")
        lexcept(ex, True)
    ###############################################################################
    # transferring initial tokens to players
    ################################################################################
    try:
        lsection("[HOUSE calls chessToken.transfer(PLAYER1)]", 1)
        p1_tr_tx = token_provider.transfer(p1_address, p1_token_amount)
        lprint(f"[EVENT] ChessToken.Transfer: {json.dumps(dict(p1_tr_tx.events['Transfer']), indent=4)}")
    except Exception as ex:
        lprint(f"Exception in sending token.transfer({p1_address},{p1_token_amount})")
        lexcept(ex, True)

    try:
        lsection("[HOUSE calls chessToken.transfer(PLAYER2)]", 1)
        p2_tr_tx = token_provider.transfer(p2_address, p2_token_amount)
        lprint(f"[EVENT] ChessToken.Transfer: {json.dumps(dict(p2_tr_tx.events['Transfer']), indent=4)}")
    except Exception as ex:
        lprint(f"Exception in sending token.transfer({p2_address},{p2_token_amount})")
        lexcept(ex, True)

    # ###############################################################################
    #  player1 sends approve and deposits
    # ################################################################################
    try:
        lsection("[PLAYER1 calls token.approve(LOBBY, amount)]",1)
        p1_ap_tx = p1_token_provider.approve(lobby_address, p1_deposit_amount)
        lprint(f"[EVENT] ChessToken.Approval: {json.dumps(dict(p1_ap_tx.events['Approval']), indent=4)}")
    except Exception as ex:
        lprint(f"Exception in sending token.approve({p1_address},{p1_token_amount})")
        lexcept(ex, True)

    try:
        lsection("[PLAYER1 calls lobby.deposit(amount)]", 1)
        p1_dp_tx = p1_lobby_provider.deposit(p1_deposit_amount)
        lprint(f"[EVENT] ChessLobby.PlayerDeposited: {json.dumps(dict(p1_dp_tx.events['PlayerDeposited']), indent=4)}")
    except Exception as ex:
        lprint(f"Exception in sending lobby({p1_deposit_amount})")
        lexcept(ex, True)

    # ###############################################################################
    #  player2 sends approve and deposits
    # ################################################################################
    try:
        lsection("[PLAYER2 calls token.approve(LOBBY, amount)]",1)
        p2_ap_tx = p2_token_provider.approve(lobby_address, p2_deposit_amount)
        lprint(f"[EVENT] ChessToken.Approval: {json.dumps(dict(p2_ap_tx.events['Approval']), indent=4)}")
    except Exception as ex:
        lprint(f"Exception in sending token.approve({p2_address},{p2_token_amount})")
        lexcept(ex, True)

    try:
        lsection("[PLAYER2 calls lobby.deposit(amount)]", 1)
        p2_dp_tx = p2_lobby_provider.deposit(p2_deposit_amount)
        lprint(f"[EVENT] ChessLobby.PlayerDeposited: {json.dumps(dict(p2_dp_tx.events['PlayerDeposited']), indent=4)}")
    except Exception as ex:
        lprint(f"Exception in sending lobby.deposit({p2_deposit_amount})")
        lexcept(ex, True)
    ###############################################################################
    # Sitting with player1 and player2
    ################################################################################
    try:
        lsection("[PLAYER1 calls lobby.sitAndWait()]", 1)
        p1_sw_tx = p1_lobby_provider.sitAndWait(p1_game_options)
        lprint(f"[EVENT] ChessLobby.PlayerSit: {json.dumps(dict(p1_sw_tx.events['PlayerSit']), indent=4)}")
    except Exception as ex:
        lprint(f"Exception in sending lobby.sitAndWait() by {p1_address}")
        lexcept(ex, True)

    # ################################################################################
    table_address = None
    try:
        lsection("[PLAYER2 calls lobby.sitAndWait()]", 1)
        p2_sw_tx = p2_lobby_provider.sitAndWait(p2_game_options)
        lprint(f"[EVENT] ChessLobby.PlayerSit: {json.dumps(dict(p2_sw_tx.events['PlayerSit']), indent=4)}")
        init_event = dict(p2_sw_tx.events['TableInitialized'])
        table_address = init_event["table"]
        lprint(f"[EVENT] ChessLobby.TableInitialized: {json.dumps(init_event, indent=4)}")
    except Exception as ex:
        lprint(f"Exception in sending lobby.sitAndWait() by {p2_address}")
        lexcept(ex, True)

    return table_address
    # ################################################################################

def s3_simulate_reverts():
    print("Not implemented")
    ###############################################################################
    # player2 sends e5 -> [REVERT EXPECTED]
    ################################################################################
    # try:
    #     lsection("[PLAYER2 sends e5]", 1)
    #     p2_il_tx = p2_table_provider.move( PIECE_IDS['B_P_E'], 0x02);
    #     lprint(f"[EVENT] ChessTable.PlayerMoved: {json.dumps(dict(p2_il_tx.events['PlayerMoved']), indent=4)}")
    # except Exception as ex:
    #     lprint(f"Exception in sending move() by {p2_address}")
    #     lexcept(ex, True)

    ###############################################################################
    # player1 sends move for player2's piece -> [REVERT EXPECTED]
    ################################################################################

    ###############################################################################
    # player1 sends illegal move for her own piece -> [REVERT EXPECTED]
    ################################################################################
#*******************************************************************************
def s3_simulate_gameplay(root_path, network, table_address):
    build_path = os.path.join(root_path, "build")

    w3, chain_id, accounts = load_web3_environment(network)

    p1_address = accounts[1]['address']
    p1_private = accounts[1]['private']

    p2_address = accounts[2]['address']
    p2_private = accounts[2]['private']

    table_path = os.path.join(build_path, "chess", "core", "build", "contracts", "ChessTable.json")
    p1_table_provider = get_brownie_provider(table_path, "ChessTable.sol", table_address, p1_address)
    p2_table_provider = get_brownie_provider(table_path, "ChessTable.sol", table_address, p2_address)
    try:
        lsection("[PLAYER1 reads the pieces]", 1)
        pieces = p1_table_provider.pieces()
        pieces, view = parse_board(pieces)
        white_address = p1_table_provider.white()
        black_address = p1_table_provider.black()
        lprint(f"pieces value: {pieces}")
        lprint(f"parsed pieces:{pieces}")
        lprint(f"White:{white_address}")
        lprint(f"Black:{black_address}")
        print_board(view)
    except Exception as ex:
        lprint(f"Exception in reading public variables by {p1_address}")
        lexcept(ex, True)

    white_provider = get_brownie_provider(table_path, "ChessTable.sol", table_address, white_address)
    black_provider = get_brownie_provider(table_path, "ChessTable.sol", table_address, black_address)

    ###############################################################################
    # A simple match
    ################################################################################
    
    send_move_and_read("WHITE", white_address, white_provider, PIECE_IDS['W_P_E'], square_id('E4'))
    send_move_and_read("BLACK", black_address, black_provider, PIECE_IDS['B_P_E'], square_id('E5'))

    send_move_and_read("WHITE", white_address, white_provider, PIECE_IDS['W_Q'], square_id('H5'))
    send_move_and_read("BLACK", black_address, black_provider, PIECE_IDS['B_P_A'], square_id('A6'))

    send_move_and_read("WHITE", white_address, white_provider, PIECE_IDS['W_B_F'], square_id('C4'))
    send_move_and_read("BLACK", black_address, black_provider, PIECE_IDS['B_N_B'], square_id('C6'))

    send_move_and_read("WHITE", white_address, white_provider, PIECE_IDS['W_Q'], square_id('F7'))

    # send_move_and_read("BLACK", black_address, black_provider, PIECE_IDS['B_P_B'], square_id('B6'))
    # send_move_and_read("BLACK", black_address, black_provider, PIECE_IDS['B_P_A'], square_id('A5'))
    # send_move_and_read("BLACK", black_address, black_provider, PIECE_IDS['B_K'], square_id('E7'))

# python test_pychess.py -c move -p W_Q -s H5
# python test_pychess.py -c move -p B_P_A -s A6

# python test_pychess.py -c move -p W_B_F -s C4
# python test_pychess.py -c move -p B_P_B -s B6

# # checkmate
# python test_pychess.py -c move -p W_Q -s F7

# # checking post checkmate move
# python test_pychess.py -c move -p B_P_A -s A5
# python test_pychess.py -c move -p B_K -s E7


#*******************************************************************************
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

    table_address = s3_simulate_game_initialization(root_path, conf["network"], receipts, conf["tokens"], conf["chess"]["players"])
    s3_simulate_gameplay(root_path, conf["network"], table_address)

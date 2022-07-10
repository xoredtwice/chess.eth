#!/bin/bash

python test_pychess.py -c reset

python test_pychess.py -c move -p W_P_E -s E4
python test_pychess.py -c move -p B_P_E -s E5

python test_pychess.py -c move -p W_Q -s H5
python test_pychess.py -c move -p B_P_A -s A6

python test_pychess.py -c move -p W_B_F -s C4
python test_pychess.py -c move -p B_P_B -s B6

# checkmate
python test_pychess.py -c move -p W_Q -s F7

# checking post checkmate move
python test_pychess.py -c move -p B_P_A -s A5
python test_pychess.py -c move -p B_K -s E7


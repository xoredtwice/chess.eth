#!/bin/bash

python test_pychess.py -c clear

python test_pychess.py -c move -p W_R_A -s A1

python test_pychess.py -c move -p W_P_A -s A2

python test_pychess.py -c move -p B_R_A -s A8

python test_pychess.py -c move -p B_P_A -s A7

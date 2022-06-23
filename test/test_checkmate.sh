#!/bin/bash

python test_pychess.py -c clear

python test_pychess.py -c move -p B_K -s B8

python test_pychess.py -c move -p W_K -s B1
python test_pychess.py -c move -p W_P_A -s A2
python test_pychess.py -c move -p W_P_B -s B2
python test_pychess.py -c move -p W_P_C -s C2


python test_pychess.py -c move -p B_R_A -s F8
python test_pychess.py -c move -p B_R_A -s F1


python test_pychess.py -c move -p W_P_A -s A3


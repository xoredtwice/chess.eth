# chess.eth
Chess Game on Ethereum Layer 2 (in progress)

Steps:
--------
+ [x] Create an offline Ethereum-Python test environment.
+ [x] Design an efiicient Chess engine based on EVM machine.
+ [x] Develop and test Chess gameplay in Python.
+ [ ] Final Tests on the gameplay over solidity (Layer 1).
+ [ ] Add Layer 2 Compatibility.
+ [ ] Security Audit.
+ [ ] Efficiency Improvements.
+ [ ] GUI.

How to run:
--------
+ Install Python3, Pip3 and Ganache

+ Create and enable a Python3 virtual environment

```
        python3 -m venv <ENV-NAME>
        source <ENV-NAME>/bin/activate
```

+ Install Brownie and PyQt5

```
        pip install eth-brownie
        pip install pyqt5
```

+ Run some tests over pychess core.

```
        ./test/set_board.sh
```


```
        ./test/test_checkmate.sh
```

+ Run the whole scenario (preparation of the project folder, compile, deploy, simulate and play) by
```
        python run_chess.py
```


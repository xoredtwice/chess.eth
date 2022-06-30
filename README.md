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
+ Install Python3 and Pip3

+ Create and enable a Python3 virtual environment

```
        python3 -m venv <ENV-NAME>
        source <ENV-NAME>/bin/activate
```
+ Install Brownie

```
        pip install eth-brownie
```

+ Run some tests over pychess core.

```
        ./test/set_board.sh
```


```
        ./test/test_checkmate.sh
```

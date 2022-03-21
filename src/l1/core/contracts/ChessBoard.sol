// SPDX-License-Identifier: GPL3
pragma solidity ^0.8;

import './libraries/SafeMath.sol';
import '../interfaces/IERC20.sol';
import '../interfaces/IChessBoard.sol';

contract ChessBoard is IChessBoard{
    using SafeMath  for uint;

    string public name;
    address public lobby;
    address public player1;
    address public player2;
    
    uint public activeGame;
    uint8 public lastMove;
    uint8 public gameState;

    uint private unlocked = 1;

    modifier lock() {
        require(unlocked == 1, 'ChessBoard: LOCKED');
        unlocked = 0;
        _;
        unlocked = 1;
    }

    constructor() public {
        lobby = msg.sender;
        name = "gary";
    }

    // called once by the factory at time of deployment
    function initialize(address _player1, address _player2) external {
        require(msg.sender == lobby, 'ChessBoard: IDENTICAL_PLAYERS'); // sufficient check
        player1 = _player1;
        player2 = _player2;
    }

    function _move(address player, uint8 newMove) private{

    }

    function move(uint8 newMove) external returns (bool) {
        _move(msg.sender, newMove);
        return true;
    }


}
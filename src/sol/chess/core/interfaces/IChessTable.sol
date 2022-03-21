// SPDX-License-Identifier: GPL3
pragma solidity ^0.8;

interface IChessTable {

    function name() external view returns (string memory);
    function lobby() external view returns (address);
    function player1() external view returns (address);
    function player2() external view returns (address);

    function state() external view returns (uint8);
    // function board() external view returns(uint8[8][8] memory);
    function activeGame() external view returns (uint);
    function lastMove() external view returns (uint8);

    event PlayerMoved(address indexed player, uint8 move, uint8 stateUpdates);
    event GameStarted(address indexed player1, address indexed player2, uint meta);
    event GameEnded(uint result);

    function initialize(address, address) external;
    function move(uint8 move) external returns (bool);
}
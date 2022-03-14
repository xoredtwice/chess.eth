// SPDX-License-Identifier: GPL3
pragma solidity ^0.8;

interface IChessBoard {

    function name() external view returns (string memory);

    function gameState() external view returns (uint8);

    event PlayerMoved(address indexed player, uint8 move, uint8 stateUpdates);
    event GameStarted(address indexed player1, address indexed player2, uint options);
    event PlayerWon(address indexed player, uint conclusion);

    function lobby() external view returns (address);
    function player1() external view returns (address);
    function player2() external view returns (address);
    function activeGame() external view returns (uint);
    function lastMove() external view returns (uint8);

    function move(uint8 move) external returns (bool);

    function initialize(address, address) external;
}
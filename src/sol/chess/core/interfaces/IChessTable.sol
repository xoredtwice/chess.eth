// SPDX-License-Identifier: GPL3
pragma solidity ^0.8;

interface IChessTable {

    function name() external view returns (string memory);
    function lobby() external view returns (address);
    function white() external view returns (address);
    function black() external view returns (address);
    function turn() external view returns (address);
    function pieces() external view returns(uint256);

    function board64W() external view returns(uint64);
    function board64B() external view returns(uint64);

    function getVisibility(uint8 piece) external view returns(uint64);

    function state() external view returns (uint8);
    function activeGame() external view returns (uint);
    function lastMove() external view returns (uint16);

    event PlayerMoved(address indexed player, uint8 piece, uint8 action);
    event GameStarted(address indexed white, address indexed black, uint8 meta);
    event GameEnded(bool isDraw, address indexed winner, address indexed log);

    function initialize(address player1, address player2, uint8 meta) external returns (bool);
    function move(uint8 piece, uint8 action) external returns (bool);
}
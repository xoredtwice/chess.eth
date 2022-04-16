// SPDX-License-Identifier: GPL3
pragma solidity ^0.8;

interface IChessTable {

    function name() external view returns (string memory);
    function lobby() external view returns (address);
    function white() external view returns (address);
    function black() external view returns (address);
    function turn() external view returns (address);
    function board() external view returns(uint256);

    function state() external view returns (uint8);
    function activeGame() external view returns (uint);
    function lastMove() external view returns (uint16);

    event PlayerMoved(address indexed player, uint16 move, uint8 state);
    event GameStarted(address indexed white, address indexed black, uint8 meta);
    event GameEnded(bool isDraw, address indexed winner, address indexed log);

    function initialize(address, address, uint8) external returns (bool);
    function move(uint8 piece, uint8 action) external returns (bool);
}
pragma solidity ^0.8;

interface IChessBoard {

    function name() external pure returns (string memory);
    
    function DOMAIN_SEPARATOR() external view returns (bytes32);

    function gameState() external view returns (uint);

    event PlayerMoved(address indexed player, uint8 move, uint8 stateUpdates);
    event GameStarted(address indexed player1, address indexed player2, uint options);
    event PlayerWon(address indexed player, uint conclusion);

    function lobby() external view returns (address);
    function player1() external view returns (address);
    function player2() external view returns (address);
    function activeGame() external pure returns (uint8);
    function lastMove() external pure returns (uint8);

    function move(uint8 move) external returns (bool);

    function initialize(address, address) external;
}
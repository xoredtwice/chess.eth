pragma solidity ^0.8;

import './libraries/Math.sol';
import './libraries/UQ112x112.sol';
import '../interfaces/IERC20.sol';
import '../interfaces/IChessBoard.sol';

contract ChessBoard is IChessBoard{
    using SafeMath  for uint;
    using UQ112x112 for uint224;

    uint public constant MINIMUM_LIQUIDITY = 10**3;
    bytes4 private constant SELECTOR = bytes4(keccak256(bytes('transfer(address,uint256)')));

    address public lobby;
    address public player1;
    address public player2;

    uint32  private blockTimestampLast; // uses single storage slot, accessible via getReserves

    uint private unlocked = 1;
    modifier lock() {
        require(unlocked == 1, 'ChessBoard: LOCKED');
        unlocked = 0;
        _;
        unlocked = 1;
    }

    constructor() public {
        lobby = msg.sender;
        factoryName = "";
    }

    // called once by the factory at time of deployment
    function initialize(address _player1, address _player2) external {
        require(msg.sender == lobby, 'ChessBoard: FORBIDDEN'); // sufficient check
        player1 = _player1;
        player2 = _player2;
    }

    function _move(address player, uint8 move) private{

    }

    function move(uint8 newMove) external lock returns (bool) {
        _move(msg.sender, newMove);
        return true;
    }


}
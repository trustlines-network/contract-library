pragma solidity ^0.4.25;

/**
 * The sole purpose of this file is to be able to test the internal functions
 * of the ECDSA library contract.
 */

import "./ECDSA.sol";


contract TestECDSA {

    constructor() public {}

    function() external {}

    function testRecover(bytes32 _hash, bytes _signature) public returns (address) {
        return ECDSA.recover(_hash, _signature);
    }

    function testToEthSignedMessageHash(bytes32 _hash) public returns (bytes32) {
        return ECDSA.toEthSignedMessageHash(_hash);
    }
}

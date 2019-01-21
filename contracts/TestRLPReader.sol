pragma solidity ^0.4.25;

/**
 * The sole purpose of this file is to be able to test the internal functions
 * of the RLPReader library contract.
 */

import "./RLPReader.sol";


contract TestRLPReader {

    constructor() public {}

    function() external {}

    function testToRlpItem(bytes _rlpEncodedItem)
        public
        pure
        returns (uint length, uint memPtr)
    {
        RLPReader.RLPItem memory rlpItem = RLPReader.toRlpItem(_rlpEncodedItem);
        return (rlpItem.len, rlpItem.memPtr);
    }

    function testIsList(bytes _rlpEncodedItem)
        public
        pure
        returns (bool)
    {
        RLPReader.RLPItem memory rlpItem = RLPReader.toRlpItem(_rlpEncodedItem);
        return RLPReader.isList(rlpItem);
    }

    function testNumItems(bytes _rlpEncodedItem)
        public
        pure
        returns (uint)
    {
        RLPReader.RLPItem memory rlpItem = RLPReader.toRlpItem(_rlpEncodedItem);
        return RLPReader.numItems(rlpItem); 
    }

    function testItemLength(bytes _rlpEncodedItem)
        public
        pure
        returns (uint)
    {
        RLPReader.RLPItem memory rlpItem = RLPReader.toRlpItem(_rlpEncodedItem);
        return RLPReader._itemLength(rlpItem.memPtr);
    }

    function testToBoolean(bytes _rlpEncodedItem)
        public
        pure
        returns (bool)
    {
        RLPReader.RLPItem memory rlpItem = RLPReader.toRlpItem(_rlpEncodedItem);
        return RLPReader.toBoolean(rlpItem);
    }

    function testToBytes(bytes _rlpEncodedItem)
        public
        pure
        returns (bytes)
    {
        RLPReader.RLPItem memory rlpItem = RLPReader.toRlpItem(_rlpEncodedItem);
        return RLPReader.toBytes(rlpItem);
    }

    function testToAddress(bytes _rlpEncodedItem)
        public
        pure
        returns (address)
    {
        RLPReader.RLPItem memory rlpItem = RLPReader.toRlpItem(_rlpEncodedItem);
        return RLPReader.toAddress(rlpItem);
    }

    function testToUint(bytes _rlpEncodedItem)
        public
        pure
        returns (uint)
    {
        RLPReader.RLPItem memory rlpItem = RLPReader.toRlpItem(_rlpEncodedItem);
        return RLPReader.toUint(rlpItem);
    }
}

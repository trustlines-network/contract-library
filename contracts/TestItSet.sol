pragma solidity ^0.4.25;

/**
 * The sole purpose of this file is to be able to test the internal functions of the ItSet
 */

import "./it_set_lib.sol";


contract TestItSet {

    ItSet.AddressSet addressSet;

    constructor() public {}

    function() external {}

    function testInsert(address _addressToInsert) public {
        return ItSet.insert(TestItSet.addressSet, _addressToInsert);
    }

    function testContains(address _addressToTest) public view returns (bool) {
        return ItSet.contains(TestItSet.addressSet, _addressToTest);
    }

    function testRemove(address _addressToRemove) public {
        return ItSet.remove(TestItSet.addressSet, _addressToRemove);
    }

    function testSize() public view returns (uint) {
        return ItSet.size(TestItSet.addressSet);
    }
}

#! pytest

import rlp
from web3 import Web3


def test_int_to_rlp_item(test_rlp_reader_contract):
    """test conversion function from integer to RLPItem"""
    contract = test_rlp_reader_contract
    rlp_encoded_item = rlp.encode(1)
    rlp_item_from_contract = contract.functions.testToRlpItem(rlp_encoded_item).call()

    assert rlp_item_from_contract[0] == 1


def test_string_to_rlp_item(test_rlp_reader_contract):
    """test conversion function from string to RLPItem"""
    contract = test_rlp_reader_contract
    rlp_encoded_item = rlp.encode('dog')
    rlp_item_from_contract = contract.functions.testToRlpItem(rlp_encoded_item).call()

    assert rlp_item_from_contract[0] == 4


def test_list_to_rlp_item(test_rlp_reader_contract):
    """test conversion function from list to RLPItem"""
    contract = test_rlp_reader_contract
    rlp_encoded_item = rlp.encode(['cat', 'dog'])
    rlp_item_from_contract = contract.functions.testToRlpItem(rlp_encoded_item).call()

    assert rlp_item_from_contract[0] == 9


def test_is_list_true(test_rlp_reader_contract):
    """test if rlp encoded item is list"""
    contract = test_rlp_reader_contract
    rlp_encoded_item = rlp.encode([1, 2, 3])

    assert contract.functions.testIsList(rlp_encoded_item).call() is True


def test_is_list_false(test_rlp_reader_contract):
    """test if rlp encoded item is not a list"""
    contract = test_rlp_reader_contract
    rlp_encoded_item = rlp.encode(1)

    assert contract.functions.testIsList(rlp_encoded_item).call() is False


def test_num_items(test_rlp_reader_contract):
    """test if number of items in rlp encoded list is 3"""
    contract = test_rlp_reader_contract
    rlp_encoded_item = rlp.encode([1, 2, 3])

    assert contract.functions.testNumItems(rlp_encoded_item).call() == 3


def test_num_items_single(test_rlp_reader_contract):
    """test if number of items in rlp encoded item is 1"""
    contract = test_rlp_reader_contract
    rlp_encoded_item = rlp.encode(1)

    assert contract.functions.testNumItems(rlp_encoded_item).call() == 1


def test_num_items_nested(test_rlp_reader_contract):
    """test if number of items in nested rlp encoded item is 2"""
    contract = test_rlp_reader_contract
    rlp_encoded_item = rlp.encode([[1, 2], 3])

    assert contract.functions.testNumItems(rlp_encoded_item).call() == 2


def test_int_item_length(test_rlp_reader_contract):
    """test item length of integer 1"""
    contract = test_rlp_reader_contract
    rlp_encoded_item = rlp.encode(1)

    assert contract.functions.testItemLength(rlp_encoded_item).call() == 1


def test_long_int_item_length(test_rlp_reader_contract):
    """test item length of integer 1024"""
    contract = test_rlp_reader_contract
    rlp_encoded_item = rlp.encode(1024)

    assert contract.functions.testItemLength(rlp_encoded_item).call() == 3


def test_string_item_length(test_rlp_reader_contract):
    """test item length of string"""
    contract = test_rlp_reader_contract
    rlp_encoded_item = rlp.encode('dog')

    assert contract.functions.testItemLength(rlp_encoded_item).call() == 4


def test_to_bytes(test_rlp_reader_contract):
    """test conversion function to bytes"""
    contract = test_rlp_reader_contract
    str_to_encode = 'dog'
    rlp_encoded_item = rlp.encode(str_to_encode)

    assert contract.functions.testToBytes(rlp_encoded_item).call() == Web3.toBytes(text=str_to_encode)


def test_to_boolean(test_rlp_reader_contract):
    """test conversion function to boolean"""
    contract = test_rlp_reader_contract
    bool_as_num = 1
    rlp_encoded_item = rlp.encode(bool_as_num)

    assert contract.functions.testToBoolean(rlp_encoded_item).call() is True


def test_to_uint(test_rlp_reader_contract):
    """test conversion function to uint"""
    contract = test_rlp_reader_contract
    num = 128  # larger than a byte
    rlp_encoded_item = rlp.encode(num)

    assert contract.functions.testToUint(rlp_encoded_item).call() == num


def test_to_address(test_rlp_reader_contract):
    """test conversion function to address"""
    contract = test_rlp_reader_contract
    zero_address = '0x0000000000000000000000000000000000000000'
    rlp_encoded_item = rlp.encode(Web3.toBytes(hexstr='0x0'))

    assert contract.functions.testToAddress(rlp_encoded_item).call() == zero_address

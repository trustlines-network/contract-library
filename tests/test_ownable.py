#! pytest

import pytest
import eth_tester.exceptions


def test_owner(ownable_contract, accounts):
    """test if ownable contract has correct owner"""
    contract = ownable_contract

    assert contract.functions.owner().call() == accounts[0]


def test_transfer_ownership_from_owner(ownable_contract, accounts, web3):
    """test if owner changes after transfer of ownership"""
    contract = ownable_contract
    new_owner = accounts[1]
    tx_hash = contract.functions.transferOwnership(new_owner).transact({"from": accounts[0]})
    tx_receipt = web3.eth.getTransactionReceipt(tx_hash)

    assert tx_receipt is not None
    assert contract.functions.owner().call() == new_owner


def test_transfer_ownership_from_other(ownable_contract, accounts):
    """test if transaction fails for ownership transfer"""
    contract = ownable_contract
    other_account = accounts[1]

    with pytest.raises(eth_tester.exceptions.TransactionFailed):
        contract.functions.transferOwnership(other_account).transact({"from": other_account})

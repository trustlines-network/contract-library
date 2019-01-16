#! pytest

import pytest
import eth_tester.exceptions
import web3.exceptions as web3_exceptions


def test_destruct(destructable_contract, accounts, web3):
    """test if contract can be destructed by owner"""
    contract = destructable_contract

    assert contract.functions.owner().call() == accounts[0]

    tx_hash = contract.functions.destruct().transact({"from": accounts[0]})
    tx_receipt = web3.eth.getTransactionReceipt(tx_hash)

    assert tx_receipt is not None

    """web3 raises BadFunctionCallOutput when it can not transact with contract"""
    with pytest.raises(web3_exceptions.BadFunctionCallOutput):
        contract.functions.owner().call()


def test_destruct_not_owner(destructable_contract, accounts, web3):
    """test onlyOwner modifier for destruct"""
    contract = destructable_contract
    other_account = accounts[1]

    with pytest.raises(eth_tester.exceptions.TransactionFailed):
        contract.functions.destruct().transact({"from": other_account})

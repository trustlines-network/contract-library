#! pytest

import pytest
import eth_tester.exceptions


def test_add_authorized_address(authorizable_contract, accounts, web3):
    """test if address can be added by owner"""
    contract = authorizable_contract
    account_to_authorize = accounts[1]

    assert contract.functions.authorized(account_to_authorize).call() is False

    tx_hash = contract.functions.addAuthorizedAddress(account_to_authorize).transact({"from": accounts[0]})
    tx_receipt = web3.eth.getTransactionReceipt(tx_hash)

    assert tx_receipt is not None
    assert contract.functions.authorized(account_to_authorize).call() is True


def test_add_authorized_address_not_owner(authorizable_contract, accounts, web3):
    """test onlyOwner modifier for addAuthorizedAddress"""
    contract = authorizable_contract
    other_account = accounts[1]

    with pytest.raises(eth_tester.exceptions.TransactionFailed):
        contract.functions.addAuthorizedAddress(other_account).transact({"from": other_account})


def test_add_already_authorized_address(authorizable_contract_with_addresses,
                                        accounts,
                                        web3):
    """test targetNotAuthorized modifier for addAuthorizedAddress"""
    contract = authorizable_contract_with_addresses

    with pytest.raises(eth_tester.exceptions.TransactionFailed):
        contract.functions.addAuthorizedAddress(accounts[0]).transact({"from": accounts[0]})


def test_remove_authorized_address(authorizable_contract_with_addresses,
                                   accounts,
                                   web3):
    """test if owner can remove an authorized address"""
    contract = authorizable_contract_with_addresses
    account_to_remove = accounts[1]
    tx_hash = contract.functions.removeAuthorizedAddress(account_to_remove).transact({"from": accounts[0]})
    tx_receipt = web3.eth.getTransactionReceipt(tx_hash)

    assert tx_receipt is not None
    assert contract.functions.authorized(account_to_remove).call() is False


def test_remove_authorized_address_not_owner(authorizable_contract_with_addresses,
                                             accounts,
                                             web3):
    """test onlyOwner modifier for removeAuthorizedAddress"""
    contract = authorizable_contract_with_addresses
    other_account = accounts[1]

    with pytest.raises(eth_tester.exceptions.TransactionFailed):
        contract.functions.removeAuthorizedAddress(other_account).transact({"from": other_account})


def test_remove_not_authorized_address(authorizable_contract_with_addresses,
                                       accounts,
                                       web3):
    """test targetAuthorized modifier for removeAuthorizedAddress"""
    contract = authorizable_contract_with_addresses
    account_to_remove = accounts[3]

    with pytest.raises(eth_tester.exceptions.TransactionFailed):
        contract.functions.removeAuthorizedAddress(account_to_remove).transact({"from": accounts[0]})

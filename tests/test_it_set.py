#! pytest


def test_insert(test_it_set_contract, accounts, web3):
    contract = test_it_set_contract
    tx_hash = contract.functions.testInsert(accounts[0]).transact({"from": accounts[0]})
    tx_receipt = web3.eth.getTransactionReceipt(tx_hash)

    assert tx_receipt is not None


def test_contains(test_it_set_contract_with_addresses, accounts):
    contract = test_it_set_contract_with_addresses

    assert contract.functions.testContains(accounts[0]).call() is True
    assert contract.functions.testContains(accounts[4]).call() is False


def test_remove(test_it_set_contract_with_addresses, accounts, web3):
    contract = test_it_set_contract_with_addresses

    tx_hash = contract.functions.testRemove(accounts[0]).transact({"from": accounts[0]})
    tx_receipt = web3.eth.getTransactionReceipt(tx_hash)

    assert tx_receipt is not None
    assert contract.functions.testContains(accounts[0]).call() is False


def test_size_initial(test_it_set_contract):
    contract = test_it_set_contract

    assert contract.functions.testSize().call() == 0


def test_size_2_addresses(test_it_set_contract_with_addresses):
    contract = test_it_set_contract_with_addresses

    assert contract.functions.testSize().call() == 2

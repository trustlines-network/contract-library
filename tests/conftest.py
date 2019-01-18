import pytest
import eth_tester
import eth_tester.backends.pyevm.main
from collections import namedtuple
from web3 import Web3
from web3.providers.eth_tester import EthereumTesterProvider
from eth_utils import to_checksum_address

from .deploy_util import (deploy_ownable,
                          deploy_authorizable,
                          deploy_destructable,
                          deploy_test_it_set,
                          deploy_test_ecdsa,)


SignedBlockHeader = namedtuple('SignedBlockHeader', 'unsignedBlockHeader signature')


@pytest.fixture(scope="session")
def ethereum_tester():
    tester = eth_tester.EthereumTester(eth_tester.PyEVMBackend())
    return tester


@pytest.fixture(autouse=True)
def blockchain_cleanup(ethereum_tester):
    snapshot = ethereum_tester.take_snapshot()
    yield
    ethereum_tester.revert_to_snapshot(snapshot)


@pytest.fixture(scope="session")
def web3(ethereum_tester):
    web3 = Web3(EthereumTesterProvider(ethereum_tester))
    web3.eth.defaultAccount = web3.eth.accounts[0]
    return web3


@pytest.fixture(scope="session")
def accounts(web3):
    accounts = web3.personal.listAccounts[0:5]
    assert len(accounts) == 5
    return [to_checksum_address(account) for account in accounts]


@pytest.fixture()
def ownable_contract(web3):
    return deploy_ownable(web3)


@pytest.fixture()
def authorizable_contract(web3):
    return deploy_authorizable(web3)


@pytest.fixture()
def authorizable_contract_with_addresses(accounts, web3):
    contract = deploy_authorizable(web3)
    contract.functions.addAuthorizedAddress(accounts[1]).transact({"from": accounts[0]})
    contract.functions.addAuthorizedAddress(accounts[2]).transact({"from": accounts[0]})
    return contract


@pytest.fixture()
def destructable_contract(web3):
    return deploy_destructable(web3)


@pytest.fixture()
def test_it_set_contract(web3):
    return deploy_test_it_set(web3)


@pytest.fixture()
def test_it_set_contract_with_addresses(accounts, web3):
    contract = deploy_test_it_set(web3)
    contract.functions.testInsert(accounts[0]).transact({"from": accounts[0]})
    contract.functions.testInsert(accounts[1]).transact({"from": accounts[0]})
    return contract


@pytest.fixture()
def test_ecdsa_contract(web3):
    return deploy_test_ecdsa(web3)

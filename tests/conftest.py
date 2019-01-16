import pytest
import eth_tester
import eth_tester.backends.pyevm.main
from collections import namedtuple
from web3 import Web3
from web3.providers.eth_tester import EthereumTesterProvider
from eth_utils import to_checksum_address

from .deploy_util import (deploy_ownable)


RELEASE_BLOCK_NUMBER_OFFSET = 50

# Fix the indexes used to get addresses from the test chain.
# Mind the difference between count and index.
HONEST_VALIDATOR_COUNT = 2
MALICIOUS_VALIDATOR_INDEX = HONEST_VALIDATOR_COUNT
MALICIOUS_NON_VALIDATOR_INDEX = MALICIOUS_VALIDATOR_INDEX + 1


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


@pytest.fixture(scope="session")
def ownable_contract_session(web3):
    return deploy_ownable(web3)


@pytest.fixture
def ownable_contract(web3):
    return deploy_ownable(web3)

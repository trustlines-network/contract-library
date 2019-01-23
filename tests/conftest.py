import pytest
from collections import namedtuple


SignedBlockHeader = namedtuple('SignedBlockHeader', 'unsignedBlockHeader signature')


@pytest.fixture(scope="session")
def ownable_contract(deploy_contract):
    return deploy_contract("Ownable")


@pytest.fixture(scope="session")
def authorizable_contract(deploy_contract):
    return deploy_contract("Authorizable")


@pytest.fixture(scope="session")
def authorizable_contract_with_addresses(accounts, deploy_contract):
    contract = deploy_contract("Authorizable")
    contract.functions.addAuthorizedAddress(accounts[0]).transact({"from": accounts[0]})
    contract.functions.addAuthorizedAddress(accounts[1]).transact({"from": accounts[0]})
    return contract


@pytest.fixture(scope="session")
def destructable_contract(deploy_contract):
    return deploy_contract("Destructable")


@pytest.fixture(scope="session")
def test_it_set_contract(deploy_contract):
    return deploy_contract("TestItSet")


@pytest.fixture(scope="session")
def test_it_set_contract_with_addresses(accounts, deploy_contract):
    contract = deploy_contract("TestItSet")
    contract.functions.testInsert(accounts[0]).transact({"from": accounts[0]})
    contract.functions.testInsert(accounts[1]).transact({"from": accounts[0]})
    return contract


@pytest.fixture(scope="session")
def test_ecdsa_contract(deploy_contract):
    return deploy_contract("TestECDSA")


@pytest.fixture(scope="session")
def test_rlp_reader_contract(deploy_contract):
    return deploy_contract("TestRLPReader")

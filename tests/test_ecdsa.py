#! pytest

from web3 import Web3

"""
NOTE Tests are ported from OpenZeppelin
(https://github.com/OpenZeppelin/openzeppelin-solidity/blob/3e82db2f6f8b8bdc05b22fb32bc2842ea58f001d/test/cryptography/ECDSA.test.js)


The MIT License (MIT)

Copyright (c) 2016 Smart Contract Solutions, Inc.

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

TEST_MESSAGE = Web3.sha3(text='OpenZeppelin')
ZERO_ADDRESS = '0x0000000000000000000000000000000000000000'
V0_SIGNER = '0x2cc1166f6212628A0deEf2B33BEFB2187D35b86c'
V0_SIGNATURE_WITHOUT_VERSION = ('0x5d99b6f7f6d1f73d1a26497f2b1c89b24c0993913f86e9a2d02cd69887d9c94f3c880358579d811b'
                                '21dd1b7fd9bb01c1d81d10e69f0384e675c32b39643be892')
V1_SIGNER = '0x1E318623aB09Fe6de3C9b8672098464Aeda9100E'
V1_SIGNATURE_WITHOUT_VERSION = ('0x331fe75a821c982f9127538858900d87d3ec1f9f737338ad67cad133fa48feff48e6fa0c18abc62'
                                'e42820f05943e47af3e9fbe306ce74d64094bdf1691ee53e0')


def test_recover_v0_sig_with_00_version(test_ecdsa_contract):
    """test recover of v0 signature with 00 as version value"""
    contract = test_ecdsa_contract
    version = '00'
    signature_with_version = V0_SIGNATURE_WITHOUT_VERSION + version
    recovered_address = contract.functions.testRecover(TEST_MESSAGE,
                                                       Web3.toBytes(hexstr=signature_with_version)).call()

    assert recovered_address == V0_SIGNER


def test_recover_v0_sig_with_27_version(test_ecdsa_contract):
    """test recover of v0 signature with 27 as version value"""
    contract = test_ecdsa_contract
    version = '1b'  # 27 = 1b
    signature_with_version = V0_SIGNATURE_WITHOUT_VERSION + version
    recovered_address = contract.functions.testRecover(TEST_MESSAGE,
                                                       Web3.toBytes(hexstr=signature_with_version)).call()

    assert recovered_address == V0_SIGNER


def test_recover_v0_sig_with_wrong_version(test_ecdsa_contract):
    """test recover of v0 signature with wrong version value only valid version
    values are 0, 1, 27, 28"""
    contract = test_ecdsa_contract
    version = '02'
    signature_with_version = V0_SIGNATURE_WITHOUT_VERSION + version
    recovered_address = contract.functions.testRecover(TEST_MESSAGE,
                                                       Web3.toBytes(hexstr=signature_with_version)).call()

    assert recovered_address == ZERO_ADDRESS


def test_recover_v1_signature_01_version(test_ecdsa_contract):
    """test recover of v1 signature with 01 as version value"""
    contract = test_ecdsa_contract
    version = '01'
    signature_with_version = V1_SIGNATURE_WITHOUT_VERSION + version
    recovered_address = contract.functions.testRecover(TEST_MESSAGE,
                                                       Web3.toBytes(hexstr=signature_with_version)).call()

    assert recovered_address == V1_SIGNER


def test_recover_v1_signature_28_version(test_ecdsa_contract):
    """test recover of v1 signature with 28 as version value"""
    contract = test_ecdsa_contract
    version = '1c'  # 28 = 1c
    signature_with_version = V1_SIGNATURE_WITHOUT_VERSION + version
    recovered_address = contract.functions.testRecover(TEST_MESSAGE,
                                                       Web3.toBytes(hexstr=signature_with_version)).call()

    assert recovered_address == V1_SIGNER


def test_to_eth_signed_message_hash(test_ecdsa_contract):
    """test toEthSignedMessage"""
    contract = test_ecdsa_contract
    prefix_bytes = Web3.toBytes(text='\x19Ethereum Signed Message:\n32')
    message_bytes = Web3.soliditySha3(['bytes32', 'bytes32'], [prefix_bytes, TEST_MESSAGE])

    assert contract.functions.testToEthSignedMessageHash(TEST_MESSAGE).call() == message_bytes

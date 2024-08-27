# coding: utf-8

"""
    Clerk Backend API

    The Clerk REST Backend API, meant to be accessed by backend servers.  ### Versions  When the API changes in a way that isn't compatible with older versions, a new version is released. Each version is identified by its release date, e.g. `2021-02-05`. For more information, please see [Clerk API Versions](https://clerk.com/docs/backend-requests/versioning/overview).   Please see https://clerk.com/docs for more information.

    The version of the OpenAPI document: v1
    Contact: support@clerk.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clerk_backend_sdk.models.web3_wallet import Web3Wallet

class TestWeb3Wallet(unittest.TestCase):
    """Web3Wallet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Web3Wallet:
        """Test Web3Wallet
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Web3Wallet`
        """
        model = Web3Wallet()
        if include_optional:
            return Web3Wallet(
                id = '',
                object = 'web3_wallet',
                web3_wallet = '',
                verification = clerk_backend_sdk.models.web3_wallet_verification.Web3Wallet_verification(),
                created_at = 56,
                updated_at = 56
            )
        else:
            return Web3Wallet(
                object = 'web3_wallet',
                web3_wallet = '',
                verification = clerk_backend_sdk.models.web3_wallet_verification.Web3Wallet_verification(),
                created_at = 56,
                updated_at = 56,
        )
        """

    def testWeb3Wallet(self):
        """Test Web3Wallet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

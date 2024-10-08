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

from clerk_backend_sdk.api.jwks_api import JWKSApi


class TestJWKSApi(unittest.TestCase):
    """JWKSApi unit test stubs"""

    def setUp(self) -> None:
        self.api = JWKSApi()

    def tearDown(self) -> None:
        pass

    def test_get_jwks(self) -> None:
        """Test case for get_jwks

        Retrieve the JSON Web Key Set of the instance
        """
        pass


if __name__ == '__main__':
    unittest.main()

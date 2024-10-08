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

from clerk_backend_sdk.models.revoke_invitation200_response import RevokeInvitation200Response

class TestRevokeInvitation200Response(unittest.TestCase):
    """RevokeInvitation200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RevokeInvitation200Response:
        """Test RevokeInvitation200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RevokeInvitation200Response`
        """
        model = RevokeInvitation200Response()
        if include_optional:
            return RevokeInvitation200Response(
                object = 'invitation',
                id = '',
                email_address = '',
                public_metadata = clerk_backend_sdk.models.public_metadata.public_metadata(),
                revoked = True,
                status = 'revoked',
                url = '',
                created_at = 56,
                updated_at = 56
            )
        else:
            return RevokeInvitation200Response(
                object = 'invitation',
                id = '',
                email_address = '',
                status = 'revoked',
                created_at = 56,
                updated_at = 56,
        )
        """

    def testRevokeInvitation200Response(self):
        """Test RevokeInvitation200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

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

from clerk_backend_sdk.models.update_instance_auth_config200_response import UpdateInstanceAuthConfig200Response

class TestUpdateInstanceAuthConfig200Response(unittest.TestCase):
    """UpdateInstanceAuthConfig200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateInstanceAuthConfig200Response:
        """Test UpdateInstanceAuthConfig200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateInstanceAuthConfig200Response`
        """
        model = UpdateInstanceAuthConfig200Response()
        if include_optional:
            return UpdateInstanceAuthConfig200Response(
                object = 'instance_settings',
                id = '',
                restricted_to_allowlist = True,
                from_email_address = '',
                progressive_sign_up = True,
                enhanced_email_deliverability = True
            )
        else:
            return UpdateInstanceAuthConfig200Response(
        )
        """

    def testUpdateInstanceAuthConfig200Response(self):
        """Test UpdateInstanceAuthConfig200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

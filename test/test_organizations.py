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

from clerk_backend_sdk.models.organizations import Organizations

class TestOrganizations(unittest.TestCase):
    """Organizations unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Organizations:
        """Test Organizations
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Organizations`
        """
        model = Organizations()
        if include_optional:
            return Organizations(
                data = [
                    clerk_backend_sdk.models.organization.Organization(
                        object = 'organization', 
                        id = '', 
                        name = '', 
                        slug = '', 
                        members_count = 56, 
                        max_allowed_memberships = 56, 
                        admin_delete_enabled = True, 
                        public_metadata = clerk_backend_sdk.models.public_metadata.public_metadata(), 
                        private_metadata = clerk_backend_sdk.models.private_metadata.private_metadata(), 
                        created_by = '', 
                        created_at = 56, 
                        updated_at = 56, )
                    ],
                total_count = 56
            )
        else:
            return Organizations(
                data = [
                    clerk_backend_sdk.models.organization.Organization(
                        object = 'organization', 
                        id = '', 
                        name = '', 
                        slug = '', 
                        members_count = 56, 
                        max_allowed_memberships = 56, 
                        admin_delete_enabled = True, 
                        public_metadata = clerk_backend_sdk.models.public_metadata.public_metadata(), 
                        private_metadata = clerk_backend_sdk.models.private_metadata.private_metadata(), 
                        created_by = '', 
                        created_at = 56, 
                        updated_at = 56, )
                    ],
                total_count = 56,
        )
        """

    def testOrganizations(self):
        """Test Organizations"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

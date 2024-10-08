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

from clerk_backend_sdk.api.organization_memberships_api import OrganizationMembershipsApi


class TestOrganizationMembershipsApi(unittest.TestCase):
    """OrganizationMembershipsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OrganizationMembershipsApi()

    def tearDown(self) -> None:
        pass

    def test_create_organization_membership(self) -> None:
        """Test case for create_organization_membership

        Create a new organization membership
        """
        pass

    def test_delete_organization_membership(self) -> None:
        """Test case for delete_organization_membership

        Remove a member from an organization
        """
        pass

    def test_list_organization_memberships(self) -> None:
        """Test case for list_organization_memberships

        Get a list of all members of an organization
        """
        pass

    def test_update_organization_membership(self) -> None:
        """Test case for update_organization_membership

        Update an organization membership
        """
        pass

    def test_update_organization_membership_metadata(self) -> None:
        """Test case for update_organization_membership_metadata

        Merge and update organization membership metadata
        """
        pass


if __name__ == '__main__':
    unittest.main()

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

from clerk_backend_sdk.api.organizations_api import OrganizationsApi


class TestOrganizationsApi(unittest.TestCase):
    """OrganizationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OrganizationsApi()

    def tearDown(self) -> None:
        pass

    def test_create_organization(self) -> None:
        """Test case for create_organization

        Create an organization
        """
        pass

    def test_delete_organization(self) -> None:
        """Test case for delete_organization

        Delete an organization
        """
        pass

    def test_delete_organization_logo(self) -> None:
        """Test case for delete_organization_logo

        """
        pass

    def test_get_organization(self) -> None:
        """Test case for get_organization

        Retrieve an organization by ID or slug
        """
        pass

    def test_list_organizations(self) -> None:
        """Test case for list_organizations

        Get a list of organizations for an instance
        """
        pass

    def test_merge_organization_metadata(self) -> None:
        """Test case for merge_organization_metadata

        Merge and update metadata for an organization
        """
        pass

    def test_update_organization(self) -> None:
        """Test case for update_organization

        Update an organization
        """
        pass

    def test_upload_organization_logo(self) -> None:
        """Test case for upload_organization_logo

        Upload a logo for the organization
        """
        pass


if __name__ == '__main__':
    unittest.main()

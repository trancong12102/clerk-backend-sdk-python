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

from clerk_backend_sdk.api.invitations_api import InvitationsApi


class TestInvitationsApi(unittest.TestCase):
    """InvitationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = InvitationsApi()

    def tearDown(self) -> None:
        pass

    def test_create_invitation(self) -> None:
        """Test case for create_invitation

        Create an invitation
        """
        pass

    def test_list_invitations(self) -> None:
        """Test case for list_invitations

        List all invitations
        """
        pass

    def test_revoke_invitation(self) -> None:
        """Test case for revoke_invitation

        Revokes an invitation
        """
        pass


if __name__ == '__main__':
    unittest.main()

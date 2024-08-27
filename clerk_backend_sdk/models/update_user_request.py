# coding: utf-8

"""
    Clerk Backend API

    The Clerk REST Backend API, meant to be accessed by backend servers.  ### Versions  When the API changes in a way that isn't compatible with older versions, a new version is released. Each version is identified by its release date, e.g. `2021-02-05`. For more information, please see [Clerk API Versions](https://clerk.com/docs/backend-requests/versioning/overview).   Please see https://clerk.com/docs for more information.

    The version of the OpenAPI document: v1
    Contact: support@clerk.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from clerk_backend_sdk.models.password_hasher import PasswordHasher
from typing import Optional, Set
from typing_extensions import Self

class UpdateUserRequest(BaseModel):
    """
    UpdateUserRequest
    """ # noqa: E501
    external_id: Optional[StrictStr] = Field(default=None, description="The ID of the user as used in your external systems or your previous authentication solution. Must be unique across your instance.")
    first_name: Optional[StrictStr] = Field(default=None, description="The first name to assign to the user")
    last_name: Optional[StrictStr] = Field(default=None, description="The last name to assign to the user")
    primary_email_address_id: Optional[StrictStr] = Field(default=None, description="The ID of the email address to set as primary. It must be verified, and present on the current user.")
    notify_primary_email_address_changed: Optional[StrictBool] = Field(default=False, description="If set to `true`, the user will be notified that their primary email address has changed. By default, no notification is sent.")
    primary_phone_number_id: Optional[StrictStr] = Field(default=None, description="The ID of the phone number to set as primary. It must be verified, and present on the current user.")
    primary_web3_wallet_id: Optional[StrictStr] = Field(default=None, description="The ID of the web3 wallets to set as primary. It must be verified, and present on the current user.")
    username: Optional[StrictStr] = Field(default=None, description="The username to give to the user. It must be unique across your instance.")
    profile_image_id: Optional[StrictStr] = Field(default=None, description="The ID of the image to set as the user's profile image")
    password: Optional[StrictStr] = Field(default=None, description="The plaintext password to give the user. Must be at least 8 characters long, and can not be in any list of hacked passwords.")
    password_digest: Optional[StrictStr] = Field(default=None, description="In case you already have the password digests and not the passwords, you can use them for the newly created user via this property. The digests should be generated with one of the supported algorithms. The hashing algorithm can be specified using the `password_hasher` property.")
    password_hasher: Optional[PasswordHasher] = None
    skip_password_checks: Optional[StrictBool] = Field(default=None, description="Set it to `true` if you're updating the user's password and want to skip any password policy settings check. This parameter can only be used when providing a `password`.")
    sign_out_of_other_sessions: Optional[StrictBool] = Field(default=None, description="Set to `true` to sign out the user from all their active sessions once their password is updated. This parameter can only be used when providing a `password`.")
    totp_secret: Optional[StrictStr] = Field(default=None, description="In case TOTP is configured on the instance, you can provide the secret to enable it on the specific user without the need to reset it. Please note that currently the supported options are: * Period: 30 seconds * Code length: 6 digits * Algorithm: SHA1")
    backup_codes: Optional[List[StrictStr]] = Field(default=None, description="If Backup Codes are configured on the instance, you can provide them to enable it on the specific user without the need to reset them. You must provide the backup codes in plain format or the corresponding bcrypt digest.")
    public_metadata: Optional[Dict[str, Any]] = Field(default=None, description="Metadata saved on the user, that is visible to both your Frontend and Backend APIs")
    private_metadata: Optional[Dict[str, Any]] = Field(default=None, description="Metadata saved on the user, that is only visible to your Backend API")
    unsafe_metadata: Optional[Dict[str, Any]] = Field(default=None, description="Metadata saved on the user, that can be updated from both the Frontend and Backend APIs. Note: Since this data can be modified from the frontend, it is not guaranteed to be safe.")
    delete_self_enabled: Optional[StrictBool] = Field(default=None, description="If true, the user can delete themselves with the Frontend API.")
    create_organization_enabled: Optional[StrictBool] = Field(default=None, description="If true, the user can create organizations with the Frontend API.")
    create_organizations_limit: Optional[StrictInt] = Field(default=None, description="The maximum number of organizations the user can create. 0 means unlimited.")
    created_at: Optional[StrictStr] = Field(default=None, description="A custom date/time denoting _when_ the user signed up to the application, specified in RFC3339 format (e.g. `2012-10-20T07:15:20.902Z`).")
    __properties: ClassVar[List[str]] = ["external_id", "first_name", "last_name", "primary_email_address_id", "notify_primary_email_address_changed", "primary_phone_number_id", "primary_web3_wallet_id", "username", "profile_image_id", "password", "password_digest", "password_hasher", "skip_password_checks", "sign_out_of_other_sessions", "totp_secret", "backup_codes", "public_metadata", "private_metadata", "unsafe_metadata", "delete_self_enabled", "create_organization_enabled", "create_organizations_limit", "created_at"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of UpdateUserRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if external_id (nullable) is None
        # and model_fields_set contains the field
        if self.external_id is None and "external_id" in self.model_fields_set:
            _dict['external_id'] = None

        # set to None if first_name (nullable) is None
        # and model_fields_set contains the field
        if self.first_name is None and "first_name" in self.model_fields_set:
            _dict['first_name'] = None

        # set to None if last_name (nullable) is None
        # and model_fields_set contains the field
        if self.last_name is None and "last_name" in self.model_fields_set:
            _dict['last_name'] = None

        # set to None if username (nullable) is None
        # and model_fields_set contains the field
        if self.username is None and "username" in self.model_fields_set:
            _dict['username'] = None

        # set to None if profile_image_id (nullable) is None
        # and model_fields_set contains the field
        if self.profile_image_id is None and "profile_image_id" in self.model_fields_set:
            _dict['profile_image_id'] = None

        # set to None if password (nullable) is None
        # and model_fields_set contains the field
        if self.password is None and "password" in self.model_fields_set:
            _dict['password'] = None

        # set to None if skip_password_checks (nullable) is None
        # and model_fields_set contains the field
        if self.skip_password_checks is None and "skip_password_checks" in self.model_fields_set:
            _dict['skip_password_checks'] = None

        # set to None if sign_out_of_other_sessions (nullable) is None
        # and model_fields_set contains the field
        if self.sign_out_of_other_sessions is None and "sign_out_of_other_sessions" in self.model_fields_set:
            _dict['sign_out_of_other_sessions'] = None

        # set to None if delete_self_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.delete_self_enabled is None and "delete_self_enabled" in self.model_fields_set:
            _dict['delete_self_enabled'] = None

        # set to None if create_organization_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.create_organization_enabled is None and "create_organization_enabled" in self.model_fields_set:
            _dict['create_organization_enabled'] = None

        # set to None if create_organizations_limit (nullable) is None
        # and model_fields_set contains the field
        if self.create_organizations_limit is None and "create_organizations_limit" in self.model_fields_set:
            _dict['create_organizations_limit'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateUserRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "external_id": obj.get("external_id"),
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "primary_email_address_id": obj.get("primary_email_address_id"),
            "notify_primary_email_address_changed": obj.get("notify_primary_email_address_changed") if obj.get("notify_primary_email_address_changed") is not None else False,
            "primary_phone_number_id": obj.get("primary_phone_number_id"),
            "primary_web3_wallet_id": obj.get("primary_web3_wallet_id"),
            "username": obj.get("username"),
            "profile_image_id": obj.get("profile_image_id"),
            "password": obj.get("password"),
            "password_digest": obj.get("password_digest"),
            "password_hasher": obj.get("password_hasher"),
            "skip_password_checks": obj.get("skip_password_checks"),
            "sign_out_of_other_sessions": obj.get("sign_out_of_other_sessions"),
            "totp_secret": obj.get("totp_secret"),
            "backup_codes": obj.get("backup_codes"),
            "public_metadata": obj.get("public_metadata"),
            "private_metadata": obj.get("private_metadata"),
            "unsafe_metadata": obj.get("unsafe_metadata"),
            "delete_self_enabled": obj.get("delete_self_enabled"),
            "create_organization_enabled": obj.get("create_organization_enabled"),
            "create_organizations_limit": obj.get("create_organizations_limit"),
            "created_at": obj.get("created_at")
        })
        return _obj



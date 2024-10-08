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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CreateOrganizationInvitationBulkRequestInner(BaseModel):
    """
    CreateOrganizationInvitationBulkRequestInner
    """ # noqa: E501
    email_address: StrictStr = Field(description="The email address of the new member that is going to be invited to the organization")
    inviter_user_id: StrictStr = Field(description="The ID of the user that invites the new member to the organization. Must be an administrator in the organization.")
    role: StrictStr = Field(description="The role of the new member in the organization.")
    public_metadata: Optional[Dict[str, Any]] = Field(default=None, description="Metadata saved on the organization invitation, read-only from the Frontend API and fully accessible (read/write) from the Backend API.")
    private_metadata: Optional[Dict[str, Any]] = Field(default=None, description="Metadata saved on the organization invitation, fully accessible (read/write) from the Backend API but not visible from the Frontend API.")
    redirect_url: Optional[StrictStr] = Field(default=None, description="Optional URL that the invitee will be redirected to once they accept the invitation by clicking the join link in the invitation email.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["email_address", "inviter_user_id", "role", "public_metadata", "private_metadata", "redirect_url"]

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
        """Create an instance of CreateOrganizationInvitationBulkRequestInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateOrganizationInvitationBulkRequestInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "email_address": obj.get("email_address"),
            "inviter_user_id": obj.get("inviter_user_id"),
            "role": obj.get("role"),
            "public_metadata": obj.get("public_metadata"),
            "private_metadata": obj.get("private_metadata"),
            "redirect_url": obj.get("redirect_url")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj



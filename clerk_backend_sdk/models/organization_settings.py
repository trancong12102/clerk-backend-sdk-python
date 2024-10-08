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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class OrganizationSettings(BaseModel):
    """
    OrganizationSettings
    """ # noqa: E501
    object: StrictStr = Field(description="String representing the object's type. Objects of the same type share the same value.")
    enabled: StrictBool
    max_allowed_memberships: StrictInt
    max_allowed_roles: Optional[StrictInt] = None
    max_allowed_permissions: Optional[StrictInt] = None
    creator_role: StrictStr = Field(description="The role key that a user will be assigned after creating an organization.")
    admin_delete_enabled: StrictBool = Field(description="The default for whether an admin can delete an organization with the Frontend API.")
    domains_enabled: StrictBool
    domains_enrollment_modes: List[StrictStr]
    domains_default_role: StrictStr = Field(description="The role key that it will be used in order to create an organization invitation or suggestion.")
    __properties: ClassVar[List[str]] = ["object", "enabled", "max_allowed_memberships", "max_allowed_roles", "max_allowed_permissions", "creator_role", "admin_delete_enabled", "domains_enabled", "domains_enrollment_modes", "domains_default_role"]

    @field_validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['organization_settings']):
            raise ValueError("must be one of enum values ('organization_settings')")
        return value

    @field_validator('domains_enrollment_modes')
    def domains_enrollment_modes_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in set(['manual_invitation', 'automatic_invitation', 'automatic_suggestion']):
                raise ValueError("each list item must be one of ('manual_invitation', 'automatic_invitation', 'automatic_suggestion')")
        return value

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
        """Create an instance of OrganizationSettings from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrganizationSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object"),
            "enabled": obj.get("enabled"),
            "max_allowed_memberships": obj.get("max_allowed_memberships"),
            "max_allowed_roles": obj.get("max_allowed_roles"),
            "max_allowed_permissions": obj.get("max_allowed_permissions"),
            "creator_role": obj.get("creator_role"),
            "admin_delete_enabled": obj.get("admin_delete_enabled"),
            "domains_enabled": obj.get("domains_enabled"),
            "domains_enrollment_modes": obj.get("domains_enrollment_modes"),
            "domains_default_role": obj.get("domains_default_role")
        })
        return _obj



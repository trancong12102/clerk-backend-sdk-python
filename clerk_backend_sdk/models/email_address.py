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
from clerk_backend_sdk.models.email_address_verification import EmailAddressVerification
from clerk_backend_sdk.models.identification_link import IdentificationLink
from typing import Optional, Set
from typing_extensions import Self

class EmailAddress(BaseModel):
    """
    EmailAddress
    """ # noqa: E501
    id: Optional[StrictStr] = None
    object: StrictStr = Field(description="String representing the object's type. Objects of the same type share the same value. ")
    email_address: StrictStr
    reserved: StrictBool
    verification: Optional[EmailAddressVerification]
    linked_to: List[IdentificationLink]
    created_at: StrictInt = Field(description="Unix timestamp of creation ")
    updated_at: StrictInt = Field(description="Unix timestamp of creation ")
    __properties: ClassVar[List[str]] = ["id", "object", "email_address", "reserved", "verification", "linked_to", "created_at", "updated_at"]

    @field_validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['email_address']):
            raise ValueError("must be one of enum values ('email_address')")
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
        """Create an instance of EmailAddress from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of verification
        if self.verification:
            _dict['verification'] = self.verification.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in linked_to (list)
        _items = []
        if self.linked_to:
            for _item_linked_to in self.linked_to:
                if _item_linked_to:
                    _items.append(_item_linked_to.to_dict())
            _dict['linked_to'] = _items
        # set to None if verification (nullable) is None
        # and model_fields_set contains the field
        if self.verification is None and "verification" in self.model_fields_set:
            _dict['verification'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EmailAddress from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "object": obj.get("object"),
            "email_address": obj.get("email_address"),
            "reserved": obj.get("reserved"),
            "verification": EmailAddressVerification.from_dict(obj["verification"]) if obj.get("verification") is not None else None,
            "linked_to": [IdentificationLink.from_dict(_item) for _item in obj["linked_to"]] if obj.get("linked_to") is not None else None,
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at")
        })
        return _obj



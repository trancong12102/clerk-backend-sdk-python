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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UpdateInstanceRequest(BaseModel):
    """
    UpdateInstanceRequest
    """ # noqa: E501
    test_mode: Optional[StrictBool] = Field(default=None, description="Toggles test mode for this instance, allowing the use of test email addresses and phone numbers. Defaults to true for development instances.")
    hibp: Optional[StrictBool] = Field(default=None, description="Whether the instance should be using the HIBP service to check passwords for breaches")
    enhanced_email_deliverability: Optional[StrictBool] = Field(default=None, description="The \"enhanced_email_deliverability\" feature will send emails from \"verifications@clerk.dev\" instead of your domain. This can be helpful if you do not have a high domain reputation.")
    support_email: Optional[StrictStr] = None
    clerk_js_version: Optional[StrictStr] = None
    development_origin: Optional[StrictStr] = None
    allowed_origins: Optional[List[StrictStr]] = Field(default=None, description="For browser-like stacks such as browser extensions, Electron, or Capacitor.js the instance allowed origins need to be updated with the request origin value. For Chrome extensions popup, background, or service worker pages the origin is chrome-extension://extension_uiid. For Electron apps the default origin is http://localhost:3000. For Capacitor, the origin is capacitor://localhost.")
    cookieless_dev: Optional[StrictBool] = Field(default=None, description="Whether the instance should operate in cookieless development mode (i.e. without third-party cookies). Deprecated: Please use `url_based_session_syncing` instead.")
    url_based_session_syncing: Optional[StrictBool] = Field(default=None, description="Whether the instance should use URL-based session syncing in development mode (i.e. without third-party cookies).")
    __properties: ClassVar[List[str]] = ["test_mode", "hibp", "enhanced_email_deliverability", "support_email", "clerk_js_version", "development_origin", "allowed_origins", "cookieless_dev", "url_based_session_syncing"]

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
        """Create an instance of UpdateInstanceRequest from a JSON string"""
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
        # set to None if test_mode (nullable) is None
        # and model_fields_set contains the field
        if self.test_mode is None and "test_mode" in self.model_fields_set:
            _dict['test_mode'] = None

        # set to None if hibp (nullable) is None
        # and model_fields_set contains the field
        if self.hibp is None and "hibp" in self.model_fields_set:
            _dict['hibp'] = None

        # set to None if enhanced_email_deliverability (nullable) is None
        # and model_fields_set contains the field
        if self.enhanced_email_deliverability is None and "enhanced_email_deliverability" in self.model_fields_set:
            _dict['enhanced_email_deliverability'] = None

        # set to None if support_email (nullable) is None
        # and model_fields_set contains the field
        if self.support_email is None and "support_email" in self.model_fields_set:
            _dict['support_email'] = None

        # set to None if clerk_js_version (nullable) is None
        # and model_fields_set contains the field
        if self.clerk_js_version is None and "clerk_js_version" in self.model_fields_set:
            _dict['clerk_js_version'] = None

        # set to None if development_origin (nullable) is None
        # and model_fields_set contains the field
        if self.development_origin is None and "development_origin" in self.model_fields_set:
            _dict['development_origin'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateInstanceRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "test_mode": obj.get("test_mode"),
            "hibp": obj.get("hibp"),
            "enhanced_email_deliverability": obj.get("enhanced_email_deliverability"),
            "support_email": obj.get("support_email"),
            "clerk_js_version": obj.get("clerk_js_version"),
            "development_origin": obj.get("development_origin"),
            "allowed_origins": obj.get("allowed_origins"),
            "cookieless_dev": obj.get("cookieless_dev"),
            "url_based_session_syncing": obj.get("url_based_session_syncing")
        })
        return _obj



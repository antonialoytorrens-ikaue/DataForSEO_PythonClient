# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ContentGenerationGenerateMetaTagsLiveResultInfo(BaseModel):
    """
    ContentGenerationGenerateMetaTagsLiveResultInfo
    """ # noqa: E501
    input_tokens: Optional[StrictInt] = Field(default=None, description="number of input tokens")
    output_tokens: Optional[StrictInt] = Field(default=None, description="number of output tokens")
    new_tokens: Optional[StrictInt] = Field(default=None, description="number of new tokens")
    title: Optional[StrictStr] = Field(default=None, description="generated title")
    description: Optional[StrictStr] = Field(default=None, description="generated description")
    __properties: ClassVar[List[str]] = ["input_tokens", "output_tokens", "new_tokens", "title", "description"]

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
        """Create an instance of ContentGenerationGenerateMetaTagsLiveResultInfo from a JSON string"""
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
        # set to None if input_tokens (nullable) is None
        # and model_fields_set contains the field
        if self.input_tokens is None and "input_tokens" in self.model_fields_set:
            _dict['input_tokens'] = None

        # set to None if output_tokens (nullable) is None
        # and model_fields_set contains the field
        if self.output_tokens is None and "output_tokens" in self.model_fields_set:
            _dict['output_tokens'] = None

        # set to None if new_tokens (nullable) is None
        # and model_fields_set contains the field
        if self.new_tokens is None and "new_tokens" in self.model_fields_set:
            _dict['new_tokens'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ContentGenerationGenerateMetaTagsLiveResultInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "input_tokens": obj.get("input_tokens"),
            "output_tokens": obj.get("output_tokens"),
            "new_tokens": obj.get("new_tokens"),
            "title": obj.get("title"),
            "description": obj.get("description")
        })
        return _obj



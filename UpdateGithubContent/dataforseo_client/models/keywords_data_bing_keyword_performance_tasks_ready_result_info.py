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

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class KeywordsDataBingKeywordPerformanceTasksReadyResultInfo(BaseModel):
    """
    KeywordsDataBingKeywordPerformanceTasksReadyResultInfo
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="task identifier of the completed task unique task identifier in our system in the UUID format")
    se: Optional[StrictStr] = Field(default=None, description="search engine specified when setting the task")
    function: Optional[StrictStr] = Field(default=None, description="type of the task")
    date_posted: Optional[StrictStr] = Field(default=None, description="date when the task was posted (in the UTC format)")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier")
    endpoint: Optional[StrictStr] = Field(default=None, description="URL for collecting the results of the task")
    __properties: ClassVar[List[str]] = ["id", "se", "function", "date_posted", "tag", "endpoint"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of KeywordsDataBingKeywordPerformanceTasksReadyResultInfo from a JSON string"""
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
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if se (nullable) is None
        # and model_fields_set contains the field
        if self.se is None and "se" in self.model_fields_set:
            _dict['se'] = None

        # set to None if function (nullable) is None
        # and model_fields_set contains the field
        if self.function is None and "function" in self.model_fields_set:
            _dict['function'] = None

        # set to None if date_posted (nullable) is None
        # and model_fields_set contains the field
        if self.date_posted is None and "date_posted" in self.model_fields_set:
            _dict['date_posted'] = None

        # set to None if tag (nullable) is None
        # and model_fields_set contains the field
        if self.tag is None and "tag" in self.model_fields_set:
            _dict['tag'] = None

        # set to None if endpoint (nullable) is None
        # and model_fields_set contains the field
        if self.endpoint is None and "endpoint" in self.model_fields_set:
            _dict['endpoint'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of KeywordsDataBingKeywordPerformanceTasksReadyResultInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "se": obj.get("se"),
            "function": obj.get("function"),
            "date_posted": obj.get("date_posted"),
            "tag": obj.get("tag"),
            "endpoint": obj.get("endpoint")
        })
        return _obj



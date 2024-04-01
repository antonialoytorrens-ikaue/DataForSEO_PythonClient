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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.queries_list_data_item_info import QueriesListDataItemInfo
from typing import Optional, Set
from typing_extensions import Self

class QueriesListDataInfo(BaseModel):
    """
    QueriesListDataInfo
    """ # noqa: E501
    top: Optional[List[QueriesListDataItemInfo]] = Field(default=None, description="the most popular related topics represents the list of the most popular related topics")
    rising: Optional[List[QueriesListDataItemInfo]] = Field(default=None, description="emerging related topics represents the list of related topics with the biggest increase in search frequency since the last time period")
    __properties: ClassVar[List[str]] = ["top", "rising"]

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
        """Create an instance of QueriesListDataInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in top (list)
        _items = []
        if self.top:
            for _item in self.top:
                if _item:
                    _items.append(_item.to_dict())
            _dict['top'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in rising (list)
        _items = []
        if self.rising:
            for _item in self.rising:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rising'] = _items
        # set to None if top (nullable) is None
        # and model_fields_set contains the field
        if self.top is None and "top" in self.model_fields_set:
            _dict['top'] = None

        # set to None if rising (nullable) is None
        # and model_fields_set contains the field
        if self.rising is None and "rising" in self.model_fields_set:
            _dict['rising'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QueriesListDataInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "top": [QueriesListDataItemInfo.from_dict(_item) for _item in obj["top"]] if obj.get("top") is not None else None,
            "rising": [QueriesListDataItemInfo.from_dict(_item) for _item in obj["rising"]] if obj.get("rising") is not None else None
        })
        return _obj



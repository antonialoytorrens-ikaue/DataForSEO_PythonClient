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

from pydantic import Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.base_dataforseo_trends_item import BaseDataforseoTrendsItem
from dataforseo_client.models.trends_graph_data_info import TrendsGraphDataInfo
from typing import Optional, Set
from typing_extensions import Self

class DataforseoTrendsDataforseoTrendsGraphElementItem(BaseDataforseoTrendsItem):
    """
    DataforseoTrendsDataforseoTrendsGraphElementItem
    """ # noqa: E501
    position: Optional[StrictInt] = Field(default=None, description="the alignment of the element can take the following values: 1, 2, 3, 4, etc.")
    keywords: Optional[List[Optional[StrictStr]]] = Field(default=None, description="relevant keywords the data included in the dataforseo_trends_graph element is based on the keywords listed in this array")
    data: Optional[List[TrendsGraphDataInfo]] = Field(default=None, description="DataForSEO Trends data for the specified parameters")
    averages: Optional[List[Optional[StrictInt]]] = Field(default=None, description="keyword popularity values averaged over the whole time range")
    __properties: ClassVar[List[str]] = ["type", "position", "keywords", "data", "averages"]

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
        """Create an instance of DataforseoTrendsDataforseoTrendsGraphElementItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['data'] = _items
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if position (nullable) is None
        # and model_fields_set contains the field
        if self.position is None and "position" in self.model_fields_set:
            _dict['position'] = None

        # set to None if keywords (nullable) is None
        # and model_fields_set contains the field
        if self.keywords is None and "keywords" in self.model_fields_set:
            _dict['keywords'] = None

        # set to None if data (nullable) is None
        # and model_fields_set contains the field
        if self.data is None and "data" in self.model_fields_set:
            _dict['data'] = None

        # set to None if averages (nullable) is None
        # and model_fields_set contains the field
        if self.averages is None and "averages" in self.model_fields_set:
            _dict['averages'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataforseoTrendsDataforseoTrendsGraphElementItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "position": obj.get("position"),
            "keywords": obj.get("keywords"),
            "data": [TrendsGraphDataInfo.from_dict(_item) for _item in obj["data"]] if obj.get("data") is not None else None,
            "averages": obj.get("averages")
        })
        return _obj



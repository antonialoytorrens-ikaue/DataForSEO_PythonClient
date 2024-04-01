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
from dataforseo_client.models.dataforseo_labs_bing_ranked_keywords_live_item import DataforseoLabsBingRankedKeywordsLiveItem
from dataforseo_client.models.metrics_info import MetricsInfo
from typing import Optional, Set
from typing_extensions import Self

class DataforseoLabsBingRankedKeywordsLiveResultInfo(BaseModel):
    """
    DataforseoLabsBingRankedKeywordsLiveResultInfo
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    target: Optional[StrictStr] = Field(default=None, description="target domain in a POST array")
    location_code: Optional[StrictInt] = Field(default=None, description="location code in a POST array if there is no data, then the value is null")
    language_code: Optional[StrictStr] = Field(default=None, description="language code in a POST array if there is no data, then the value is null")
    total_count: Optional[StrictInt] = Field(default=None, description="total number of results in our database relevant to your request")
    items_count: Optional[StrictInt] = Field(default=None, description="the number of results returned in the items array")
    metrics: Optional[Dict[str, MetricsInfo]] = Field(default=None, description="ranking data relevant to the specified domain ranking data is provided by the rank_group parameters that show the result’s rank considering only equivalent SERP elements")
    metrics_absolute: Optional[Dict[str, MetricsInfo]] = Field(default=None, description="ranking data relevant to the specified domain ranking data is provided by the rank_absolute parameters that indicate the result’s position among all SERP elements")
    items: Optional[List[DataforseoLabsBingRankedKeywordsLiveItem]] = Field(default=None, description="contains ranked keywords and related data")
    __properties: ClassVar[List[str]] = ["se_type", "target", "location_code", "language_code", "total_count", "items_count", "metrics", "metrics_absolute", "items"]

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
        """Create an instance of DataforseoLabsBingRankedKeywordsLiveResultInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in metrics (dict)
        _field_dict = {}
        if self.metrics:
            for _key in self.metrics:
                if self.metrics[_key]:
                    _field_dict[_key] = self.metrics[_key].to_dict()
            _dict['metrics'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in metrics_absolute (dict)
        _field_dict = {}
        if self.metrics_absolute:
            for _key in self.metrics_absolute:
                if self.metrics_absolute[_key]:
                    _field_dict[_key] = self.metrics_absolute[_key].to_dict()
            _dict['metrics_absolute'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        # set to None if se_type (nullable) is None
        # and model_fields_set contains the field
        if self.se_type is None and "se_type" in self.model_fields_set:
            _dict['se_type'] = None

        # set to None if target (nullable) is None
        # and model_fields_set contains the field
        if self.target is None and "target" in self.model_fields_set:
            _dict['target'] = None

        # set to None if location_code (nullable) is None
        # and model_fields_set contains the field
        if self.location_code is None and "location_code" in self.model_fields_set:
            _dict['location_code'] = None

        # set to None if language_code (nullable) is None
        # and model_fields_set contains the field
        if self.language_code is None and "language_code" in self.model_fields_set:
            _dict['language_code'] = None

        # set to None if total_count (nullable) is None
        # and model_fields_set contains the field
        if self.total_count is None and "total_count" in self.model_fields_set:
            _dict['total_count'] = None

        # set to None if items_count (nullable) is None
        # and model_fields_set contains the field
        if self.items_count is None and "items_count" in self.model_fields_set:
            _dict['items_count'] = None

        # set to None if metrics (nullable) is None
        # and model_fields_set contains the field
        if self.metrics is None and "metrics" in self.model_fields_set:
            _dict['metrics'] = None

        # set to None if metrics_absolute (nullable) is None
        # and model_fields_set contains the field
        if self.metrics_absolute is None and "metrics_absolute" in self.model_fields_set:
            _dict['metrics_absolute'] = None

        # set to None if items (nullable) is None
        # and model_fields_set contains the field
        if self.items is None and "items" in self.model_fields_set:
            _dict['items'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataforseoLabsBingRankedKeywordsLiveResultInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "se_type": obj.get("se_type"),
            "target": obj.get("target"),
            "location_code": obj.get("location_code"),
            "language_code": obj.get("language_code"),
            "total_count": obj.get("total_count"),
            "items_count": obj.get("items_count"),
            "metrics": dict(
                (_k, MetricsInfo.from_dict(_v))
                for _k, _v in obj["metrics"].items()
            )
            if obj.get("metrics") is not None
            else None,
            "metrics_absolute": dict(
                (_k, MetricsInfo.from_dict(_v))
                for _k, _v in obj["metrics_absolute"].items()
            )
            if obj.get("metrics_absolute") is not None
            else None,
            "items": [DataforseoLabsBingRankedKeywordsLiveItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None
        })
        return _obj



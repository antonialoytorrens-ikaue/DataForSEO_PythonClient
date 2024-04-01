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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from dataforseo_client.models.google_play_metrics_bundle_info import GooglePlayMetricsBundleInfo
from typing import Optional, Set
from typing_extensions import Self

class DataforseoLabsGoogleAppCompetitorsLiveItem(BaseModel):
    """
    DataforseoLabsGoogleAppCompetitorsLiveItem
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    app_id: Optional[StrictStr] = Field(default=None, description="id of the competitor app")
    avg_position: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="average position of the app in Google Play SERP Note: average position is calculated for intersected keywords only; the value for a given application may differ when combined with different target applications")
    sum_position: Optional[StrictInt] = Field(default=None, description="sum of all app positions in Google Play SERP Note: sum position is calculated for intersected keywords only; the value for a given application may differ when combined with different target applications")
    intersections: Optional[StrictInt] = Field(default=None, description="number of intersecting keywords")
    competitor_metrics: Optional[GooglePlayMetricsBundleInfo] = None
    full_metrics: Optional[GooglePlayMetricsBundleInfo] = None
    __properties: ClassVar[List[str]] = ["se_type", "app_id", "avg_position", "sum_position", "intersections", "competitor_metrics", "full_metrics"]

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
        """Create an instance of DataforseoLabsGoogleAppCompetitorsLiveItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of competitor_metrics
        if self.competitor_metrics:
            _dict['competitor_metrics'] = self.competitor_metrics.to_dict()
        # override the default output from pydantic by calling `to_dict()` of full_metrics
        if self.full_metrics:
            _dict['full_metrics'] = self.full_metrics.to_dict()
        # set to None if se_type (nullable) is None
        # and model_fields_set contains the field
        if self.se_type is None and "se_type" in self.model_fields_set:
            _dict['se_type'] = None

        # set to None if app_id (nullable) is None
        # and model_fields_set contains the field
        if self.app_id is None and "app_id" in self.model_fields_set:
            _dict['app_id'] = None

        # set to None if avg_position (nullable) is None
        # and model_fields_set contains the field
        if self.avg_position is None and "avg_position" in self.model_fields_set:
            _dict['avg_position'] = None

        # set to None if sum_position (nullable) is None
        # and model_fields_set contains the field
        if self.sum_position is None and "sum_position" in self.model_fields_set:
            _dict['sum_position'] = None

        # set to None if intersections (nullable) is None
        # and model_fields_set contains the field
        if self.intersections is None and "intersections" in self.model_fields_set:
            _dict['intersections'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataforseoLabsGoogleAppCompetitorsLiveItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "se_type": obj.get("se_type"),
            "app_id": obj.get("app_id"),
            "avg_position": obj.get("avg_position"),
            "sum_position": obj.get("sum_position"),
            "intersections": obj.get("intersections"),
            "competitor_metrics": GooglePlayMetricsBundleInfo.from_dict(obj["competitor_metrics"]) if obj.get("competitor_metrics") is not None else None,
            "full_metrics": GooglePlayMetricsBundleInfo.from_dict(obj["full_metrics"]) if obj.get("full_metrics") is not None else None
        })
        return _obj



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

from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from dataforseo_client.models.dataforseo_labs_metrics_info import DataforseoLabsMetricsInfo
from typing import Optional, Set
from typing_extensions import Self

class DataforseoLabsCompetitorsDomainLiveItem(BaseModel):
    """
    DataforseoLabsCompetitorsDomainLiveItem
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    domain: Optional[StrictStr] = Field(default=None, description="domain name")
    avg_position: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="average position of the domain in SERP Note: average position is calculated for intersected keywords only; the value for a given domain may differ when combined with different target websites")
    sum_position: Optional[StrictInt] = Field(default=None, description="sum of all domain positions in SERP Note: average position is calculated for intersected keywords only; the value for a given domain may differ when combined with different target websites")
    intersections: Optional[StrictInt] = Field(default=None, description="number of intersecting keywords")
    full_domain_metrics: Optional[Dict[str, DataforseoLabsMetricsInfo]] = Field(default=None, description="metrics for all keywords of the domain full overview of ranking and traffic data relevant to all keywords that the provided domain is ranking for")
    metrics: Optional[Dict[str, DataforseoLabsMetricsInfo]] = Field(default=None, description="metrics for intersecting keywords ranking and traffic data relevant to the keywords that the provided domain shares with the target domain note: in this array ranking and traffic data is provided for the target considering the keywords target shares in search with the competitor’s domain")
    competitor_metrics: Optional[Dict[str, DataforseoLabsMetricsInfo]] = Field(default=None, description="metrics for intersecting keywords ranking and traffic data relevant to the keywords that the provided domain shares with the target domain note: in this array ranking and traffic data is provided for the returned competitor’s domain")
    __properties: ClassVar[List[str]] = ["se_type", "domain", "avg_position", "sum_position", "intersections", "full_domain_metrics", "metrics", "competitor_metrics"]

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
        """Create an instance of DataforseoLabsCompetitorsDomainLiveItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in full_domain_metrics (dict)
        _field_dict = {}
        if self.full_domain_metrics:
            for _key in self.full_domain_metrics:
                if self.full_domain_metrics[_key]:
                    _field_dict[_key] = self.full_domain_metrics[_key].to_dict()
            _dict['full_domain_metrics'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in metrics (dict)
        _field_dict = {}
        if self.metrics:
            for _key in self.metrics:
                if self.metrics[_key]:
                    _field_dict[_key] = self.metrics[_key].to_dict()
            _dict['metrics'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in competitor_metrics (dict)
        _field_dict = {}
        if self.competitor_metrics:
            for _key in self.competitor_metrics:
                if self.competitor_metrics[_key]:
                    _field_dict[_key] = self.competitor_metrics[_key].to_dict()
            _dict['competitor_metrics'] = _field_dict
        # set to None if se_type (nullable) is None
        # and model_fields_set contains the field
        if self.se_type is None and "se_type" in self.model_fields_set:
            _dict['se_type'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

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

        # set to None if full_domain_metrics (nullable) is None
        # and model_fields_set contains the field
        if self.full_domain_metrics is None and "full_domain_metrics" in self.model_fields_set:
            _dict['full_domain_metrics'] = None

        # set to None if metrics (nullable) is None
        # and model_fields_set contains the field
        if self.metrics is None and "metrics" in self.model_fields_set:
            _dict['metrics'] = None

        # set to None if competitor_metrics (nullable) is None
        # and model_fields_set contains the field
        if self.competitor_metrics is None and "competitor_metrics" in self.model_fields_set:
            _dict['competitor_metrics'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataforseoLabsCompetitorsDomainLiveItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "se_type": obj.get("se_type"),
            "domain": obj.get("domain"),
            "avg_position": obj.get("avg_position"),
            "sum_position": obj.get("sum_position"),
            "intersections": obj.get("intersections"),
            "full_domain_metrics": dict(
                (_k, DataforseoLabsMetricsInfo.from_dict(_v))
                for _k, _v in obj["full_domain_metrics"].items()
            )
            if obj.get("full_domain_metrics") is not None
            else None,
            "metrics": dict(
                (_k, DataforseoLabsMetricsInfo.from_dict(_v))
                for _k, _v in obj["metrics"].items()
            )
            if obj.get("metrics") is not None
            else None,
            "competitor_metrics": dict(
                (_k, DataforseoLabsMetricsInfo.from_dict(_v))
                for _k, _v in obj["competitor_metrics"].items()
            )
            if obj.get("competitor_metrics") is not None
            else None
        })
        return _obj



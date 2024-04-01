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
from dataforseo_client.models.metrics_info import MetricsInfo
from typing import Optional, Set
from typing_extensions import Self

class DataforseoLabsGoogleDomainMetricsByCategoriesLiveItem(BaseModel):
    """
    DataforseoLabsGoogleDomainMetricsByCategoriesLiveItem
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    top_categories: Optional[List[Optional[StrictInt]]] = Field(default=None, description="categories for which domains are collected")
    organic_etv: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="current organic ETV of the domain")
    organic_count: Optional[StrictInt] = Field(default=None, description="current total count of organic SERPs that contain the domain")
    organic_is_lost: Optional[StrictInt] = Field(default=None, description="current number of lost ranked elements indicates how many ranked elements of the domain were previously presented in SERPs, but weren’t found during the last check")
    organic_is_new: Optional[StrictInt] = Field(default=None, description="current number of new ranked elements indicates how many new ranked elements were found for the domain")
    domain: Optional[StrictStr] = Field(default=None, description="domain found for the specified category")
    main_domain: Optional[StrictStr] = Field(default=None, description="primary domain")
    metrics_history: Optional[Dict[str, Dict[str, MetricsInfo]]] = Field(default=None, description="historical ranking and traffic data of the domain")
    metrics_difference: Optional[Dict[str, MetricsInfo]] = Field(default=None, description="metrics difference between first_date and second_date calculated by subtracting domain metrics as of the greater date from domain metrics as of the smaller date")
    __properties: ClassVar[List[str]] = ["se_type", "top_categories", "organic_etv", "organic_count", "organic_is_lost", "organic_is_new", "domain", "main_domain", "metrics_history", "metrics_difference"]

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
        """Create an instance of DataforseoLabsGoogleDomainMetricsByCategoriesLiveItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in metrics_history (dict)
        _field_dict = {}
        if self.metrics_history:
            for _key in self.metrics_history:
                if self.metrics_history[_key]:
                    _field_dict[_key] = self.metrics_history[_key].to_dict()
            _dict['metrics_history'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in metrics_difference (dict)
        _field_dict = {}
        if self.metrics_difference:
            for _key in self.metrics_difference:
                if self.metrics_difference[_key]:
                    _field_dict[_key] = self.metrics_difference[_key].to_dict()
            _dict['metrics_difference'] = _field_dict
        # set to None if se_type (nullable) is None
        # and model_fields_set contains the field
        if self.se_type is None and "se_type" in self.model_fields_set:
            _dict['se_type'] = None

        # set to None if top_categories (nullable) is None
        # and model_fields_set contains the field
        if self.top_categories is None and "top_categories" in self.model_fields_set:
            _dict['top_categories'] = None

        # set to None if organic_etv (nullable) is None
        # and model_fields_set contains the field
        if self.organic_etv is None and "organic_etv" in self.model_fields_set:
            _dict['organic_etv'] = None

        # set to None if organic_count (nullable) is None
        # and model_fields_set contains the field
        if self.organic_count is None and "organic_count" in self.model_fields_set:
            _dict['organic_count'] = None

        # set to None if organic_is_lost (nullable) is None
        # and model_fields_set contains the field
        if self.organic_is_lost is None and "organic_is_lost" in self.model_fields_set:
            _dict['organic_is_lost'] = None

        # set to None if organic_is_new (nullable) is None
        # and model_fields_set contains the field
        if self.organic_is_new is None and "organic_is_new" in self.model_fields_set:
            _dict['organic_is_new'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if main_domain (nullable) is None
        # and model_fields_set contains the field
        if self.main_domain is None and "main_domain" in self.model_fields_set:
            _dict['main_domain'] = None

        # set to None if metrics_history (nullable) is None
        # and model_fields_set contains the field
        if self.metrics_history is None and "metrics_history" in self.model_fields_set:
            _dict['metrics_history'] = None

        # set to None if metrics_difference (nullable) is None
        # and model_fields_set contains the field
        if self.metrics_difference is None and "metrics_difference" in self.model_fields_set:
            _dict['metrics_difference'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataforseoLabsGoogleDomainMetricsByCategoriesLiveItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "se_type": obj.get("se_type"),
            "top_categories": obj.get("top_categories"),
            "organic_etv": obj.get("organic_etv"),
            "organic_count": obj.get("organic_count"),
            "organic_is_lost": obj.get("organic_is_lost"),
            "organic_is_new": obj.get("organic_is_new"),
            "domain": obj.get("domain"),
            "main_domain": obj.get("main_domain"),
            "metrics_history": dict(
                (_k, dict(
                    (_ik, MetricsInfo.from_dict(_iv))
                        for _ik, _iv in _v.items()
                    )
                    if _v is not None
                    else None
                )
                for _k, _v in obj.get("metrics_history").items()
            )
            if obj.get("metrics_history") is not None
            else None,
            "metrics_difference": dict(
                (_k, MetricsInfo.from_dict(_v))
                for _k, _v in obj["metrics_difference"].items()
            )
            if obj.get("metrics_difference") is not None
            else None
        })
        return _obj



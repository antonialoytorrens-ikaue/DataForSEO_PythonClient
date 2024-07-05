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
from dataforseo_client.models.data_app_app_store_search_organic_serp_element_item import DataAppAppStoreSearchOrganicSerpElementItem
from typing import Optional, Set
from typing_extensions import Self

class ItemsRankedSerpElement(BaseModel):
    """
    ItemsRankedSerpElement
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    serp_item: Optional[DataAppAppStoreSearchOrganicSerpElementItem] = None
    check_url: Optional[StrictStr] = Field(default=None, description="direct URL to search engine results you can use it to make sure that we provided accurate results")
    se_results_count: Optional[StrictStr] = Field(default=None, description="number of search results for the returned keyword")
    last_updated_time: Optional[StrictStr] = Field(default=None, description="date and time when SERP data was updated in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00")
    previous_updated_time: Optional[StrictStr] = Field(default=None, description="previous to the most recent date and time when SERP data was updated in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-10-15 12:57:46 +00:00; in this case, will equal null")
    __properties: ClassVar[List[str]] = ["se_type", "serp_item", "check_url", "se_results_count", "last_updated_time", "previous_updated_time"]

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
        """Create an instance of ItemsRankedSerpElement from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of serp_item
        if self.serp_item:
            _dict['serp_item'] = self.serp_item.to_dict()
        # set to None if se_type (nullable) is None
        # and model_fields_set contains the field
        if self.se_type is None and "se_type" in self.model_fields_set:
            _dict['se_type'] = None

        # set to None if check_url (nullable) is None
        # and model_fields_set contains the field
        if self.check_url is None and "check_url" in self.model_fields_set:
            _dict['check_url'] = None

        # set to None if se_results_count (nullable) is None
        # and model_fields_set contains the field
        if self.se_results_count is None and "se_results_count" in self.model_fields_set:
            _dict['se_results_count'] = None

        # set to None if last_updated_time (nullable) is None
        # and model_fields_set contains the field
        if self.last_updated_time is None and "last_updated_time" in self.model_fields_set:
            _dict['last_updated_time'] = None

        # set to None if previous_updated_time (nullable) is None
        # and model_fields_set contains the field
        if self.previous_updated_time is None and "previous_updated_time" in self.model_fields_set:
            _dict['previous_updated_time'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ItemsRankedSerpElement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "se_type": obj.get("se_type"),
            "serp_item": DataAppAppStoreSearchOrganicSerpElementItem.from_dict(obj["serp_item"]) if obj.get("serp_item") is not None else None,
            "check_url": obj.get("check_url"),
            "se_results_count": obj.get("se_results_count"),
            "last_updated_time": obj.get("last_updated_time"),
            "previous_updated_time": obj.get("previous_updated_time")
        })
        return _obj



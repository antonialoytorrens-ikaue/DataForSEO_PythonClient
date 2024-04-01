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
from dataforseo_client.models.base_business_data_serp_element_item import BaseBusinessDataSerpElementItem
from dataforseo_client.models.rating_info import RatingInfo
from typing import Optional, Set
from typing_extensions import Self

class BusinessDataTrustpilotReviewsTaskGetResultInfo(BaseModel):
    """
    BusinessDataTrustpilotReviewsTaskGetResultInfo
    """ # noqa: E501
    domain: Optional[StrictStr] = Field(default=None, description="domain of the business entity")
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    se_domain: Optional[StrictStr] = Field(default=None, description="search engine domain in a POST array")
    check_url: Optional[StrictStr] = Field(default=None, description="direct URL to search engine results you can use it to make sure that we provided accurate results")
    datetime: Optional[StrictStr] = Field(default=None, description="date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00")
    title: Optional[StrictStr] = Field(default=None, description="title of the ‘reviews’ element on Trustpilot the name of the business entity for which the reviews are collected")
    location: Optional[StrictStr] = Field(default=None, description="location of the business entity as specified on Trustpilot address of the business entity for which the reviews are collected")
    reviews_count: Optional[StrictInt] = Field(default=None, description="the total number of reviews")
    rating: Optional[RatingInfo] = None
    items_count: Optional[StrictInt] = Field(default=None, description="the number of items in the results array you can get more results by using the depth parameter when setting a task")
    items: Optional[List[BaseBusinessDataSerpElementItem]] = Field(default=None, description="found reviews you can get more results by using the depth parameter when setting a task")
    __properties: ClassVar[List[str]] = ["domain", "type", "se_domain", "check_url", "datetime", "title", "location", "reviews_count", "rating", "items_count", "items"]

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
        """Create an instance of BusinessDataTrustpilotReviewsTaskGetResultInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of rating
        if self.rating:
            _dict['rating'] = self.rating.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if se_domain (nullable) is None
        # and model_fields_set contains the field
        if self.se_domain is None and "se_domain" in self.model_fields_set:
            _dict['se_domain'] = None

        # set to None if check_url (nullable) is None
        # and model_fields_set contains the field
        if self.check_url is None and "check_url" in self.model_fields_set:
            _dict['check_url'] = None

        # set to None if datetime (nullable) is None
        # and model_fields_set contains the field
        if self.datetime is None and "datetime" in self.model_fields_set:
            _dict['datetime'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if location (nullable) is None
        # and model_fields_set contains the field
        if self.location is None and "location" in self.model_fields_set:
            _dict['location'] = None

        # set to None if reviews_count (nullable) is None
        # and model_fields_set contains the field
        if self.reviews_count is None and "reviews_count" in self.model_fields_set:
            _dict['reviews_count'] = None

        # set to None if items_count (nullable) is None
        # and model_fields_set contains the field
        if self.items_count is None and "items_count" in self.model_fields_set:
            _dict['items_count'] = None

        # set to None if items (nullable) is None
        # and model_fields_set contains the field
        if self.items is None and "items" in self.model_fields_set:
            _dict['items'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BusinessDataTrustpilotReviewsTaskGetResultInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "domain": obj.get("domain"),
            "type": obj.get("type"),
            "se_domain": obj.get("se_domain"),
            "check_url": obj.get("check_url"),
            "datetime": obj.get("datetime"),
            "title": obj.get("title"),
            "location": obj.get("location"),
            "reviews_count": obj.get("reviews_count"),
            "rating": RatingInfo.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "items_count": obj.get("items_count"),
            "items": [BaseBusinessDataSerpElementItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None
        })
        return _obj



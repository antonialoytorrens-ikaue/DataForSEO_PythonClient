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
from dataforseo_client.models.base_merchant_serp_element_item import BaseMerchantSerpElementItem
from typing import Optional, Set
from typing_extensions import Self

class MerchantGoogleProductSpecTaskGetAdvancedResultInfo(BaseModel):
    """
    MerchantGoogleProductSpecTaskGetAdvancedResultInfo
    """ # noqa: E501
    product_id: Optional[StrictStr] = Field(default=None, description="product ID in a POST array learn more about the parameter in this help center guide")
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    se_domain: Optional[StrictStr] = Field(default=None, description="search engine domain in a POST array")
    location_code: Optional[StrictInt] = Field(default=None, description="location code in a POST array")
    language_code: Optional[StrictStr] = Field(default=None, description="language code in a POST array")
    title: Optional[StrictStr] = Field(default=None, description="title of the product")
    description: Optional[StrictStr] = Field(default=None, description="description of the product")
    image_url: Optional[StrictStr] = Field(default=None, description="URL of the product image")
    tags: Optional[List[Optional[StrictStr]]] = Field(default=None, description="tags of the product")
    check_url: Optional[StrictStr] = Field(default=None, description="direct URL to search engine results you can use it to make sure that we provided accurate results")
    datetime: Optional[StrictStr] = Field(default=None, description="date and time when the result was received in the format: “year-month-date:minutes:UTC_difference_hours:UTC_difference_minutes” example: 2019-11-15 12:57:46 +00:00")
    item_types: Optional[List[Optional[StrictStr]]] = Field(default=None, description="types of items found on the product specification page possible item types: shopping_specification")
    items_count: Optional[StrictInt] = Field(default=None, description="the number of results returned in the items array")
    items: Optional[List[BaseMerchantSerpElementItem]] = Field(default=None, description="items on the product specification page contains all product attributes and related data listed on the product specification page")
    __properties: ClassVar[List[str]] = ["product_id", "type", "se_domain", "location_code", "language_code", "title", "description", "image_url", "tags", "check_url", "datetime", "item_types", "items_count", "items"]

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
        """Create an instance of MerchantGoogleProductSpecTaskGetAdvancedResultInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        # set to None if product_id (nullable) is None
        # and model_fields_set contains the field
        if self.product_id is None and "product_id" in self.model_fields_set:
            _dict['product_id'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if se_domain (nullable) is None
        # and model_fields_set contains the field
        if self.se_domain is None and "se_domain" in self.model_fields_set:
            _dict['se_domain'] = None

        # set to None if location_code (nullable) is None
        # and model_fields_set contains the field
        if self.location_code is None and "location_code" in self.model_fields_set:
            _dict['location_code'] = None

        # set to None if language_code (nullable) is None
        # and model_fields_set contains the field
        if self.language_code is None and "language_code" in self.model_fields_set:
            _dict['language_code'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if image_url (nullable) is None
        # and model_fields_set contains the field
        if self.image_url is None and "image_url" in self.model_fields_set:
            _dict['image_url'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        # set to None if check_url (nullable) is None
        # and model_fields_set contains the field
        if self.check_url is None and "check_url" in self.model_fields_set:
            _dict['check_url'] = None

        # set to None if datetime (nullable) is None
        # and model_fields_set contains the field
        if self.datetime is None and "datetime" in self.model_fields_set:
            _dict['datetime'] = None

        # set to None if item_types (nullable) is None
        # and model_fields_set contains the field
        if self.item_types is None and "item_types" in self.model_fields_set:
            _dict['item_types'] = None

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
        """Create an instance of MerchantGoogleProductSpecTaskGetAdvancedResultInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "product_id": obj.get("product_id"),
            "type": obj.get("type"),
            "se_domain": obj.get("se_domain"),
            "location_code": obj.get("location_code"),
            "language_code": obj.get("language_code"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "image_url": obj.get("image_url"),
            "tags": obj.get("tags"),
            "check_url": obj.get("check_url"),
            "datetime": obj.get("datetime"),
            "item_types": obj.get("item_types"),
            "items_count": obj.get("items_count"),
            "items": [BaseMerchantSerpElementItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None
        })
        return _obj



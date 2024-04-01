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
from dataforseo_client.models.hotel_price_item_info import HotelPriceItemInfo
from typing import Optional, Set
from typing_extensions import Self

class HotelPriceInfo(BaseModel):
    """
    HotelPriceInfo
    """ # noqa: E501
    price: Optional[StrictInt] = Field(default=None, description="price per night")
    price_without_discount: Optional[StrictInt] = Field(default=None, description="full price per night without a discount applied")
    currency: Optional[StrictStr] = Field(default=None, description="price currency USD is applied by default, unless specified in the POST array")
    discount_text: Optional[StrictStr] = Field(default=None, description="text about a discount applied")
    check_in: Optional[StrictStr] = Field(default=None, description="check-in date and time in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00")
    check_out: Optional[StrictStr] = Field(default=None, description="check-out date and time in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00")
    visitors: Optional[StrictInt] = Field(default=None, description="number of hotel visitors for this price")
    items: Optional[List[HotelPriceItemInfo]] = Field(default=None, description="encountered item types types of search engine results encountered in the items array; possible item types: hotel_search_item")
    __properties: ClassVar[List[str]] = ["price", "price_without_discount", "currency", "discount_text", "check_in", "check_out", "visitors", "items"]

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
        """Create an instance of HotelPriceInfo from a JSON string"""
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
        # set to None if price (nullable) is None
        # and model_fields_set contains the field
        if self.price is None and "price" in self.model_fields_set:
            _dict['price'] = None

        # set to None if price_without_discount (nullable) is None
        # and model_fields_set contains the field
        if self.price_without_discount is None and "price_without_discount" in self.model_fields_set:
            _dict['price_without_discount'] = None

        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

        # set to None if discount_text (nullable) is None
        # and model_fields_set contains the field
        if self.discount_text is None and "discount_text" in self.model_fields_set:
            _dict['discount_text'] = None

        # set to None if check_in (nullable) is None
        # and model_fields_set contains the field
        if self.check_in is None and "check_in" in self.model_fields_set:
            _dict['check_in'] = None

        # set to None if check_out (nullable) is None
        # and model_fields_set contains the field
        if self.check_out is None and "check_out" in self.model_fields_set:
            _dict['check_out'] = None

        # set to None if visitors (nullable) is None
        # and model_fields_set contains the field
        if self.visitors is None and "visitors" in self.model_fields_set:
            _dict['visitors'] = None

        # set to None if items (nullable) is None
        # and model_fields_set contains the field
        if self.items is None and "items" in self.model_fields_set:
            _dict['items'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HotelPriceInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "price": obj.get("price"),
            "price_without_discount": obj.get("price_without_discount"),
            "currency": obj.get("currency"),
            "discount_text": obj.get("discount_text"),
            "check_in": obj.get("check_in"),
            "check_out": obj.get("check_out"),
            "visitors": obj.get("visitors"),
            "items": [HotelPriceItemInfo.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None
        })
        return _obj



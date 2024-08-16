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

from pydantic import BaseModel
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.appendix_amazon_merchant_price_data import AppendixAmazonMerchantPriceData
from dataforseo_client.models.appendix_google_merchant_price_data import AppendixGoogleMerchantPriceData
from dataforseo_client.models.appendix_product_google_merchant_price_data_info import AppendixProductGoogleMerchantPriceDataInfo
from dataforseo_client.models.appendix_task_keywords_data_price_data_info import AppendixTaskKeywordsDataPriceDataInfo
from typing import Optional, Set
from typing_extensions import Self

class AppendixMerchantPriceData(BaseModel):
    """
    AppendixMerchantPriceData
    """ # noqa: E501
    google: Optional[AppendixGoogleMerchantPriceData] = None
    amazon: Optional[AppendixAmazonMerchantPriceData] = None
    errors: Optional[AppendixTaskKeywordsDataPriceDataInfo] = None
    languages: Optional[AppendixTaskKeywordsDataPriceDataInfo] = None
    locations: Optional[AppendixTaskKeywordsDataPriceDataInfo] = None
    reviews: Optional[AppendixProductGoogleMerchantPriceDataInfo] = None
    tasks_ready: Optional[AppendixTaskKeywordsDataPriceDataInfo] = None
    __properties: ClassVar[List[str]] = ["google", "amazon", "errors", "languages", "locations", "reviews", "tasks_ready"]

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
        """Create an instance of AppendixMerchantPriceData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of google
        if self.google:
            _dict['google'] = self.google.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amazon
        if self.amazon:
            _dict['amazon'] = self.amazon.to_dict()
        # override the default output from pydantic by calling `to_dict()` of errors
        if self.errors:
            _dict['errors'] = self.errors.to_dict()
        # override the default output from pydantic by calling `to_dict()` of languages
        if self.languages:
            _dict['languages'] = self.languages.to_dict()
        # override the default output from pydantic by calling `to_dict()` of locations
        if self.locations:
            _dict['locations'] = self.locations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reviews
        if self.reviews:
            _dict['reviews'] = self.reviews.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tasks_ready
        if self.tasks_ready:
            _dict['tasks_ready'] = self.tasks_ready.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AppendixMerchantPriceData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "google": AppendixGoogleMerchantPriceData.from_dict(obj["google"]) if obj.get("google") is not None else None,
            "amazon": AppendixAmazonMerchantPriceData.from_dict(obj["amazon"]) if obj.get("amazon") is not None else None,
            "errors": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["errors"]) if obj.get("errors") is not None else None,
            "languages": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["languages"]) if obj.get("languages") is not None else None,
            "locations": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["locations"]) if obj.get("locations") is not None else None,
            "reviews": AppendixProductGoogleMerchantPriceDataInfo.from_dict(obj["reviews"]) if obj.get("reviews") is not None else None,
            "tasks_ready": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["tasks_ready"]) if obj.get("tasks_ready") is not None else None
        })
        return _obj



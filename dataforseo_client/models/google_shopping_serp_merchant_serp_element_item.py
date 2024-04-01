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

from pydantic import ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from dataforseo_client.models.base_merchant_serp_element_item import BaseMerchantSerpElementItem
from dataforseo_client.models.delivery_info import DeliveryInfo
from dataforseo_client.models.rating_element import RatingElement
from dataforseo_client.models.stores_count_info import StoresCountInfo
from typing import Optional, Set
from typing_extensions import Self

class GoogleShoppingSerpMerchantSerpElementItem(BaseMerchantSerpElementItem):
    """
    GoogleShoppingSerpMerchantSerpElementItem
    """ # noqa: E501
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP absolute position among all the elements found in Google Shopping SERP")
    position: Optional[StrictStr] = Field(default=None, description="alignment of the element in SERP can take the following values: left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="XPath of the element")
    domain: Optional[StrictStr] = Field(default=None, description="domain in SERP")
    title: Optional[StrictStr] = Field(default=None, description="title of the element")
    description: Optional[StrictStr] = Field(default=None, description="description of the product in Google Shopping SERP")
    url: Optional[StrictStr] = Field(default=None, description="URL to the product page on the seller’s website")
    shopping_url: Optional[StrictStr] = Field(default=None, description="URL to the product page on Google Shopping")
    tags: Optional[List[Optional[StrictStr]]] = Field(default=None, description="tags assigned to the product")
    price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="product price example: 384.99")
    old_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="product old price displayed if the product price has been changed example: 499")
    currency: Optional[StrictStr] = Field(default=None, description="currency in the ISO format example: USD")
    product_id: Optional[StrictStr] = Field(default=None, description="unique product identifier on Google Shopping note that there is no full list of possible values as the product_id is a dynamic value assigned by Google if there are no values, you will get null example: 4485466949985702538 learn more about the parameter in this help center guide")
    data_docid: Optional[StrictStr] = Field(default=None, description="unique identifier of the SERP data element note that there is no full list of possible values as the data_docid is a dynamic value assigned by Google example: 17363035694596624076")
    seller: Optional[StrictStr] = Field(default=None, description="name of the seller the name of the company that placed a corresponding product on Google Shopping")
    additional_specifications: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="object containing additional url parameters you can get more details about the product by using this object in the POST request to the Google Shopping Product Specification and Google Shopping Sellers endpoint")
    reviews_count: Optional[StrictInt] = Field(default=None, description="number of product reviews indicates the number of reviews left by users on Google Shopping if there are no values, you will get null")
    is_best_match: Optional[StrictBool] = Field(default=None, description="“best match” label if the value is true, the product is marked with the “best match” label if there are no values, you will get null")
    product_rating: Optional[RatingElement] = None
    shop_rating: Optional[RatingElement] = None
    product_images: Optional[List[Optional[StrictStr]]] = Field(default=None, description="URLs to the images of the product the first URL in the array is the featured image of the product")
    shop_ad_aclk: Optional[StrictStr] = Field(default=None, description="unique ad click referral parameter using this parameter you can get a URL of the advertisement in Google Shopping Sellers Ad URL")
    delivery_info: Optional[DeliveryInfo] = None
    stores_count_info: Optional[StoresCountInfo] = None
    __properties: ClassVar[List[str]] = ["type", "rank_group", "rank_absolute", "position", "xpath", "domain", "title", "description", "url", "shopping_url", "tags", "price", "old_price", "currency", "product_id", "data_docid", "seller", "additional_specifications", "reviews_count", "is_best_match", "product_rating", "shop_rating", "product_images", "shop_ad_aclk", "delivery_info", "stores_count_info"]

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
        """Create an instance of GoogleShoppingSerpMerchantSerpElementItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of product_rating
        if self.product_rating:
            _dict['product_rating'] = self.product_rating.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shop_rating
        if self.shop_rating:
            _dict['shop_rating'] = self.shop_rating.to_dict()
        # override the default output from pydantic by calling `to_dict()` of delivery_info
        if self.delivery_info:
            _dict['delivery_info'] = self.delivery_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of stores_count_info
        if self.stores_count_info:
            _dict['stores_count_info'] = self.stores_count_info.to_dict()
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if rank_group (nullable) is None
        # and model_fields_set contains the field
        if self.rank_group is None and "rank_group" in self.model_fields_set:
            _dict['rank_group'] = None

        # set to None if rank_absolute (nullable) is None
        # and model_fields_set contains the field
        if self.rank_absolute is None and "rank_absolute" in self.model_fields_set:
            _dict['rank_absolute'] = None

        # set to None if position (nullable) is None
        # and model_fields_set contains the field
        if self.position is None and "position" in self.model_fields_set:
            _dict['position'] = None

        # set to None if xpath (nullable) is None
        # and model_fields_set contains the field
        if self.xpath is None and "xpath" in self.model_fields_set:
            _dict['xpath'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if shopping_url (nullable) is None
        # and model_fields_set contains the field
        if self.shopping_url is None and "shopping_url" in self.model_fields_set:
            _dict['shopping_url'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        # set to None if price (nullable) is None
        # and model_fields_set contains the field
        if self.price is None and "price" in self.model_fields_set:
            _dict['price'] = None

        # set to None if old_price (nullable) is None
        # and model_fields_set contains the field
        if self.old_price is None and "old_price" in self.model_fields_set:
            _dict['old_price'] = None

        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

        # set to None if product_id (nullable) is None
        # and model_fields_set contains the field
        if self.product_id is None and "product_id" in self.model_fields_set:
            _dict['product_id'] = None

        # set to None if data_docid (nullable) is None
        # and model_fields_set contains the field
        if self.data_docid is None and "data_docid" in self.model_fields_set:
            _dict['data_docid'] = None

        # set to None if seller (nullable) is None
        # and model_fields_set contains the field
        if self.seller is None and "seller" in self.model_fields_set:
            _dict['seller'] = None

        # set to None if additional_specifications (nullable) is None
        # and model_fields_set contains the field
        if self.additional_specifications is None and "additional_specifications" in self.model_fields_set:
            _dict['additional_specifications'] = None

        # set to None if reviews_count (nullable) is None
        # and model_fields_set contains the field
        if self.reviews_count is None and "reviews_count" in self.model_fields_set:
            _dict['reviews_count'] = None

        # set to None if is_best_match (nullable) is None
        # and model_fields_set contains the field
        if self.is_best_match is None and "is_best_match" in self.model_fields_set:
            _dict['is_best_match'] = None

        # set to None if product_images (nullable) is None
        # and model_fields_set contains the field
        if self.product_images is None and "product_images" in self.model_fields_set:
            _dict['product_images'] = None

        # set to None if shop_ad_aclk (nullable) is None
        # and model_fields_set contains the field
        if self.shop_ad_aclk is None and "shop_ad_aclk" in self.model_fields_set:
            _dict['shop_ad_aclk'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GoogleShoppingSerpMerchantSerpElementItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "position": obj.get("position"),
            "xpath": obj.get("xpath"),
            "domain": obj.get("domain"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "url": obj.get("url"),
            "shopping_url": obj.get("shopping_url"),
            "tags": obj.get("tags"),
            "price": obj.get("price"),
            "old_price": obj.get("old_price"),
            "currency": obj.get("currency"),
            "product_id": obj.get("product_id"),
            "data_docid": obj.get("data_docid"),
            "seller": obj.get("seller"),
            "additional_specifications": obj.get("additional_specifications"),
            "reviews_count": obj.get("reviews_count"),
            "is_best_match": obj.get("is_best_match"),
            "product_rating": RatingElement.from_dict(obj["product_rating"]) if obj.get("product_rating") is not None else None,
            "shop_rating": RatingElement.from_dict(obj["shop_rating"]) if obj.get("shop_rating") is not None else None,
            "product_images": obj.get("product_images"),
            "shop_ad_aclk": obj.get("shop_ad_aclk"),
            "delivery_info": DeliveryInfo.from_dict(obj["delivery_info"]) if obj.get("delivery_info") is not None else None,
            "stores_count_info": StoresCountInfo.from_dict(obj["stores_count_info"]) if obj.get("stores_count_info") is not None else None
        })
        return _obj



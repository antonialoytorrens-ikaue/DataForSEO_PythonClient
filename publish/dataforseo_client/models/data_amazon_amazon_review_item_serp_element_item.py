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

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.base_amazon_serp_element_item import BaseAmazonSerpElementItem
from dataforseo_client.models.images_element import ImagesElement
from dataforseo_client.models.rating_info import RatingInfo
from dataforseo_client.models.user_profile_info import UserProfileInfo
from dataforseo_client.models.video_element import VideoElement
from typing import Optional, Set
from typing_extensions import Self

class DataAmazonAmazonReviewItemSerpElementItem(BaseAmazonSerpElementItem):
    """
    DataAmazonAmazonReviewItemSerpElementItem
    """ # noqa: E501
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank among all the listed reviews absolute position among all reviews on the list")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the review in SERP can take the following values: right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    verified: Optional[StrictBool] = Field(default=None, description="indicates whether the review has the “Verified Purchase” mark")
    subtitle: Optional[StrictStr] = Field(default=None, description="subtitle of the review")
    helpful_votes: Optional[StrictInt] = Field(default=None, description="helpful votes count number of users who clicked on the ‘Helpful” button under the review text")
    images: Optional[List[ImagesElement]] = Field(default=None, description="images of the product submitted by the reviewer")
    videos: Optional[List[VideoElement]] = Field(default=None, description="videos of the product submitted by the reviewer")
    user_profile: Optional[UserProfileInfo] = None
    title: Optional[StrictStr] = Field(default=None, description="title of the review")
    url: Optional[StrictStr] = Field(default=None, description="URL to the review")
    review_text: Optional[StrictStr] = Field(default=None, description="content of the review")
    publication_date: Optional[StrictStr] = Field(default=None, description="date and time when the review was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”; example: 2019-11-15 12:57:46 +00:00")
    rating: Optional[RatingInfo] = None
    __properties: ClassVar[List[str]] = ["type", "rank_group", "rank_absolute", "position", "xpath", "verified", "subtitle", "helpful_votes", "images", "videos", "user_profile", "title", "url", "review_text", "publication_date", "rating"]

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
        """Create an instance of DataAmazonAmazonReviewItemSerpElementItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in images (list)
        _items = []
        if self.images:
            for _item in self.images:
                if _item:
                    _items.append(_item.to_dict())
            _dict['images'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in videos (list)
        _items = []
        if self.videos:
            for _item in self.videos:
                if _item:
                    _items.append(_item.to_dict())
            _dict['videos'] = _items
        # override the default output from pydantic by calling `to_dict()` of user_profile
        if self.user_profile:
            _dict['user_profile'] = self.user_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rating
        if self.rating:
            _dict['rating'] = self.rating.to_dict()
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

        # set to None if verified (nullable) is None
        # and model_fields_set contains the field
        if self.verified is None and "verified" in self.model_fields_set:
            _dict['verified'] = None

        # set to None if subtitle (nullable) is None
        # and model_fields_set contains the field
        if self.subtitle is None and "subtitle" in self.model_fields_set:
            _dict['subtitle'] = None

        # set to None if helpful_votes (nullable) is None
        # and model_fields_set contains the field
        if self.helpful_votes is None and "helpful_votes" in self.model_fields_set:
            _dict['helpful_votes'] = None

        # set to None if images (nullable) is None
        # and model_fields_set contains the field
        if self.images is None and "images" in self.model_fields_set:
            _dict['images'] = None

        # set to None if videos (nullable) is None
        # and model_fields_set contains the field
        if self.videos is None and "videos" in self.model_fields_set:
            _dict['videos'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if review_text (nullable) is None
        # and model_fields_set contains the field
        if self.review_text is None and "review_text" in self.model_fields_set:
            _dict['review_text'] = None

        # set to None if publication_date (nullable) is None
        # and model_fields_set contains the field
        if self.publication_date is None and "publication_date" in self.model_fields_set:
            _dict['publication_date'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataAmazonAmazonReviewItemSerpElementItem from a dict"""
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
            "verified": obj.get("verified"),
            "subtitle": obj.get("subtitle"),
            "helpful_votes": obj.get("helpful_votes"),
            "images": [ImagesElement.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "videos": [VideoElement.from_dict(_item) for _item in obj["videos"]] if obj.get("videos") is not None else None,
            "user_profile": UserProfileInfo.from_dict(obj["user_profile"]) if obj.get("user_profile") is not None else None,
            "title": obj.get("title"),
            "url": obj.get("url"),
            "review_text": obj.get("review_text"),
            "publication_date": obj.get("publication_date"),
            "rating": RatingInfo.from_dict(obj["rating"]) if obj.get("rating") is not None else None
        })
        return _obj



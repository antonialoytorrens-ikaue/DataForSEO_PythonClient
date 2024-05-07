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
from dataforseo_client.models.base_business_data_serp_element_item import BaseBusinessDataSerpElementItem
from dataforseo_client.models.business_data_user_profile_info import BusinessDataUserProfileInfo
from dataforseo_client.models.rating_info import RatingInfo
from dataforseo_client.models.review_response_item_info import ReviewResponseItemInfo
from typing import Optional, Set
from typing_extensions import Self

class TrustpilotReviewSearchBusinessDataSerpElementItem(BaseBusinessDataSerpElementItem):
    """
    TrustpilotReviewSearchBusinessDataSerpElementItem
    """ # noqa: E501
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank among all the listed reviews absolute position among all reviews on the list")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the review in SERP can take the following values: right")
    url: Optional[StrictStr] = Field(default=None, description="the URL of the review")
    rating: Optional[RatingInfo] = None
    verified: Optional[StrictBool] = Field(default=None, description="indicates whether the review has the “Verified” mark")
    language: Optional[StrictStr] = Field(default=None, description="the language of the review")
    timestamp: Optional[StrictStr] = Field(default=None, description="date and time when a review was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00")
    title: Optional[StrictStr] = Field(default=None, description="the title of the review")
    review_text: Optional[StrictStr] = Field(default=None, description="the content of the review")
    review_images: Optional[List[StrictStr]] = Field(default=None, description="images submitted by the reviewer displays URLs to the images provided by the author of the review; please note that Trustpilot doesn’t allow adding images to reviews, so the review_images parameter will always equal null")
    user_profile: Optional[BusinessDataUserProfileInfo] = None
    responses: Optional[List[ReviewResponseItemInfo]] = Field(default=None, description="owner’s response to the submitted review")
    __properties: ClassVar[List[str]] = ["type", "rank_group", "rank_absolute", "position", "url", "rating", "verified", "language", "timestamp", "title", "review_text", "review_images", "user_profile", "responses"]

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
        """Create an instance of TrustpilotReviewSearchBusinessDataSerpElementItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of user_profile
        if self.user_profile:
            _dict['user_profile'] = self.user_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in responses (list)
        _items = []
        if self.responses:
            for _item in self.responses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['responses'] = _items
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

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if verified (nullable) is None
        # and model_fields_set contains the field
        if self.verified is None and "verified" in self.model_fields_set:
            _dict['verified'] = None

        # set to None if language (nullable) is None
        # and model_fields_set contains the field
        if self.language is None and "language" in self.model_fields_set:
            _dict['language'] = None

        # set to None if timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.timestamp is None and "timestamp" in self.model_fields_set:
            _dict['timestamp'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if review_text (nullable) is None
        # and model_fields_set contains the field
        if self.review_text is None and "review_text" in self.model_fields_set:
            _dict['review_text'] = None

        # set to None if review_images (nullable) is None
        # and model_fields_set contains the field
        if self.review_images is None and "review_images" in self.model_fields_set:
            _dict['review_images'] = None

        # set to None if responses (nullable) is None
        # and model_fields_set contains the field
        if self.responses is None and "responses" in self.model_fields_set:
            _dict['responses'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TrustpilotReviewSearchBusinessDataSerpElementItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "position": obj.get("position"),
            "url": obj.get("url"),
            "rating": RatingInfo.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "verified": obj.get("verified"),
            "language": obj.get("language"),
            "timestamp": obj.get("timestamp"),
            "title": obj.get("title"),
            "review_text": obj.get("review_text"),
            "review_images": obj.get("review_images"),
            "user_profile": BusinessDataUserProfileInfo.from_dict(obj["user_profile"]) if obj.get("user_profile") is not None else None,
            "responses": [ReviewResponseItemInfo.from_dict(_item) for _item in obj["responses"]] if obj.get("responses") is not None else None
        })
        return _obj



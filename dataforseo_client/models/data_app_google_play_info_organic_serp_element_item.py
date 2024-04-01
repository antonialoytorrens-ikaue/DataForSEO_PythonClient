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

from pydantic import ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.apps_info import AppsInfo
from dataforseo_client.models.base_app_data_serp_element_item import BaseAppDataSerpElementItem
from dataforseo_client.models.price_info import PriceInfo
from dataforseo_client.models.rating_info import RatingInfo
from typing import Optional, Set
from typing_extensions import Self

class DataAppGooglePlayInfoOrganicSerpElementItem(BaseAppDataSerpElementItem):
    """
    DataAppGooglePlayInfoOrganicSerpElementItem
    """ # noqa: E501
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank among all the listed apps absolute position among all apps on the list")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP can take the following values: left")
    app_id: Optional[StrictStr] = Field(default=None, description="ID of the app")
    title: Optional[StrictStr] = Field(default=None, description="title of the app")
    url: Optional[StrictStr] = Field(default=None, description="URL to the app page on Google Play")
    icon: Optional[StrictStr] = Field(default=None, description="URL to the app icon")
    description: Optional[StrictStr] = Field(default=None, description="description of the app")
    reviews_count: Optional[StrictInt] = Field(default=None, description="the total number of reviews the app has")
    rating: Optional[RatingInfo] = None
    price: Optional[PriceInfo] = None
    is_free: Optional[StrictBool] = Field(default=None, description="indicates whether the app is free")
    main_category: Optional[StrictStr] = Field(default=None, description="main category of the app")
    installs: Optional[StrictStr] = Field(default=None, description="number of installs of the app approximate number of installs as displayed on the app page")
    installs_count: Optional[StrictInt] = Field(default=None, description="number of installs of the app the exact number of installs of the app")
    developer: Optional[StrictStr] = Field(default=None, description="name of the app developer")
    developer_id: Optional[StrictStr] = Field(default=None, description="ID of the app developer")
    developer_url: Optional[StrictStr] = Field(default=None, description="URL to the developer page on Google Play")
    developer_email: Optional[StrictStr] = Field(default=None, description="email address of the developer")
    developer_address: Optional[StrictStr] = Field(default=None, description="physical address of the developer")
    developer_website: Optional[StrictStr] = Field(default=None, description="official website of the developer")
    version: Optional[StrictStr] = Field(default=None, description="current version of the app")
    minimum_os_version: Optional[StrictStr] = Field(default=None, description="minimum OS version required to install the app")
    size: Optional[StrictStr] = Field(default=None, description="size of the app")
    released_date: Optional[StrictStr] = Field(default=None, description="date and time when the app was released in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”; example: 2019-11-15 12:57:46 +00:00")
    last_update_date: Optional[StrictStr] = Field(default=None, description="date and time when the app was last updated in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”; example: 2019-11-15 12:57:46 +00:00")
    update_notes: Optional[StrictStr] = Field(default=None, description="update notes contains the latest update notes from the developer")
    images: Optional[List[Optional[StrictStr]]] = Field(default=None, description="app images contains URLs to the images published on the app page on Google Play")
    videos: Optional[List[Optional[StrictStr]]] = Field(default=None, description="app videos contains URLs to the video published on the app page on Google Play")
    similar_apps: Optional[List[AppsInfo]] = Field(default=None, description="similar apps displays apps similar to the app in a POST request")
    more_apps_by_developer: Optional[List[AppsInfo]] = Field(default=None, description="similar apps information about apps built by the same developer")
    genres: Optional[List[Optional[StrictStr]]] = Field(default=None, description="app genres contains relevant app categories")
    tags: Optional[List[Optional[StrictStr]]] = Field(default=None, description="app tags contains relevant app tags")
    __properties: ClassVar[List[str]] = ["type", "rank_group", "rank_absolute", "position", "app_id", "title", "url", "icon", "description", "reviews_count", "rating", "price", "is_free", "main_category", "installs", "installs_count", "developer", "developer_id", "developer_url", "developer_email", "developer_address", "developer_website", "version", "minimum_os_version", "size", "released_date", "last_update_date", "update_notes", "images", "videos", "similar_apps", "more_apps_by_developer", "genres", "tags"]

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
        """Create an instance of DataAppGooglePlayInfoOrganicSerpElementItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of price
        if self.price:
            _dict['price'] = self.price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in similar_apps (list)
        _items = []
        if self.similar_apps:
            for _item in self.similar_apps:
                if _item:
                    _items.append(_item.to_dict())
            _dict['similar_apps'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in more_apps_by_developer (list)
        _items = []
        if self.more_apps_by_developer:
            for _item in self.more_apps_by_developer:
                if _item:
                    _items.append(_item.to_dict())
            _dict['more_apps_by_developer'] = _items
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

        # set to None if app_id (nullable) is None
        # and model_fields_set contains the field
        if self.app_id is None and "app_id" in self.model_fields_set:
            _dict['app_id'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if icon (nullable) is None
        # and model_fields_set contains the field
        if self.icon is None and "icon" in self.model_fields_set:
            _dict['icon'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if reviews_count (nullable) is None
        # and model_fields_set contains the field
        if self.reviews_count is None and "reviews_count" in self.model_fields_set:
            _dict['reviews_count'] = None

        # set to None if is_free (nullable) is None
        # and model_fields_set contains the field
        if self.is_free is None and "is_free" in self.model_fields_set:
            _dict['is_free'] = None

        # set to None if main_category (nullable) is None
        # and model_fields_set contains the field
        if self.main_category is None and "main_category" in self.model_fields_set:
            _dict['main_category'] = None

        # set to None if installs (nullable) is None
        # and model_fields_set contains the field
        if self.installs is None and "installs" in self.model_fields_set:
            _dict['installs'] = None

        # set to None if installs_count (nullable) is None
        # and model_fields_set contains the field
        if self.installs_count is None and "installs_count" in self.model_fields_set:
            _dict['installs_count'] = None

        # set to None if developer (nullable) is None
        # and model_fields_set contains the field
        if self.developer is None and "developer" in self.model_fields_set:
            _dict['developer'] = None

        # set to None if developer_id (nullable) is None
        # and model_fields_set contains the field
        if self.developer_id is None and "developer_id" in self.model_fields_set:
            _dict['developer_id'] = None

        # set to None if developer_url (nullable) is None
        # and model_fields_set contains the field
        if self.developer_url is None and "developer_url" in self.model_fields_set:
            _dict['developer_url'] = None

        # set to None if developer_email (nullable) is None
        # and model_fields_set contains the field
        if self.developer_email is None and "developer_email" in self.model_fields_set:
            _dict['developer_email'] = None

        # set to None if developer_address (nullable) is None
        # and model_fields_set contains the field
        if self.developer_address is None and "developer_address" in self.model_fields_set:
            _dict['developer_address'] = None

        # set to None if developer_website (nullable) is None
        # and model_fields_set contains the field
        if self.developer_website is None and "developer_website" in self.model_fields_set:
            _dict['developer_website'] = None

        # set to None if version (nullable) is None
        # and model_fields_set contains the field
        if self.version is None and "version" in self.model_fields_set:
            _dict['version'] = None

        # set to None if minimum_os_version (nullable) is None
        # and model_fields_set contains the field
        if self.minimum_os_version is None and "minimum_os_version" in self.model_fields_set:
            _dict['minimum_os_version'] = None

        # set to None if size (nullable) is None
        # and model_fields_set contains the field
        if self.size is None and "size" in self.model_fields_set:
            _dict['size'] = None

        # set to None if released_date (nullable) is None
        # and model_fields_set contains the field
        if self.released_date is None and "released_date" in self.model_fields_set:
            _dict['released_date'] = None

        # set to None if last_update_date (nullable) is None
        # and model_fields_set contains the field
        if self.last_update_date is None and "last_update_date" in self.model_fields_set:
            _dict['last_update_date'] = None

        # set to None if update_notes (nullable) is None
        # and model_fields_set contains the field
        if self.update_notes is None and "update_notes" in self.model_fields_set:
            _dict['update_notes'] = None

        # set to None if images (nullable) is None
        # and model_fields_set contains the field
        if self.images is None and "images" in self.model_fields_set:
            _dict['images'] = None

        # set to None if videos (nullable) is None
        # and model_fields_set contains the field
        if self.videos is None and "videos" in self.model_fields_set:
            _dict['videos'] = None

        # set to None if similar_apps (nullable) is None
        # and model_fields_set contains the field
        if self.similar_apps is None and "similar_apps" in self.model_fields_set:
            _dict['similar_apps'] = None

        # set to None if more_apps_by_developer (nullable) is None
        # and model_fields_set contains the field
        if self.more_apps_by_developer is None and "more_apps_by_developer" in self.model_fields_set:
            _dict['more_apps_by_developer'] = None

        # set to None if genres (nullable) is None
        # and model_fields_set contains the field
        if self.genres is None and "genres" in self.model_fields_set:
            _dict['genres'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataAppGooglePlayInfoOrganicSerpElementItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "position": obj.get("position"),
            "app_id": obj.get("app_id"),
            "title": obj.get("title"),
            "url": obj.get("url"),
            "icon": obj.get("icon"),
            "description": obj.get("description"),
            "reviews_count": obj.get("reviews_count"),
            "rating": RatingInfo.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "price": PriceInfo.from_dict(obj["price"]) if obj.get("price") is not None else None,
            "is_free": obj.get("is_free"),
            "main_category": obj.get("main_category"),
            "installs": obj.get("installs"),
            "installs_count": obj.get("installs_count"),
            "developer": obj.get("developer"),
            "developer_id": obj.get("developer_id"),
            "developer_url": obj.get("developer_url"),
            "developer_email": obj.get("developer_email"),
            "developer_address": obj.get("developer_address"),
            "developer_website": obj.get("developer_website"),
            "version": obj.get("version"),
            "minimum_os_version": obj.get("minimum_os_version"),
            "size": obj.get("size"),
            "released_date": obj.get("released_date"),
            "last_update_date": obj.get("last_update_date"),
            "update_notes": obj.get("update_notes"),
            "images": obj.get("images"),
            "videos": obj.get("videos"),
            "similar_apps": [AppsInfo.from_dict(_item) for _item in obj["similar_apps"]] if obj.get("similar_apps") is not None else None,
            "more_apps_by_developer": [AppsInfo.from_dict(_item) for _item in obj["more_apps_by_developer"]] if obj.get("more_apps_by_developer") is not None else None,
            "genres": obj.get("genres"),
            "tags": obj.get("tags")
        })
        return _obj



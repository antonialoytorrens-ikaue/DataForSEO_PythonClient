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
from dataforseo_client.models.base_on_page_resource_item_info import BaseOnPageResourceItemInfo
from dataforseo_client.models.cache_control import CacheControl
from dataforseo_client.models.fetch_timing import FetchTiming
from dataforseo_client.models.last_modified import LastModified
from dataforseo_client.models.on_page_resource_issue_info import OnPageResourceIssueInfo
from dataforseo_client.models.resource_meta_info import ResourceMetaInfo
from typing import Optional, Set
from typing_extensions import Self

class OnPageStylesheetResourceElementItem(BaseOnPageResourceItemInfo):
    """
    OnPageStylesheetResourceElementItem
    """ # noqa: E501
    meta: Optional[ResourceMetaInfo] = None
    status_code: Optional[StrictInt] = Field(default=None, description="status code of the page where a given resource is located")
    location: Optional[StrictStr] = Field(default=None, description="location header indicates the URL to redirect a page to")
    url: Optional[StrictStr] = Field(default=None, description="resource URL")
    size: Optional[StrictInt] = Field(default=None, description="resource size indicates the size of a given resource measured in bytes")
    encoded_size: Optional[StrictInt] = Field(default=None, description="resource size after encoding indicates the size of the encoded resource measured in bytes")
    total_transfer_size: Optional[StrictInt] = Field(default=None, description="compressed resource size indicates the compressed size of a given resource in bytes")
    fetch_time: Optional[StrictStr] = Field(default=None, description="date and time when a resource was fetched in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2021-02-17 13:54:15 +00:00")
    fetch_timing: Optional[FetchTiming] = None
    cache_control: Optional[CacheControl] = None
    checks: Optional[Dict[str, Optional[StrictBool]]] = Field(default=None, description="resource check-ups contents of the array depend on the resource_type")
    resource_errors: Optional[OnPageResourceIssueInfo] = None
    content_encoding: Optional[StrictStr] = Field(default=None, description="type of encoding")
    media_type: Optional[StrictStr] = Field(default=None, description="types of media used to display a resource")
    accept_type: Optional[StrictStr] = Field(default=None, description="indicates the expected type of resource for example, if \"resource_type\": \"broken\", accept_type will indicate the type of the broken resource possible values: any, none, image, sitemap, robots, script, stylesheet, redirect, html, text, other, font")
    server: Optional[StrictStr] = Field(default=None, description="server version")
    last_modified: Optional[LastModified] = None
    initiator: Optional[StrictStr] = Field(default=None, description="resource initiator")
    duration_time: Optional[StrictInt] = Field(default=None, description="total time it takes until a browser receives a complete response from a server (in milliseconds)")
    fetch_start: Optional[StrictInt] = Field(default=None, description="time to start downloading the resource the amount of time the browser needs to start downloading a resource")
    fetch_end: Optional[StrictInt] = Field(default=None, description="time to complete downloading the resource the amount of time the browser needs to complete downloading a resource")
    is_render_blocking: Optional[StrictBool] = Field(default=None, description="indicates whether the resource blocks rendering")
    __properties: ClassVar[List[str]] = ["resource_type", "meta", "status_code", "location", "url", "size", "encoded_size", "total_transfer_size", "fetch_time", "fetch_timing", "cache_control", "checks", "resource_errors", "content_encoding", "media_type", "accept_type", "server", "last_modified", "initiator", "duration_time", "fetch_start", "fetch_end", "is_render_blocking"]

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
        """Create an instance of OnPageStylesheetResourceElementItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict['meta'] = self.meta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fetch_timing
        if self.fetch_timing:
            _dict['fetch_timing'] = self.fetch_timing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cache_control
        if self.cache_control:
            _dict['cache_control'] = self.cache_control.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resource_errors
        if self.resource_errors:
            _dict['resource_errors'] = self.resource_errors.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_modified
        if self.last_modified:
            _dict['last_modified'] = self.last_modified.to_dict()
        # set to None if resource_type (nullable) is None
        # and model_fields_set contains the field
        if self.resource_type is None and "resource_type" in self.model_fields_set:
            _dict['resource_type'] = None

        # set to None if status_code (nullable) is None
        # and model_fields_set contains the field
        if self.status_code is None and "status_code" in self.model_fields_set:
            _dict['status_code'] = None

        # set to None if location (nullable) is None
        # and model_fields_set contains the field
        if self.location is None and "location" in self.model_fields_set:
            _dict['location'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if size (nullable) is None
        # and model_fields_set contains the field
        if self.size is None and "size" in self.model_fields_set:
            _dict['size'] = None

        # set to None if encoded_size (nullable) is None
        # and model_fields_set contains the field
        if self.encoded_size is None and "encoded_size" in self.model_fields_set:
            _dict['encoded_size'] = None

        # set to None if total_transfer_size (nullable) is None
        # and model_fields_set contains the field
        if self.total_transfer_size is None and "total_transfer_size" in self.model_fields_set:
            _dict['total_transfer_size'] = None

        # set to None if fetch_time (nullable) is None
        # and model_fields_set contains the field
        if self.fetch_time is None and "fetch_time" in self.model_fields_set:
            _dict['fetch_time'] = None

        # set to None if checks (nullable) is None
        # and model_fields_set contains the field
        if self.checks is None and "checks" in self.model_fields_set:
            _dict['checks'] = None

        # set to None if content_encoding (nullable) is None
        # and model_fields_set contains the field
        if self.content_encoding is None and "content_encoding" in self.model_fields_set:
            _dict['content_encoding'] = None

        # set to None if media_type (nullable) is None
        # and model_fields_set contains the field
        if self.media_type is None and "media_type" in self.model_fields_set:
            _dict['media_type'] = None

        # set to None if accept_type (nullable) is None
        # and model_fields_set contains the field
        if self.accept_type is None and "accept_type" in self.model_fields_set:
            _dict['accept_type'] = None

        # set to None if server (nullable) is None
        # and model_fields_set contains the field
        if self.server is None and "server" in self.model_fields_set:
            _dict['server'] = None

        # set to None if initiator (nullable) is None
        # and model_fields_set contains the field
        if self.initiator is None and "initiator" in self.model_fields_set:
            _dict['initiator'] = None

        # set to None if duration_time (nullable) is None
        # and model_fields_set contains the field
        if self.duration_time is None and "duration_time" in self.model_fields_set:
            _dict['duration_time'] = None

        # set to None if fetch_start (nullable) is None
        # and model_fields_set contains the field
        if self.fetch_start is None and "fetch_start" in self.model_fields_set:
            _dict['fetch_start'] = None

        # set to None if fetch_end (nullable) is None
        # and model_fields_set contains the field
        if self.fetch_end is None and "fetch_end" in self.model_fields_set:
            _dict['fetch_end'] = None

        # set to None if is_render_blocking (nullable) is None
        # and model_fields_set contains the field
        if self.is_render_blocking is None and "is_render_blocking" in self.model_fields_set:
            _dict['is_render_blocking'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OnPageStylesheetResourceElementItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "resource_type": obj.get("resource_type"),
            "meta": ResourceMetaInfo.from_dict(obj["meta"]) if obj.get("meta") is not None else None,
            "status_code": obj.get("status_code"),
            "location": obj.get("location"),
            "url": obj.get("url"),
            "size": obj.get("size"),
            "encoded_size": obj.get("encoded_size"),
            "total_transfer_size": obj.get("total_transfer_size"),
            "fetch_time": obj.get("fetch_time"),
            "fetch_timing": FetchTiming.from_dict(obj["fetch_timing"]) if obj.get("fetch_timing") is not None else None,
            "cache_control": CacheControl.from_dict(obj["cache_control"]) if obj.get("cache_control") is not None else None,
            "checks": obj.get("checks"),
            "resource_errors": OnPageResourceIssueInfo.from_dict(obj["resource_errors"]) if obj.get("resource_errors") is not None else None,
            "content_encoding": obj.get("content_encoding"),
            "media_type": obj.get("media_type"),
            "accept_type": obj.get("accept_type"),
            "server": obj.get("server"),
            "last_modified": LastModified.from_dict(obj["last_modified"]) if obj.get("last_modified") is not None else None,
            "initiator": obj.get("initiator"),
            "duration_time": obj.get("duration_time"),
            "fetch_start": obj.get("fetch_start"),
            "fetch_end": obj.get("fetch_end"),
            "is_render_blocking": obj.get("is_render_blocking")
        })
        return _obj



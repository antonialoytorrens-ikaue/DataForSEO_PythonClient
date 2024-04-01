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
from dataforseo_client.models.base_on_page_resource_item_info import BaseOnPageResourceItemInfo
from typing import Optional, Set
from typing_extensions import Self

class OnPageWaterfallItem(BaseModel):
    """
    OnPageWaterfallItem
    """ # noqa: E501
    page_url: Optional[StrictStr] = Field(default=None, description="URL of the page")
    time_to_interactive: Optional[StrictInt] = Field(default=None, description="Time To Interactive (TTI) metric the time it takes until the user can interact with a page (in milliseconds)")
    dom_complete: Optional[StrictInt] = Field(default=None, description="time to load resources the time it takes until the page and all of its subresources are downloaded (in milliseconds)")
    connection_time: Optional[StrictInt] = Field(default=None, description="time to connect to a server the time it takes until the connection with a server is established (in milliseconds)")
    time_to_secure_connection: Optional[StrictInt] = Field(default=None, description="time to establish a secure connection the time it takes until the secure connection with a server is established (in milliseconds)")
    request_sent_time: Optional[StrictInt] = Field(default=None, description="time to send a request to a server the time it takes until the request to a server is sent (in milliseconds)")
    waiting_time: Optional[StrictInt] = Field(default=None, description="time to first byte (TTFB) in milliseconds")
    download_time: Optional[StrictInt] = Field(default=None, description="time it takes for a browser to receive a response (in milliseconds)")
    duration_time: Optional[StrictInt] = Field(default=None, description="total time it takes until a browser receives a complete response from a server (in milliseconds)")
    fetch_start: Optional[StrictInt] = Field(default=None, description="time to start downloading the HTML resource the amount of time the browser needs to start downloading a page")
    fetch_end: Optional[StrictInt] = Field(default=None, description="time to complete downloading the HTML resource the amount of time the browser needs to complete downloading a page")
    resources: Optional[List[BaseOnPageResourceItemInfo]] = Field(default=None, description="resource-specific timing contains separate arrays with timing for each resource found on the page")
    __properties: ClassVar[List[str]] = ["page_url", "time_to_interactive", "dom_complete", "connection_time", "time_to_secure_connection", "request_sent_time", "waiting_time", "download_time", "duration_time", "fetch_start", "fetch_end", "resources"]

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
        """Create an instance of OnPageWaterfallItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in resources (list)
        _items = []
        if self.resources:
            for _item in self.resources:
                if _item:
                    _items.append(_item.to_dict())
            _dict['resources'] = _items
        # set to None if page_url (nullable) is None
        # and model_fields_set contains the field
        if self.page_url is None and "page_url" in self.model_fields_set:
            _dict['page_url'] = None

        # set to None if time_to_interactive (nullable) is None
        # and model_fields_set contains the field
        if self.time_to_interactive is None and "time_to_interactive" in self.model_fields_set:
            _dict['time_to_interactive'] = None

        # set to None if dom_complete (nullable) is None
        # and model_fields_set contains the field
        if self.dom_complete is None and "dom_complete" in self.model_fields_set:
            _dict['dom_complete'] = None

        # set to None if connection_time (nullable) is None
        # and model_fields_set contains the field
        if self.connection_time is None and "connection_time" in self.model_fields_set:
            _dict['connection_time'] = None

        # set to None if time_to_secure_connection (nullable) is None
        # and model_fields_set contains the field
        if self.time_to_secure_connection is None and "time_to_secure_connection" in self.model_fields_set:
            _dict['time_to_secure_connection'] = None

        # set to None if request_sent_time (nullable) is None
        # and model_fields_set contains the field
        if self.request_sent_time is None and "request_sent_time" in self.model_fields_set:
            _dict['request_sent_time'] = None

        # set to None if waiting_time (nullable) is None
        # and model_fields_set contains the field
        if self.waiting_time is None and "waiting_time" in self.model_fields_set:
            _dict['waiting_time'] = None

        # set to None if download_time (nullable) is None
        # and model_fields_set contains the field
        if self.download_time is None and "download_time" in self.model_fields_set:
            _dict['download_time'] = None

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

        # set to None if resources (nullable) is None
        # and model_fields_set contains the field
        if self.resources is None and "resources" in self.model_fields_set:
            _dict['resources'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OnPageWaterfallItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "page_url": obj.get("page_url"),
            "time_to_interactive": obj.get("time_to_interactive"),
            "dom_complete": obj.get("dom_complete"),
            "connection_time": obj.get("connection_time"),
            "time_to_secure_connection": obj.get("time_to_secure_connection"),
            "request_sent_time": obj.get("request_sent_time"),
            "waiting_time": obj.get("waiting_time"),
            "download_time": obj.get("download_time"),
            "duration_time": obj.get("duration_time"),
            "fetch_start": obj.get("fetch_start"),
            "fetch_end": obj.get("fetch_end"),
            "resources": [BaseOnPageResourceItemInfo.from_dict(_item) for _item in obj["resources"]] if obj.get("resources") is not None else None
        })
        return _obj



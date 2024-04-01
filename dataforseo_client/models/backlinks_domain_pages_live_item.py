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
from dataforseo_client.models.backlinks_page_meta import BacklinksPageMeta
from dataforseo_client.models.page_summary import PageSummary
from typing import Optional, Set
from typing_extensions import Self

class BacklinksDomainPagesLiveItem(BaseModel):
    """
    BacklinksDomainPagesLiveItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    main_domain: Optional[StrictStr] = Field(default=None, description="main website domain main website domain does not include subdomains")
    domain: Optional[StrictStr] = Field(default=None, description="domain domain where the page was found")
    tld: Optional[StrictStr] = Field(default=None, description="top-level domain top-level domain in the DNS root zone")
    page: Optional[StrictStr] = Field(default=None, description="page URL relevant page URL")
    ip: Optional[StrictStr] = Field(default=None, description="Internet Protocol address")
    first_visited: Optional[StrictStr] = Field(default=None, description="date and time of the first page visit date and time when our crawler visited this page for the first time in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2017-01-24 13:20:59 +00:00")
    prev_visited: Optional[StrictStr] = Field(default=None, description="previous to the most recent date when our crawler visited the page in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2017-01-24 13:20:59 +00:00")
    fetch_time: Optional[StrictStr] = Field(default=None, description="most recent date and time when our crawler visited the page in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2017-01-24 13:20:59 +00:00")
    status_code: Optional[StrictInt] = Field(default=None, description="HTTP status code of the page")
    location: Optional[StrictStr] = Field(default=None, description="location header indicates the URL to redirect a page to if exists")
    size: Optional[StrictInt] = Field(default=None, description="indicates the page size, in bytes")
    encoded_size: Optional[StrictInt] = Field(default=None, description="page size after encoding indicates the size of the encoded page, in bytes")
    content_encoding: Optional[StrictStr] = Field(default=None, description="type of encoding")
    media_type: Optional[StrictStr] = Field(default=None, description="types of media used to display a page")
    server: Optional[StrictStr] = Field(default=None, description="server version")
    meta: Optional[BacklinksPageMeta] = None
    page_summary: Optional[PageSummary] = None
    __properties: ClassVar[List[str]] = ["type", "main_domain", "domain", "tld", "page", "ip", "first_visited", "prev_visited", "fetch_time", "status_code", "location", "size", "encoded_size", "content_encoding", "media_type", "server", "meta", "page_summary"]

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
        """Create an instance of BacklinksDomainPagesLiveItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of page_summary
        if self.page_summary:
            _dict['page_summary'] = self.page_summary.to_dict()
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if main_domain (nullable) is None
        # and model_fields_set contains the field
        if self.main_domain is None and "main_domain" in self.model_fields_set:
            _dict['main_domain'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if tld (nullable) is None
        # and model_fields_set contains the field
        if self.tld is None and "tld" in self.model_fields_set:
            _dict['tld'] = None

        # set to None if page (nullable) is None
        # and model_fields_set contains the field
        if self.page is None and "page" in self.model_fields_set:
            _dict['page'] = None

        # set to None if ip (nullable) is None
        # and model_fields_set contains the field
        if self.ip is None and "ip" in self.model_fields_set:
            _dict['ip'] = None

        # set to None if first_visited (nullable) is None
        # and model_fields_set contains the field
        if self.first_visited is None and "first_visited" in self.model_fields_set:
            _dict['first_visited'] = None

        # set to None if prev_visited (nullable) is None
        # and model_fields_set contains the field
        if self.prev_visited is None and "prev_visited" in self.model_fields_set:
            _dict['prev_visited'] = None

        # set to None if fetch_time (nullable) is None
        # and model_fields_set contains the field
        if self.fetch_time is None and "fetch_time" in self.model_fields_set:
            _dict['fetch_time'] = None

        # set to None if status_code (nullable) is None
        # and model_fields_set contains the field
        if self.status_code is None and "status_code" in self.model_fields_set:
            _dict['status_code'] = None

        # set to None if location (nullable) is None
        # and model_fields_set contains the field
        if self.location is None and "location" in self.model_fields_set:
            _dict['location'] = None

        # set to None if size (nullable) is None
        # and model_fields_set contains the field
        if self.size is None and "size" in self.model_fields_set:
            _dict['size'] = None

        # set to None if encoded_size (nullable) is None
        # and model_fields_set contains the field
        if self.encoded_size is None and "encoded_size" in self.model_fields_set:
            _dict['encoded_size'] = None

        # set to None if content_encoding (nullable) is None
        # and model_fields_set contains the field
        if self.content_encoding is None and "content_encoding" in self.model_fields_set:
            _dict['content_encoding'] = None

        # set to None if media_type (nullable) is None
        # and model_fields_set contains the field
        if self.media_type is None and "media_type" in self.model_fields_set:
            _dict['media_type'] = None

        # set to None if server (nullable) is None
        # and model_fields_set contains the field
        if self.server is None and "server" in self.model_fields_set:
            _dict['server'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BacklinksDomainPagesLiveItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "main_domain": obj.get("main_domain"),
            "domain": obj.get("domain"),
            "tld": obj.get("tld"),
            "page": obj.get("page"),
            "ip": obj.get("ip"),
            "first_visited": obj.get("first_visited"),
            "prev_visited": obj.get("prev_visited"),
            "fetch_time": obj.get("fetch_time"),
            "status_code": obj.get("status_code"),
            "location": obj.get("location"),
            "size": obj.get("size"),
            "encoded_size": obj.get("encoded_size"),
            "content_encoding": obj.get("content_encoding"),
            "media_type": obj.get("media_type"),
            "server": obj.get("server"),
            "meta": BacklinksPageMeta.from_dict(obj["meta"]) if obj.get("meta") is not None else None,
            "page_summary": PageSummary.from_dict(obj["page_summary"]) if obj.get("page_summary") is not None else None
        })
        return _obj



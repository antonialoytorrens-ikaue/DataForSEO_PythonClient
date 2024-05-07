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

from pydantic import BaseModel, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.base_on_page_resource_item_info import BaseOnPageResourceItemInfo
from typing import Optional, Set
from typing_extensions import Self

class Pages(BaseModel):
    """
    Pages
    """ # noqa: E501
    similarity: Optional[StrictInt] = Field(default=None, description="content similarity score by default, the content is considered duplicate if the value is greater than or equals 6 can take values from 0 to 10")
    page: Optional[List[BaseOnPageResourceItemInfo]] = Field(default=None, description="information about the page with duplicate content")
    __properties: ClassVar[List[str]] = ["similarity", "page"]

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
        """Create an instance of Pages from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in page (list)
        _items = []
        if self.page:
            for _item in self.page:
                if _item:
                    _items.append(_item.to_dict())
            _dict['page'] = _items
        # set to None if similarity (nullable) is None
        # and model_fields_set contains the field
        if self.similarity is None and "similarity" in self.model_fields_set:
            _dict['similarity'] = None

        # set to None if page (nullable) is None
        # and model_fields_set contains the field
        if self.page is None and "page" in self.model_fields_set:
            _dict['page'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Pages from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "similarity": obj.get("similarity"),
            "page": [BaseOnPageResourceItemInfo.from_dict(_item) for _item in obj["page"]] if obj.get("page") is not None else None
        })
        return _obj



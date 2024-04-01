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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.work_day_info import WorkDayInfo
from typing import Optional, Set
from typing_extensions import Self

class WorkHours(BaseModel):
    """
    WorkHours
    """ # noqa: E501
    timetable: Optional[Dict[str, Optional[List[WorkDayInfo]]]] = Field(default=None, description="work hours timetable")
    current_status: Optional[StrictStr] = Field(default=None, description="current status of the establishment indicates whether the establishment is opened or closed")
    __properties: ClassVar[List[str]] = ["timetable", "current_status"]

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
        """Create an instance of WorkHours from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in timetable (dict of array)
        _field_dict_of_array = {}
        if self.timetable:
            for _key in self.timetable:
                if self.timetable[_key] is not None:
                    _field_dict_of_array[_key] = [
                        _item.to_dict() for _item in self.timetable[_key]
                    ]
            _dict['timetable'] = _field_dict_of_array
        # set to None if timetable (nullable) is None
        # and model_fields_set contains the field
        if self.timetable is None and "timetable" in self.model_fields_set:
            _dict['timetable'] = None

        # set to None if current_status (nullable) is None
        # and model_fields_set contains the field
        if self.current_status is None and "current_status" in self.model_fields_set:
            _dict['current_status'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WorkHours from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "timetable": dict(
                (_k,
                        [WorkDayInfo.from_dict(_item) for _item in _v]
                        if _v is not None
                        else None
                )
                for _k, _v in obj.get("timetable", {}).items()
            ),
            "current_status": obj.get("current_status")
        })
        return _obj



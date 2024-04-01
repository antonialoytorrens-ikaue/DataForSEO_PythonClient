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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from dataforseo_client.models.dataforseo_labs_google_related_keywords_live_result_info import DataforseoLabsGoogleRelatedKeywordsLiveResultInfo
from typing import Optional, Set
from typing_extensions import Self

class DataforseoLabsGoogleRelatedKeywordsLiveTaskInfo(BaseModel):
    """
    DataforseoLabsGoogleRelatedKeywordsLiveTaskInfo
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="task identifier unique task identifier in our system in the UUID format")
    status_code: Optional[StrictInt] = Field(default=None, description="status code of the task generated by DataForSEO, can be within the following range: 10000-60000 you can find the full list of the response codes here")
    status_message: Optional[StrictStr] = Field(default=None, description="informational message of the task you can find the full list of general informational messages here")
    time: Optional[StrictStr] = Field(default=None, description="execution time, seconds")
    cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="total tasks cost, USD")
    result_count: Optional[StrictInt] = Field(default=None, description="number of elements in the result array")
    path: Optional[List[Optional[StrictStr]]] = Field(default=None, description="URL path")
    data: Optional[Dict[str, Any]] = Field(default=None, description="contains the same parameters that you specified in the POST request")
    result: Optional[List[DataforseoLabsGoogleRelatedKeywordsLiveResultInfo]] = Field(default=None, description="array of results")
    __properties: ClassVar[List[str]] = ["id", "status_code", "status_message", "time", "cost", "result_count", "path", "data", "result"]

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
        """Create an instance of DataforseoLabsGoogleRelatedKeywordsLiveTaskInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in result (list)
        _items = []
        if self.result:
            for _item in self.result:
                if _item:
                    _items.append(_item.to_dict())
            _dict['result'] = _items
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if status_code (nullable) is None
        # and model_fields_set contains the field
        if self.status_code is None and "status_code" in self.model_fields_set:
            _dict['status_code'] = None

        # set to None if status_message (nullable) is None
        # and model_fields_set contains the field
        if self.status_message is None and "status_message" in self.model_fields_set:
            _dict['status_message'] = None

        # set to None if time (nullable) is None
        # and model_fields_set contains the field
        if self.time is None and "time" in self.model_fields_set:
            _dict['time'] = None

        # set to None if cost (nullable) is None
        # and model_fields_set contains the field
        if self.cost is None and "cost" in self.model_fields_set:
            _dict['cost'] = None

        # set to None if result_count (nullable) is None
        # and model_fields_set contains the field
        if self.result_count is None and "result_count" in self.model_fields_set:
            _dict['result_count'] = None

        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict['path'] = None

        # set to None if data (nullable) is None
        # and model_fields_set contains the field
        if self.data is None and "data" in self.model_fields_set:
            _dict['data'] = None

        # set to None if result (nullable) is None
        # and model_fields_set contains the field
        if self.result is None and "result" in self.model_fields_set:
            _dict['result'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataforseoLabsGoogleRelatedKeywordsLiveTaskInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "status_code": obj.get("status_code"),
            "status_message": obj.get("status_message"),
            "time": obj.get("time"),
            "cost": obj.get("cost"),
            "result_count": obj.get("result_count"),
            "path": obj.get("path"),
            "data": obj.get("data"),
            "result": [DataforseoLabsGoogleRelatedKeywordsLiveResultInfo.from_dict(_item) for _item in obj["result"]] if obj.get("result") is not None else None
        })
        return _obj



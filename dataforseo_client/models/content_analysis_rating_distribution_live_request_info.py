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
from typing import Optional, Set
from typing_extensions import Self

class ContentAnalysisRatingDistributionLiveRequestInfo(BaseModel):
    """
    ContentAnalysisRatingDistributionLiveRequestInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="target keyword required field UTF-8 encoding a keyword should be at least 3 characters long; the keywords will be converted to a lowercase format; Note: to match an exact phrase instead of a stand-alone keyword, use double quotes and backslashes; example: \"keyword\": \"\\\"tesla palo alto\\\"\"")
    keyword_fields: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="target keyword fields and target keywords optional field use this parameter to filter the dataset by keywords that certain fields should contain; fields you can specify: title, main_title, previous_title, snippet you can indicate several fields; Note: to match an exact phrase instead of a stand-alone keyword, use double quotes and backslashes; example: \"keyword_fields\": {     \"snippet\": \"\\\"logitech mouse\\\"\",     \"main_title\": \"sale\" }")
    page_type: Optional[List[StrictStr]] = Field(default=None, description="target page types optional field use this parameter to filter the dataset by page types possible values: \"ecommerce\", \"news\", \"blogs\", \"message-boards\", \"organization\"")
    internal_list_limit: Optional[StrictInt] = Field(default=None, description="maximum number of elements within internal arrays optional field you can use this field to limit the number of elements within the following arrays: top_domains text_categories page_categories countries languages default value: 1 maximum value: 20")
    search_mode: Optional[StrictStr] = Field(default=None, description="results grouping type optional field possible grouping types: as_is – returns all citations for the target keyword one_per_domain – returns one citation of the keyword per domain default value: as_is")
    positive_connotation_threshold: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="positive connotation threshold optional field specified as the probability index threshold for positive sentiment related to the citation content if you specify this field, connotation_types object in the response will only contain data on citations with positive sentiment probability more than or equal to the specified value possible values: from 0 to 1 default value: 0.4")
    sentiments_connotation_threshold: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="sentiment connotation threshold optional field specified as the probability index threshold for sentiment connotations related to the citation content if you specify this field, sentiment_connotations object in the response will only contain data on citations where the probability per each sentiment is more than or equal to the specified value possible values: from 0 to 1 default value: 0.4")
    initial_dataset_filters: Optional[List[Optional[Dict[str, Any]]]] = Field(default=None, description="initial dataset filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: regex, <, <=, >, >=, =, <>, in, not_in, like,not_like, has, has_not you can use the % operator with like and not_like to match any string of zero or more characters example: [\"domain\",\"<>\", \"logitech.com\"] [[\"domain\",\"<>\",\"logitech.com\"],\"and\",[\"content_info.connotation_types.negative\",\">\",1000]] [[\"domain\",\"<>\",\"logitech.com\"]], \"and\", [[\"content_info.connotation_types.negative\",\">\",1000], \"or\", [\"content_info.text_category\",\"has\",10994]]] for more information about filters, please refer to Content Analysis API – Filters")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = ["keyword", "keyword_fields", "page_type", "internal_list_limit", "search_mode", "positive_connotation_threshold", "sentiments_connotation_threshold", "initial_dataset_filters", "tag"]

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
        """Create an instance of ContentAnalysisRatingDistributionLiveRequestInfo from a JSON string"""
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
        # set to None if keyword_fields (nullable) is None
        # and model_fields_set contains the field
        if self.keyword_fields is None and "keyword_fields" in self.model_fields_set:
            _dict['keyword_fields'] = None

        # set to None if page_type (nullable) is None
        # and model_fields_set contains the field
        if self.page_type is None and "page_type" in self.model_fields_set:
            _dict['page_type'] = None

        # set to None if internal_list_limit (nullable) is None
        # and model_fields_set contains the field
        if self.internal_list_limit is None and "internal_list_limit" in self.model_fields_set:
            _dict['internal_list_limit'] = None

        # set to None if search_mode (nullable) is None
        # and model_fields_set contains the field
        if self.search_mode is None and "search_mode" in self.model_fields_set:
            _dict['search_mode'] = None

        # set to None if positive_connotation_threshold (nullable) is None
        # and model_fields_set contains the field
        if self.positive_connotation_threshold is None and "positive_connotation_threshold" in self.model_fields_set:
            _dict['positive_connotation_threshold'] = None

        # set to None if sentiments_connotation_threshold (nullable) is None
        # and model_fields_set contains the field
        if self.sentiments_connotation_threshold is None and "sentiments_connotation_threshold" in self.model_fields_set:
            _dict['sentiments_connotation_threshold'] = None

        # set to None if initial_dataset_filters (nullable) is None
        # and model_fields_set contains the field
        if self.initial_dataset_filters is None and "initial_dataset_filters" in self.model_fields_set:
            _dict['initial_dataset_filters'] = None

        # set to None if tag (nullable) is None
        # and model_fields_set contains the field
        if self.tag is None and "tag" in self.model_fields_set:
            _dict['tag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ContentAnalysisRatingDistributionLiveRequestInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keyword": obj.get("keyword"),
            "keyword_fields": obj.get("keyword_fields"),
            "page_type": obj.get("page_type"),
            "internal_list_limit": obj.get("internal_list_limit"),
            "search_mode": obj.get("search_mode"),
            "positive_connotation_threshold": obj.get("positive_connotation_threshold"),
            "sentiments_connotation_threshold": obj.get("sentiments_connotation_threshold"),
            "initial_dataset_filters": obj.get("initial_dataset_filters"),
            "tag": obj.get("tag")
        })
        return _obj



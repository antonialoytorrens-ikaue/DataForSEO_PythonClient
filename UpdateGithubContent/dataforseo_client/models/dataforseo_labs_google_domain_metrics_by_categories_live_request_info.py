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

from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class DataforseoLabsGoogleDomainMetricsByCategoriesLiveRequestInfo(BaseModel):
    """
    DataforseoLabsGoogleDomainMetricsByCategoriesLiveRequestInfo
    """ # noqa: E501
    category_codes: Optional[List[StrictStr]] = Field(default=None, description="product and service categories required field The maximum number of categories you can specify: 5 you can download the full list of possible categories")
    first_date: Optional[StrictStr] = Field(default=None, description="first date of comparison period required field first date for which domain metrics will be provided; date format: \"yyyy-mm-dd\"; example: \"2021-06-01\"; the list available dates is available through the available history endpoint; Note: first_date cannot be greater than today’s date; Also note: the dates specified in first_date and second_date cannot point to the same month of the same year; you can specify the dates in any order: first_date can be greater than second_date and vice versa; minimum date: \"2020-10-01\"")
    second_date: Optional[StrictStr] = Field(default=None, description="second date of comparison period required field second date for which domain metrics will be provided; date format: \"yyyy-mm-dd\"; example: \"2021-10-01\"; the list available dates is available through the available history endpoint; Note: second_date cannot be greater than today’s date; Also note: the dates specified in first_date and second_date cannot point to the same month of the same year; you can specify the dates in any order: second_date can be greater than first_date and vice versa; minimum date: \"2020-10-01\"")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of the location required field if you don’t specify location_code Note: it is required to specify either location_name or location_code; you can receive the list of available locations with their location_name by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; example: United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description="unique location identifier required field if you don’t specify location_name Note: it is required to specify either location_name or location_code; you can receive the list of available locations with their location_code by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; example: 2840")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of the language required field if you don’t specify language_code Note: it is required to specify either language_name or language_code; you can receive the list of available languages with their language_name by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; example: English")
    language_code: Optional[StrictStr] = Field(default=None, description="unique language identifier required field if you don’t specify language_name Note: it is required to specify either language_name or language_code; you can receive the list of available languages with their language_code by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; example: en")
    item_types: Optional[List[StrictStr]] = Field(default=None, description="display results by item type optional field indicates the type of search results included in the response; Note: if the item_types array contains item types that are different from the organic object, the results will be ordered by the first item type in the array; you will not be able to sort and filter results by the types of search results not included in the response; possible values: [\"organic\", \"paid\", \"featured_snippet\", \"local_pack\"]; default value: [\"organic\", \"paid\"]")
    top_categories_count: Optional[StrictInt] = Field(default=None, description="number of additional domain categories optional field by using this parameter, you can receive domains relevant to additional categories that are not specified in category_codes above; to learn more about the parameter, please refer to this help center article; by default, top_categories_count is equal to the number of categories specified in the category_codes array; Note: top_categories_count cannot be less than the number of categories in the category_codes array; maximum value: 5")
    include_subdomains: Optional[StrictBool] = Field(default=None, description="return subdomains in the API response optional field if false, the API response will contain main_domain only; if true, the API will return main_domain plus its subdomains (if available); default value: true")
    etv_min: Optional[StrictInt] = Field(default=None, description="minimum current organic ETV of the domain optional field if specified, the API will return only domains with organic_etv greater than the specified value")
    etv_max: Optional[StrictInt] = Field(default=None, description="maximum current organic ETV of the domain optional field if specified, the API will return only domains with organic_etv lesser than the specified value")
    correlate: Optional[StrictBool] = Field(default=None, description="correlate data with previously obtained datasets optional field default value: true; if you use this parameter, our system will correlate data you obtain now with previously obtained datasets; this parameter is intended to mitigate any inconsistencies that may result from changes to our database; Note: we do not recommend setting correlate to false")
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of domains in the results array optional field default value: 100; maximum value: 1000")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the results array of returned domains optional field default value: 0; if you specify the 10 value, the first ten domains in the results array will be omitted and the data will be provided for the successive domains")
    filters: Optional[List[Optional[Dict[str, Any]]]] = Field(default=None, description="array of results filtering parameters optional field you can add several filters at once (8 filters maximum); you should set a logical operator and, or between the conditions the following operators are supported: regex, <, <=, >, >=, =, <>, in, not_in, like, not_like; you can use the % operator with like and not_like to match any string of zero or more characters; example: [\"metrics_history.202110.organic.pos_1\", \">\", 15]; for more information about filters, please refer to Dataforseo Labs – Filters or this help center guide")
    order_by: Optional[List[StrictStr]] = Field(default=None, description="results sorting rules optional field you can use the same values as in the filters array to sort the results; default rule: [\"organic_etv,desc\"]; possible sorting types: asc – results will be sorted in ascending order desc – results will be sorted in descending order; you should use a comma to set up a sorting type; example: [\"organic_count,desc\"]; note that you can set no more than three sorting rules in a single request; you should use a comma to separate several sorting rules; example: [\"organic_etv,desc\",\"organic_count,asc\"]")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier optional field the character limit is 255; you can use this parameter to identify the task and match it with the result; you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = ["category_codes", "first_date", "second_date", "location_name", "location_code", "language_name", "language_code", "item_types", "top_categories_count", "include_subdomains", "etv_min", "etv_max", "correlate", "limit", "offset", "filters", "order_by", "tag"]

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
        """Create an instance of DataforseoLabsGoogleDomainMetricsByCategoriesLiveRequestInfo from a JSON string"""
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
        # set to None if location_name (nullable) is None
        # and model_fields_set contains the field
        if self.location_name is None and "location_name" in self.model_fields_set:
            _dict['location_name'] = None

        # set to None if location_code (nullable) is None
        # and model_fields_set contains the field
        if self.location_code is None and "location_code" in self.model_fields_set:
            _dict['location_code'] = None

        # set to None if language_name (nullable) is None
        # and model_fields_set contains the field
        if self.language_name is None and "language_name" in self.model_fields_set:
            _dict['language_name'] = None

        # set to None if language_code (nullable) is None
        # and model_fields_set contains the field
        if self.language_code is None and "language_code" in self.model_fields_set:
            _dict['language_code'] = None

        # set to None if item_types (nullable) is None
        # and model_fields_set contains the field
        if self.item_types is None and "item_types" in self.model_fields_set:
            _dict['item_types'] = None

        # set to None if top_categories_count (nullable) is None
        # and model_fields_set contains the field
        if self.top_categories_count is None and "top_categories_count" in self.model_fields_set:
            _dict['top_categories_count'] = None

        # set to None if include_subdomains (nullable) is None
        # and model_fields_set contains the field
        if self.include_subdomains is None and "include_subdomains" in self.model_fields_set:
            _dict['include_subdomains'] = None

        # set to None if etv_min (nullable) is None
        # and model_fields_set contains the field
        if self.etv_min is None and "etv_min" in self.model_fields_set:
            _dict['etv_min'] = None

        # set to None if etv_max (nullable) is None
        # and model_fields_set contains the field
        if self.etv_max is None and "etv_max" in self.model_fields_set:
            _dict['etv_max'] = None

        # set to None if correlate (nullable) is None
        # and model_fields_set contains the field
        if self.correlate is None and "correlate" in self.model_fields_set:
            _dict['correlate'] = None

        # set to None if limit (nullable) is None
        # and model_fields_set contains the field
        if self.limit is None and "limit" in self.model_fields_set:
            _dict['limit'] = None

        # set to None if offset (nullable) is None
        # and model_fields_set contains the field
        if self.offset is None and "offset" in self.model_fields_set:
            _dict['offset'] = None

        # set to None if filters (nullable) is None
        # and model_fields_set contains the field
        if self.filters is None and "filters" in self.model_fields_set:
            _dict['filters'] = None

        # set to None if order_by (nullable) is None
        # and model_fields_set contains the field
        if self.order_by is None and "order_by" in self.model_fields_set:
            _dict['order_by'] = None

        # set to None if tag (nullable) is None
        # and model_fields_set contains the field
        if self.tag is None and "tag" in self.model_fields_set:
            _dict['tag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataforseoLabsGoogleDomainMetricsByCategoriesLiveRequestInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "category_codes": obj.get("category_codes"),
            "first_date": obj.get("first_date"),
            "second_date": obj.get("second_date"),
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "item_types": obj.get("item_types"),
            "top_categories_count": obj.get("top_categories_count"),
            "include_subdomains": obj.get("include_subdomains"),
            "etv_min": obj.get("etv_min"),
            "etv_max": obj.get("etv_max"),
            "correlate": obj.get("correlate"),
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "filters": obj.get("filters"),
            "order_by": obj.get("order_by"),
            "tag": obj.get("tag")
        })
        return _obj



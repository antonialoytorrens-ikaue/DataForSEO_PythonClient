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

from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class ContentGenerationGenerateTextLiveRequestInfo(BaseModel):
    """
    ContentGenerationGenerateTextLiveRequestInfo
    """ # noqa: E501
    topic: Optional[StrictStr] = Field(default=None, description="main topic of the content to generate required field main topic for generating content; can contain from 1 to 50 tokens")
    word_count: Optional[StrictInt] = Field(default=None, description="number of words in content required field the number of tokens in the generated text; can take values from 1 to 1000")
    sub_topics: Optional[List[StrictStr]] = Field(default=None, description="secondary topics of the content to generate optional field secondary topics for generating content; can contain up to 10 terms; example: \"sub_topics\": [\"Apple\",\"Pixar\",\"Amazing Products\"]")
    description: Optional[StrictStr] = Field(default=None, description="meta description of the content to generate optional field can contain from 1 to 1000 tokens learn more about this parameter on our help center")
    meta_keywords: Optional[List[StrictStr]] = Field(default=None, description="keywords for the content to generate optional field can contain up to 10 terms; learn more about this parameter on our help center example: \"meta_keywords\": [\"iPhone\",\"sell\",\"CEO\"]")
    creativity_index: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="creativity of content generation optional field the randomness of the selection of equally probable subsequent tokens; can take values from 0 to 1 default value: 0.8 learn more about this parameter on our help center")
    include_conclusion: Optional[StrictBool] = Field(default=None, description="include conclusion in generated text optional field if set to true, generated content will include a logical conclusion")
    supplement_token: Optional[StrictStr] = Field(default=None, description="token for generating subsequent results optional field provided in the identical filed of the response to each request; you can use this parameter to continue the generation of text from the initial response supplement_token values are unique for each subsequent task")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = ["topic", "word_count", "sub_topics", "description", "meta_keywords", "creativity_index", "include_conclusion", "supplement_token", "tag"]

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
        """Create an instance of ContentGenerationGenerateTextLiveRequestInfo from a JSON string"""
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
        # set to None if sub_topics (nullable) is None
        # and model_fields_set contains the field
        if self.sub_topics is None and "sub_topics" in self.model_fields_set:
            _dict['sub_topics'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if meta_keywords (nullable) is None
        # and model_fields_set contains the field
        if self.meta_keywords is None and "meta_keywords" in self.model_fields_set:
            _dict['meta_keywords'] = None

        # set to None if creativity_index (nullable) is None
        # and model_fields_set contains the field
        if self.creativity_index is None and "creativity_index" in self.model_fields_set:
            _dict['creativity_index'] = None

        # set to None if include_conclusion (nullable) is None
        # and model_fields_set contains the field
        if self.include_conclusion is None and "include_conclusion" in self.model_fields_set:
            _dict['include_conclusion'] = None

        # set to None if supplement_token (nullable) is None
        # and model_fields_set contains the field
        if self.supplement_token is None and "supplement_token" in self.model_fields_set:
            _dict['supplement_token'] = None

        # set to None if tag (nullable) is None
        # and model_fields_set contains the field
        if self.tag is None and "tag" in self.model_fields_set:
            _dict['tag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ContentGenerationGenerateTextLiveRequestInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "topic": obj.get("topic"),
            "word_count": obj.get("word_count"),
            "sub_topics": obj.get("sub_topics"),
            "description": obj.get("description"),
            "meta_keywords": obj.get("meta_keywords"),
            "creativity_index": obj.get("creativity_index"),
            "include_conclusion": obj.get("include_conclusion"),
            "supplement_token": obj.get("supplement_token"),
            "tag": obj.get("tag")
        })
        return _obj



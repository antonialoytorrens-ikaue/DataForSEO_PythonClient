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

from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class QuestionsAndAnswersElement(BaseModel):
    """
    QuestionsAndAnswersElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    url: Optional[StrictStr] = Field(default=None, description="URL")
    question_text: Optional[StrictStr] = Field(default=None, description="question included in the item")
    answer_text: Optional[StrictStr] = Field(default=None, description="answer included in the item")
    source: Optional[StrictStr] = Field(default=None, description="source of the element indicates the source of information included in the top_stories_element")
    domain: Optional[StrictStr] = Field(default=None, description="website domain")
    votes: Optional[StrictInt] = Field(default=None, description="answer upvotes from the source")
    __properties: ClassVar[List[str]] = ["type", "url", "question_text", "answer_text", "source", "domain", "votes"]

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
        """Create an instance of QuestionsAndAnswersElement from a JSON string"""
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
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if question_text (nullable) is None
        # and model_fields_set contains the field
        if self.question_text is None and "question_text" in self.model_fields_set:
            _dict['question_text'] = None

        # set to None if answer_text (nullable) is None
        # and model_fields_set contains the field
        if self.answer_text is None and "answer_text" in self.model_fields_set:
            _dict['answer_text'] = None

        # set to None if source (nullable) is None
        # and model_fields_set contains the field
        if self.source is None and "source" in self.model_fields_set:
            _dict['source'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if votes (nullable) is None
        # and model_fields_set contains the field
        if self.votes is None and "votes" in self.model_fields_set:
            _dict['votes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QuestionsAndAnswersElement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "url": obj.get("url"),
            "question_text": obj.get("question_text"),
            "answer_text": obj.get("answer_text"),
            "source": obj.get("source"),
            "domain": obj.get("domain"),
            "votes": obj.get("votes")
        })
        return _obj



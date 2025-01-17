# coding: utf-8

"""
    clevermaps-client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, conlist, constr, validator
from openapi_client.models.additional_series_link_dto import AdditionalSeriesLinkDTO
from openapi_client.models.annotation_link_dto import AnnotationLinkDTO

class TimeSeriesDTO(BaseModel):
    """
    TimeSeriesDTO
    """
    type: constr(strict=True) = Field(...)
    title: Optional[constr(strict=True, max_length=255)] = None
    indicator: Optional[constr(strict=True)] = None
    collapsed: Optional[StrictBool] = None
    visualized: Optional[StrictBool] = None
    default_period: Optional[constr(strict=True)] = Field(default=None, alias="defaultPeriod")
    additional_series: Optional[conlist(AdditionalSeriesLinkDTO)] = Field(default=None, alias="additionalSeries")
    annotations: Optional[conlist(AnnotationLinkDTO)] = None
    __properties = ["type", "title", "indicator", "collapsed", "visualized", "defaultPeriod", "additionalSeries", "annotations"]

    @validator('type')
    def type_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^timeSeries$", value):
            raise ValueError(r"must validate the regular expression /^timeSeries$/")
        return value

    @validator('indicator')
    def indicator_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\/rest\/projects\/(\$projectId|[a-z0-9]{16})\/md\/indicators(\?name=[a-z0-9_-]+|\/[a-z0-9]+)$", value):
            raise ValueError(r"must validate the regular expression /^\/rest\/projects\/(\$projectId|[a-z0-9]{16})\/md\/indicators(\?name=[a-z0-9_-]+|\/[a-z0-9]+)$/")
        return value

    @validator('default_period')
    def default_period_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\/rest\/projects\/(\$projectId|[a-z0-9]{16})\/md\/datasets(\?name=[a-z0-9_-]+|\/[a-z0-9]+)$", value):
            raise ValueError(r"must validate the regular expression /^\/rest\/projects\/(\$projectId|[a-z0-9]{16})\/md\/datasets(\?name=[a-z0-9_-]+|\/[a-z0-9]+)$/")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TimeSeriesDTO:
        """Create an instance of TimeSeriesDTO from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in additional_series (list)
        _items = []
        if self.additional_series:
            for _item in self.additional_series:
                if _item:
                    _items.append(_item.to_dict())
            _dict['additionalSeries'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in annotations (list)
        _items = []
        if self.annotations:
            for _item in self.annotations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['annotations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TimeSeriesDTO:
        """Create an instance of TimeSeriesDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TimeSeriesDTO.parse_obj(obj)

        _obj = TimeSeriesDTO.parse_obj({
            "type": obj.get("type"),
            "title": obj.get("title"),
            "indicator": obj.get("indicator"),
            "collapsed": obj.get("collapsed"),
            "visualized": obj.get("visualized"),
            "default_period": obj.get("defaultPeriod"),
            "additional_series": [AdditionalSeriesLinkDTO.from_dict(_item) for _item in obj.get("additionalSeries")] if obj.get("additionalSeries") is not None else None,
            "annotations": [AnnotationLinkDTO.from_dict(_item) for _item in obj.get("annotations")] if obj.get("annotations") is not None else None
        })
        return _obj


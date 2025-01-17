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


from typing import Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, constr, validator
from openapi_client.models.format_dto import FormatDTO

class VariableDTO(BaseModel):
    """
    VariableDTO
    """
    name: constr(strict=True) = Field(...)
    title: constr(strict=True, max_length=255, min_length=1) = Field(...)
    min_value: Union[StrictFloat, StrictInt] = Field(default=..., alias="minValue")
    max_value: Union[StrictFloat, StrictInt] = Field(default=..., alias="maxValue")
    default_value: Union[StrictFloat, StrictInt] = Field(default=..., alias="defaultValue")
    format: FormatDTO = Field(...)
    __properties = ["name", "title", "minValue", "maxValue", "defaultValue", "format"]

    @validator('name')
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-z][a-z0-9_-]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-z][a-z0-9_-]*$/")
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
    def from_json(cls, json_str: str) -> VariableDTO:
        """Create an instance of VariableDTO from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of format
        if self.format:
            _dict['format'] = self.format.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VariableDTO:
        """Create an instance of VariableDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VariableDTO.parse_obj(obj)

        _obj = VariableDTO.parse_obj({
            "name": obj.get("name"),
            "title": obj.get("title"),
            "min_value": obj.get("minValue"),
            "max_value": obj.get("maxValue"),
            "default_value": obj.get("defaultValue"),
            "format": FormatDTO.from_dict(obj.get("format")) if obj.get("format") is not None else None
        })
        return _obj



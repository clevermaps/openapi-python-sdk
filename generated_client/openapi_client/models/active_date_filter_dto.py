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



from pydantic import BaseModel, Field, StrictStr, constr, validator
from openapi_client.models.default_values_date_dto import DefaultValuesDateDTO

class ActiveDateFilterDTO(BaseModel):
    """
    ActiveDateFilterDTO
    """
    default_values: DefaultValuesDateDTO = Field(default=..., alias="defaultValues")
    type: constr(strict=True) = Field(...)
    var_property: StrictStr = Field(default=..., alias="property")
    __properties = ["defaultValues", "type", "property"]

    @validator('type')
    def type_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^date$", value):
            raise ValueError(r"must validate the regular expression /^date$/")
        return value

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('date'):
            raise ValueError("must be one of enum values ('date')")
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
    def from_json(cls, json_str: str) -> ActiveDateFilterDTO:
        """Create an instance of ActiveDateFilterDTO from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of default_values
        if self.default_values:
            _dict['defaultValues'] = self.default_values.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ActiveDateFilterDTO:
        """Create an instance of ActiveDateFilterDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ActiveDateFilterDTO.parse_obj(obj)

        _obj = ActiveDateFilterDTO.parse_obj({
            "default_values": DefaultValuesDateDTO.from_dict(obj.get("defaultValues")) if obj.get("defaultValues") is not None else None,
            "type": obj.get("type"),
            "var_property": obj.get("property")
        })
        return _obj



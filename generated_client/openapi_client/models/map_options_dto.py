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


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conint, validator
from openapi_client.models.center_dto import CenterDTO
from openapi_client.models.map_options_dto_custom_tile_layer import MapOptionsDTOCustomTileLayer

class MapOptionsDTO(BaseModel):
    """
    MapOptionsDTO
    """
    center: Optional[CenterDTO] = None
    zoom: Optional[StrictInt] = None
    min_zoom: Optional[conint(strict=True, ge=0)] = Field(default=None, alias="minZoom")
    max_zoom: Optional[StrictInt] = Field(default=None, alias="maxZoom")
    tile_layer_menu: Optional[StrictBool] = Field(default=None, alias="tileLayerMenu")
    tile_layer: Optional[StrictStr] = Field(default=None, alias="tileLayer")
    custom_tile_layer: Optional[MapOptionsDTOCustomTileLayer] = Field(default=None, alias="customTileLayer")
    __properties = ["center", "zoom", "minZoom", "maxZoom", "tileLayerMenu", "tileLayer", "customTileLayer"]

    @validator('tile_layer')
    def tile_layer_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('mapbox', 'mapboxStreets', 'mapboxOutdoors', 'mapboxSatelliteStreets', 'mapboxLight', 'mapboxDark'):
            raise ValueError("must be one of enum values ('mapbox', 'mapboxStreets', 'mapboxOutdoors', 'mapboxSatelliteStreets', 'mapboxLight', 'mapboxDark')")
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
    def from_json(cls, json_str: str) -> MapOptionsDTO:
        """Create an instance of MapOptionsDTO from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of center
        if self.center:
            _dict['center'] = self.center.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_tile_layer
        if self.custom_tile_layer:
            _dict['customTileLayer'] = self.custom_tile_layer.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MapOptionsDTO:
        """Create an instance of MapOptionsDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MapOptionsDTO.parse_obj(obj)

        _obj = MapOptionsDTO.parse_obj({
            "center": CenterDTO.from_dict(obj.get("center")) if obj.get("center") is not None else None,
            "zoom": obj.get("zoom"),
            "min_zoom": obj.get("minZoom"),
            "max_zoom": obj.get("maxZoom"),
            "tile_layer_menu": obj.get("tileLayerMenu"),
            "tile_layer": obj.get("tileLayer"),
            "custom_tile_layer": MapOptionsDTOCustomTileLayer.from_dict(obj.get("customTileLayer")) if obj.get("customTileLayer") is not None else None
        })
        return _obj


# coding: utf-8

"""
    clevermaps-client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.map_options_dto_custom_tile_layer import MapOptionsDTOCustomTileLayer  # noqa: E501

class TestMapOptionsDTOCustomTileLayer(unittest.TestCase):
    """MapOptionsDTOCustomTileLayer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MapOptionsDTOCustomTileLayer:
        """Test MapOptionsDTOCustomTileLayer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MapOptionsDTOCustomTileLayer`
        """
        model = MapOptionsDTOCustomTileLayer()  # noqa: E501
        if include_optional:
            return MapOptionsDTOCustomTileLayer(
                url = 'mapbox://styles/jUR,rZ#UM/?R,Fp^l6$ARj',
                access_token = '0'
            )
        else:
            return MapOptionsDTOCustomTileLayer(
                url = 'mapbox://styles/jUR,rZ#UM/?R,Fp^l6$ARj',
                access_token = '0',
        )
        """

    def testMapOptionsDTOCustomTileLayer(self):
        """Test MapOptionsDTOCustomTileLayer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

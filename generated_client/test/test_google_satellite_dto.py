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

from openapi_client.models.google_satellite_dto import GoogleSatelliteDTO  # noqa: E501

class TestGoogleSatelliteDTO(unittest.TestCase):
    """GoogleSatelliteDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GoogleSatelliteDTO:
        """Test GoogleSatelliteDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GoogleSatelliteDTO`
        """
        model = GoogleSatelliteDTO()  # noqa: E501
        if include_optional:
            return GoogleSatelliteDTO(
                type = 'googleSatellite'
            )
        else:
            return GoogleSatelliteDTO(
        )
        """

    def testGoogleSatelliteDTO(self):
        """Test GoogleSatelliteDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
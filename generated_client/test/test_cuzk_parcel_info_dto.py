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

from openapi_client.models.cuzk_parcel_info_dto import CuzkParcelInfoDTO  # noqa: E501

class TestCuzkParcelInfoDTO(unittest.TestCase):
    """CuzkParcelInfoDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CuzkParcelInfoDTO:
        """Test CuzkParcelInfoDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CuzkParcelInfoDTO`
        """
        model = CuzkParcelInfoDTO()  # noqa: E501
        if include_optional:
            return CuzkParcelInfoDTO(
                type = 'cuzkParcelInfo'
            )
        else:
            return CuzkParcelInfoDTO(
        )
        """

    def testCuzkParcelInfoDTO(self):
        """Test CuzkParcelInfoDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
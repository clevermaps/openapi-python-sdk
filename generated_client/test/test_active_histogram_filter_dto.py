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

from openapi_client.models.active_histogram_filter_dto import ActiveHistogramFilterDTO  # noqa: E501

class TestActiveHistogramFilterDTO(unittest.TestCase):
    """ActiveHistogramFilterDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActiveHistogramFilterDTO:
        """Test ActiveHistogramFilterDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActiveHistogramFilterDTO`
        """
        model = ActiveHistogramFilterDTO()  # noqa: E501
        if include_optional:
            return ActiveHistogramFilterDTO(
                default_values = openapi_client.models.default_values_histogram_dto.DefaultValuesHistogramDTO(
                    values = [
                        1.337
                        ], 
                    null_filtered = True, ),
                type = 'histogram',
                var_property = '',
                format = openapi_client.models.format_dto.FormatDTO(
                    type = 'number', 
                    fraction = 0, 
                    symbol = '', )
            )
        else:
            return ActiveHistogramFilterDTO(
                default_values = openapi_client.models.default_values_histogram_dto.DefaultValuesHistogramDTO(
                    values = [
                        1.337
                        ], 
                    null_filtered = True, ),
                type = 'histogram',
                var_property = '',
        )
        """

    def testActiveHistogramFilterDTO(self):
        """Test ActiveHistogramFilterDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
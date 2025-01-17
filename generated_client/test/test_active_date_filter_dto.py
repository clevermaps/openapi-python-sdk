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

from openapi_client.models.active_date_filter_dto import ActiveDateFilterDTO  # noqa: E501

class TestActiveDateFilterDTO(unittest.TestCase):
    """ActiveDateFilterDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActiveDateFilterDTO:
        """Test ActiveDateFilterDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActiveDateFilterDTO`
        """
        model = ActiveDateFilterDTO()  # noqa: E501
        if include_optional:
            return ActiveDateFilterDTO(
                default_values = openapi_client.models.default_values_date_dto.DefaultValuesDateDTO(
                    start_date = null, 
                    end_date = null, ),
                type = 'date',
                var_property = ''
            )
        else:
            return ActiveDateFilterDTO(
                default_values = openapi_client.models.default_values_date_dto.DefaultValuesDateDTO(
                    start_date = null, 
                    end_date = null, ),
                type = 'date',
                var_property = '',
        )
        """

    def testActiveDateFilterDTO(self):
        """Test ActiveDateFilterDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

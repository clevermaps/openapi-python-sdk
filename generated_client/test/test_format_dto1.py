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

from openapi_client.models.format_dto1 import FormatDTO1  # noqa: E501

class TestFormatDTO1(unittest.TestCase):
    """FormatDTO1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FormatDTO1:
        """Test FormatDTO1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FormatDTO1`
        """
        model = FormatDTO1()  # noqa: E501
        if include_optional:
            return FormatDTO1(
                type = 'number',
                fraction = 0,
                symbol = ''
            )
        else:
            return FormatDTO1(
                type = 'number',
        )
        """

    def testFormatDTO1(self):
        """Test FormatDTO1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

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

from openapi_client.models.default_selected_dto import DefaultSelectedDTO  # noqa: E501

class TestDefaultSelectedDTO(unittest.TestCase):
    """DefaultSelectedDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DefaultSelectedDTO:
        """Test DefaultSelectedDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DefaultSelectedDTO`
        """
        model = DefaultSelectedDTO()  # noqa: E501
        if include_optional:
            return DefaultSelectedDTO(
                dataset = '/rest/projects/8q6zgckec0l3o4gi/md/datasets?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc',
                ids = [
                    null
                    ],
                coordinates = [
                    openapi_client.models.center_dto.CenterDTO(
                        lat = 1.337, 
                        lng = 1.337, )
                    ]
            )
        else:
            return DefaultSelectedDTO(
        )
        """

    def testDefaultSelectedDTO(self):
        """Test DefaultSelectedDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

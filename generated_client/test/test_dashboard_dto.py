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

from openapi_client.models.dashboard_dto import DashboardDTO  # noqa: E501

class TestDashboardDTO(unittest.TestCase):
    """DashboardDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DashboardDTO:
        """Test DashboardDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DashboardDTO`
        """
        model = DashboardDTO()  # noqa: E501
        if include_optional:
            return DashboardDTO(
                id = '',
                name = 'awat5ikwowtta-3mh2lcafqw3zhes',
                type = 'dataset',
                title = '0',
                description = '0',
                content = openapi_client.models.dashboard_content_dto.DashboardContentDTO(
                    block_rows = [
                        null
                        ], 
                    dataset_properties = [
                        openapi_client.models.dashboard_dataset_properties_dto.DashboardDatasetPropertiesDTO(
                            dataset = '/rest/projects/8q6zgckec0l3o4gi/md/datasets?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc', 
                            default_search = 'enable', 
                            feature_attributes = [
                                openapi_client.models.feature_attribute_dto.FeatureAttributeDTO(
                                    type = 'property', 
                                    value = '', 
                                    format = openapi_client.models.attribute_format_dto.AttributeFormatDTO(
                                        type = 'text', 
                                        fraction = 0, 
                                        symbol = '', ), 
                                    layout = 'primary', )
                                ], )
                        ], )
            )
        else:
            return DashboardDTO(
                name = 'awat5ikwowtta-3mh2lcafqw3zhes',
                content = openapi_client.models.dashboard_content_dto.DashboardContentDTO(
                    block_rows = [
                        null
                        ], 
                    dataset_properties = [
                        openapi_client.models.dashboard_dataset_properties_dto.DashboardDatasetPropertiesDTO(
                            dataset = '/rest/projects/8q6zgckec0l3o4gi/md/datasets?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc', 
                            default_search = 'enable', 
                            feature_attributes = [
                                openapi_client.models.feature_attribute_dto.FeatureAttributeDTO(
                                    type = 'property', 
                                    value = '', 
                                    format = openapi_client.models.attribute_format_dto.AttributeFormatDTO(
                                        type = 'text', 
                                        fraction = 0, 
                                        symbol = '', ), 
                                    layout = 'primary', )
                                ], )
                        ], ),
        )
        """

    def testDashboardDTO(self):
        """Test DashboardDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

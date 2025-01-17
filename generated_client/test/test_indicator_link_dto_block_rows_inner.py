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

from openapi_client.models.indicator_link_dto_block_rows_inner import IndicatorLinkDTOBlockRowsInner  # noqa: E501

class TestIndicatorLinkDTOBlockRowsInner(unittest.TestCase):
    """IndicatorLinkDTOBlockRowsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IndicatorLinkDTOBlockRowsInner:
        """Test IndicatorLinkDTOBlockRowsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IndicatorLinkDTOBlockRowsInner`
        """
        model = IndicatorLinkDTOBlockRowsInner()  # noqa: E501
        if include_optional:
            return IndicatorLinkDTOBlockRowsInner(
                type = 'timeSeries',
                title = '',
                description = '',
                split_property = '',
                attribute_style = '/rest/projects/8q6zgckec0l3o4gi/md/attributeStyles?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc',
                indicator = '/rest/projects/8q6zgckec0l3o4gi/md/indicators?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc',
                collapsed = True,
                visualized = True,
                filterable = True,
                hide_null_items = True,
                size_limit = 56,
                order_by = openapi_client.models.order_by_dto.OrderByDTO(
                    property = '', 
                    direction = 'asc', ),
                vertical = True,
                condensed = True,
                dual_property = '',
                dual_attribute_style = '/rest/projects/8q6zgckec0l3o4gi/md/attributeStyles?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc',
                label = '',
                default_dataset = '/rest/projects/8q6zgckec0l3o4gi/md/datasets?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc',
                default_layer = 'awat5ikwowtta-3mh2lcafqw3zhes',
                feature_type = 'granularity',
                direction = 'asc',
                default_period = '/rest/projects/8q6zgckec0l3o4gi/md/datasets?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc',
                additional_series = [
                    openapi_client.models.additional_series_link_dto.AdditionalSeriesLinkDTO(
                        indicator = '/rest/projects/8q6zgckec0l3o4gi/md/indicators?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc', )
                    ],
                annotations = [
                    openapi_client.models.annotation_link_dto.AnnotationLinkDTO(
                        dataset = '/rest/projects/8q6zgckec0l3o4gi/md/datasets?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc', )
                    ]
            )
        else:
            return IndicatorLinkDTOBlockRowsInner(
                type = 'timeSeries',
        )
        """

    def testIndicatorLinkDTOBlockRowsInner(self):
        """Test IndicatorLinkDTOBlockRowsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

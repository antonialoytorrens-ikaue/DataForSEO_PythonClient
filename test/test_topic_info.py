# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.topic_info import TopicInfo

class TestTopicInfo(unittest.TestCase):
    """TopicInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TopicInfo:
        """Test TopicInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TopicInfo`
        """
        model = TopicInfo()
        if include_optional:
            return TopicInfo(
                h_title = '',
                main_title = '',
                author = '',
                language = '',
                level = 56,
                primary_content = [
                    dataforseo_client.models.content_item_info.ContentItemInfo(
                        text = '', 
                        url = '', 
                        urls = [
                            dataforseo_client.models.content_url_info.ContentUrlInfo(
                                url = '', 
                                anchor_text = '', )
                            ], )
                    ],
                secondary_content = [
                    dataforseo_client.models.content_item_info.ContentItemInfo(
                        text = '', 
                        url = '', 
                        urls = [
                            dataforseo_client.models.content_url_info.ContentUrlInfo(
                                url = '', 
                                anchor_text = '', )
                            ], )
                    ],
                table_content = [
                    dataforseo_client.models.table_content.TableContent(
                        header = [
                            dataforseo_client.models.table_content_item_info.TableContentItemInfo(
                                row_cells = [
                                    dataforseo_client.models.row_cell_info.RowCellInfo(
                                        text = '', 
                                        urls = [
                                            dataforseo_client.models.content_url_info.ContentUrlInfo(
                                                url = '', 
                                                anchor_text = '', )
                                            ], 
                                        is_header = True, )
                                    ], )
                            ], 
                        body = [
                            dataforseo_client.models.table_content_item_info.TableContentItemInfo()
                            ], 
                        footer = [
                            
                            ], )
                    ]
            )
        else:
            return TopicInfo(
        )
        """

    def testTopicInfo(self):
        """Test TopicInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

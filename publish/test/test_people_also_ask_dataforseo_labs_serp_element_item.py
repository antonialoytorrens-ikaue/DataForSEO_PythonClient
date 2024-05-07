# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.people_also_ask_dataforseo_labs_serp_element_item import PeopleAlsoAskDataforseoLabsSerpElementItem

class TestPeopleAlsoAskDataforseoLabsSerpElementItem(unittest.TestCase):
    """PeopleAlsoAskDataforseoLabsSerpElementItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PeopleAlsoAskDataforseoLabsSerpElementItem:
        """Test PeopleAlsoAskDataforseoLabsSerpElementItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PeopleAlsoAskDataforseoLabsSerpElementItem`
        """
        model = PeopleAlsoAskDataforseoLabsSerpElementItem()
        if include_optional:
            return PeopleAlsoAskDataforseoLabsSerpElementItem(
                se_type = '',
                rank_group = 56,
                rank_absolute = 56,
                position = '',
                xpath = '',
                items = [
                    dataforseo_client.models.people_also_ask_element.PeopleAlsoAskElement(
                        type = '', 
                        title = '', 
                        seed_question = '', 
                        xpath = '', 
                        expanded_element = [
                            dataforseo_client.models.people_also_ask_expanded_element.PeopleAlsoAskExpandedElement(
                                type = '', 
                                featured_title = '', 
                                url = '', 
                                domain = '', 
                                title = '', 
                                description = '', 
                                images = [
                                    dataforseo_client.models.images_element.ImagesElement(
                                        type = '', 
                                        alt = '', 
                                        url = '', 
                                        image_url = '', )
                                    ], 
                                timestamp = '', 
                                table = dataforseo_client.models.table.Table(
                                    table_element = '', 
                                    table_header = [
                                        ''
                                        ], 
                                    table_content = [
                                        [
                                            ''
                                            ]
                                        ], ), )
                            ], )
                    ]
            )
        else:
            return PeopleAlsoAskDataforseoLabsSerpElementItem(
        )
        """

    def testPeopleAlsoAskDataforseoLabsSerpElementItem(self):
        """Test PeopleAlsoAskDataforseoLabsSerpElementItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

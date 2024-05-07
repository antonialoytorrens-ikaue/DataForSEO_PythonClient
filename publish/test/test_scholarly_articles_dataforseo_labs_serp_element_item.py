# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.scholarly_articles_dataforseo_labs_serp_element_item import ScholarlyArticlesDataforseoLabsSerpElementItem

class TestScholarlyArticlesDataforseoLabsSerpElementItem(unittest.TestCase):
    """ScholarlyArticlesDataforseoLabsSerpElementItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScholarlyArticlesDataforseoLabsSerpElementItem:
        """Test ScholarlyArticlesDataforseoLabsSerpElementItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScholarlyArticlesDataforseoLabsSerpElementItem`
        """
        model = ScholarlyArticlesDataforseoLabsSerpElementItem()
        if include_optional:
            return ScholarlyArticlesDataforseoLabsSerpElementItem(
                rank_group = 56,
                rank_absolute = 56,
                position = '',
                xpath = '',
                title = '',
                url = '',
                items = [
                    dataforseo_client.models.scholarly_articles_element.ScholarlyArticlesElement(
                        type = '', 
                        title = '', 
                        url = '', 
                        author = '', 
                        description = '', )
                    ]
            )
        else:
            return ScholarlyArticlesDataforseoLabsSerpElementItem(
        )
        """

    def testScholarlyArticlesDataforseoLabsSerpElementItem(self):
        """Test ScholarlyArticlesDataforseoLabsSerpElementItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.domain_analytics_technologies_domains_by_live_item import DomainAnalyticsTechnologiesDomainsByLiveItem

class TestDomainAnalyticsTechnologiesDomainsByLiveItem(unittest.TestCase):
    """DomainAnalyticsTechnologiesDomainsByLiveItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DomainAnalyticsTechnologiesDomainsByLiveItem:
        """Test DomainAnalyticsTechnologiesDomainsByLiveItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DomainAnalyticsTechnologiesDomainsByLiveItem`
        """
        model = DomainAnalyticsTechnologiesDomainsByLiveItem()
        if include_optional:
            return DomainAnalyticsTechnologiesDomainsByLiveItem(
                type = '',
                domain = '',
                title = '',
                description = '',
                meta_keywords = [
                    ''
                    ],
                domain_rank = '',
                last_visited = '',
                country_iso_code = '',
                language_code = '',
                content_language_code = '',
                phone_numbers = [
                    ''
                    ],
                emails = [
                    ''
                    ],
                social_graph_urls = [
                    ''
                    ],
                technologies = dataforseo_client.models.technologies_info.TechnologiesInfo(
                    add_ons = {
                        'key' : [
                            ''
                            ]
                        }, 
                    analytics = {
                        'key' : [
                            ''
                            ]
                        }, 
                    web_development = {
                        'key' : [
                            ''
                            ]
                        }, 
                    security = {
                        'key' : [
                            ''
                            ]
                        }, 
                    business_tools = {
                        'key' : [
                            ''
                            ]
                        }, 
                    sales = {
                        'key' : [
                            ''
                            ]
                        }, 
                    other = {
                        'key' : [
                            ''
                            ]
                        }, 
                    user_generated_content = {
                        'key' : [
                            ''
                            ]
                        }, 
                    privacy = {
                        'key' : [
                            ''
                            ]
                        }, 
                    servers = {
                        'key' : [
                            ''
                            ]
                        }, 
                    location = {
                        'key' : [
                            ''
                            ]
                        }, 
                    content = {
                        'key' : [
                            ''
                            ]
                        }, 
                    media = {
                        'key' : [
                            ''
                            ]
                        }, 
                    marketing = {
                        'key' : [
                            ''
                            ]
                        }, 
                    communication = {
                        'key' : [
                            ''
                            ]
                        }, 
                    utilities = {
                        'key' : [
                            ''
                            ]
                        }, )
            )
        else:
            return DomainAnalyticsTechnologiesDomainsByLiveItem(
        )
        """

    def testDomainAnalyticsTechnologiesDomainsByLiveItem(self):
        """Test DomainAnalyticsTechnologiesDomainsByLiveItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

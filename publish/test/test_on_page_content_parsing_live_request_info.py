# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.on_page_content_parsing_live_request_info import OnPageContentParsingLiveRequestInfo

class TestOnPageContentParsingLiveRequestInfo(unittest.TestCase):
    """OnPageContentParsingLiveRequestInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OnPageContentParsingLiveRequestInfo:
        """Test OnPageContentParsingLiveRequestInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OnPageContentParsingLiveRequestInfo`
        """
        model = OnPageContentParsingLiveRequestInfo()
        if include_optional:
            return OnPageContentParsingLiveRequestInfo(
                url = '',
                custom_user_agent = '',
                browser_preset = '',
                browser_screen_width = 56,
                browser_screen_height = 56,
                browser_screen_scale_factor = 1.337,
                store_raw_html = True,
                disable_cookie_popup = True,
                accept_language = '',
                enable_javascript = True,
                enable_browser_rendering = True,
                enable_xhr = True
            )
        else:
            return OnPageContentParsingLiveRequestInfo(
        )
        """

    def testOnPageContentParsingLiveRequestInfo(self):
        """Test OnPageContentParsingLiveRequestInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

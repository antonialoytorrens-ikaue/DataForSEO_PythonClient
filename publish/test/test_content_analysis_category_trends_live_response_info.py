# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.content_analysis_category_trends_live_response_info import ContentAnalysisCategoryTrendsLiveResponseInfo

class TestContentAnalysisCategoryTrendsLiveResponseInfo(unittest.TestCase):
    """ContentAnalysisCategoryTrendsLiveResponseInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContentAnalysisCategoryTrendsLiveResponseInfo:
        """Test ContentAnalysisCategoryTrendsLiveResponseInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContentAnalysisCategoryTrendsLiveResponseInfo`
        """
        model = ContentAnalysisCategoryTrendsLiveResponseInfo()
        if include_optional:
            return ContentAnalysisCategoryTrendsLiveResponseInfo(
                version = '',
                status_code = 56,
                status_message = '',
                time = '',
                cost = 1.337,
                tasks_count = 56,
                tasks_error = 56,
                tasks = [
                    dataforseo_client.models.content_analysis_category_trends_live_task_info.ContentAnalysisCategoryTrendsLiveTaskInfo()
                    ]
            )
        else:
            return ContentAnalysisCategoryTrendsLiveResponseInfo(
        )
        """

    def testContentAnalysisCategoryTrendsLiveResponseInfo(self):
        """Test ContentAnalysisCategoryTrendsLiveResponseInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

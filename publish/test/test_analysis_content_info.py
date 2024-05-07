# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.analysis_content_info import AnalysisContentInfo

class TestAnalysisContentInfo(unittest.TestCase):
    """AnalysisContentInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AnalysisContentInfo:
        """Test AnalysisContentInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AnalysisContentInfo`
        """
        model = AnalysisContentInfo()
        if include_optional:
            return AnalysisContentInfo(
                content_type = '',
                title = '',
                main_title = '',
                previous_title = '',
                level = 56,
                author = '',
                snippet = '',
                snippet_length = 56,
                social_metrics = [
                    dataforseo_client.models.social_metrics_info.SocialMetricsInfo(
                        type = '', 
                        like_count = 56, )
                    ],
                highlighted_text = '',
                language = '',
                sentiment_connotations = {
                    'key' : 56
                    },
                connotation_types = {
                    'key' : 56
                    },
                text_category = [
                    56
                    ],
                date_published = '',
                content_quality_score = 56,
                semantic_location = '',
                rating = dataforseo_client.models.content_analysis_rating_info.ContentAnalysisRatingInfo(
                    name = '', 
                    rating_value = 1.337, 
                    rating_count = 56, 
                    max_rating_value = '', 
                    relative_rating = 1.337, ),
                group_date = ''
            )
        else:
            return AnalysisContentInfo(
        )
        """

    def testAnalysisContentInfo(self):
        """Test AnalysisContentInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

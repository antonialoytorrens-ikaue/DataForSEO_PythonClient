# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.keywords_data_google_ads_keywords_for_keywords_live_result_info import KeywordsDataGoogleAdsKeywordsForKeywordsLiveResultInfo

class TestKeywordsDataGoogleAdsKeywordsForKeywordsLiveResultInfo(unittest.TestCase):
    """KeywordsDataGoogleAdsKeywordsForKeywordsLiveResultInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> KeywordsDataGoogleAdsKeywordsForKeywordsLiveResultInfo:
        """Test KeywordsDataGoogleAdsKeywordsForKeywordsLiveResultInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `KeywordsDataGoogleAdsKeywordsForKeywordsLiveResultInfo`
        """
        model = KeywordsDataGoogleAdsKeywordsForKeywordsLiveResultInfo()
        if include_optional:
            return KeywordsDataGoogleAdsKeywordsForKeywordsLiveResultInfo(
                keyword = '',
                location_code = 56,
                language_code = '',
                search_partners = True,
                competition = '',
                competition_index = 56,
                search_volume = 56,
                low_top_of_page_bid = 1.337,
                high_top_of_page_bid = 1.337,
                cpc = 1.337,
                monthly_searches = [
                    dataforseo_client.models.monthly_searches.MonthlySearches(
                        year = 56, 
                        month = 56, 
                        search_volume = 56, )
                    ],
                keyword_annotations = dataforseo_client.models.keyword_annotations.KeywordAnnotations(
                    concepts = [
                        dataforseo_client.models.concept_info.ConceptInfo(
                            name = '', 
                            concept_group = dataforseo_client.models.concept_group_info.ConceptGroupInfo(
                                name = '', 
                                type = '', ), )
                        ], )
            )
        else:
            return KeywordsDataGoogleAdsKeywordsForKeywordsLiveResultInfo(
        )
        """

    def testKeywordsDataGoogleAdsKeywordsForKeywordsLiveResultInfo(self):
        """Test KeywordsDataGoogleAdsKeywordsForKeywordsLiveResultInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

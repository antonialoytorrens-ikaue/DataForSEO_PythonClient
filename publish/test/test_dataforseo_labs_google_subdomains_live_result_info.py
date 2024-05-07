# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.dataforseo_labs_google_subdomains_live_result_info import DataforseoLabsGoogleSubdomainsLiveResultInfo

class TestDataforseoLabsGoogleSubdomainsLiveResultInfo(unittest.TestCase):
    """DataforseoLabsGoogleSubdomainsLiveResultInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataforseoLabsGoogleSubdomainsLiveResultInfo:
        """Test DataforseoLabsGoogleSubdomainsLiveResultInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataforseoLabsGoogleSubdomainsLiveResultInfo`
        """
        model = DataforseoLabsGoogleSubdomainsLiveResultInfo()
        if include_optional:
            return DataforseoLabsGoogleSubdomainsLiveResultInfo(
                se_type = '',
                target = '',
                location_code = 56,
                language_code = '',
                total_count = 56,
                items_count = 56,
                items = [
                    dataforseo_client.models.dataforseo_labs_subdomains_live_item.DataforseoLabsSubdomainsLiveItem(
                        se_type = '', 
                        subdomain = '', 
                        metrics = {
                            'key' : dataforseo_client.models.metrics_info.MetricsInfo(
                                pos_1 = 56, 
                                pos_2_3 = 56, 
                                pos_4_10 = 56, 
                                pos_11_20 = 56, 
                                pos_21_30 = 56, 
                                pos_31_40 = 56, 
                                pos_41_50 = 56, 
                                pos_51_60 = 56, 
                                pos_61_70 = 56, 
                                pos_71_80 = 56, 
                                pos_81_90 = 56, 
                                pos_91_100 = 56, 
                                etv = 1.337, 
                                impressions_etv = 1.337, 
                                count = 56, 
                                estimated_paid_traffic_cost = 1.337, 
                                is_new = 56, 
                                is_up = 56, 
                                is_down = 56, 
                                is_lost = 56, )
                            }, )
                    ]
            )
        else:
            return DataforseoLabsGoogleSubdomainsLiveResultInfo(
        )
        """

    def testDataforseoLabsGoogleSubdomainsLiveResultInfo(self):
        """Test DataforseoLabsGoogleSubdomainsLiveResultInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

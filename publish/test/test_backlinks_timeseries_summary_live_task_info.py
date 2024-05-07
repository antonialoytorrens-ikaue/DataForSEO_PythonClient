# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.backlinks_timeseries_summary_live_task_info import BacklinksTimeseriesSummaryLiveTaskInfo

class TestBacklinksTimeseriesSummaryLiveTaskInfo(unittest.TestCase):
    """BacklinksTimeseriesSummaryLiveTaskInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BacklinksTimeseriesSummaryLiveTaskInfo:
        """Test BacklinksTimeseriesSummaryLiveTaskInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BacklinksTimeseriesSummaryLiveTaskInfo`
        """
        model = BacklinksTimeseriesSummaryLiveTaskInfo()
        if include_optional:
            return BacklinksTimeseriesSummaryLiveTaskInfo(
                id = '',
                status_code = 56,
                status_message = '',
                time = '',
                cost = 1.337,
                result_count = 56,
                path = [
                    ''
                    ],
                data = dataforseo_client.models.data.data(),
                result = [
                    dataforseo_client.models.backlinks_timeseries_summary_live_result_info.BacklinksTimeseriesSummaryLiveResultInfo(
                        target = '', 
                        date_from = '', 
                        date_to = '', 
                        group_range = '', 
                        items_count = 56, 
                        items = [
                            dataforseo_client.models.backlinks_timeseries_summary_live_item.BacklinksTimeseriesSummaryLiveItem(
                                type = '', 
                                date = '', 
                                rank = 56, 
                                backlinks = 56, 
                                backlinks_nofollow = 56, 
                                referring_pages = 56, 
                                referring_pages_nofollow = 56, 
                                referring_domains = 56, 
                                referring_domains_nofollow = 56, 
                                referring_main_domains = 56, 
                                referring_main_domains_nofollow = 56, 
                                referring_ips = 56, 
                                referring_subnets = 56, )
                            ], )
                    ]
            )
        else:
            return BacklinksTimeseriesSummaryLiveTaskInfo(
        )
        """

    def testBacklinksTimeseriesSummaryLiveTaskInfo(self):
        """Test BacklinksTimeseriesSummaryLiveTaskInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

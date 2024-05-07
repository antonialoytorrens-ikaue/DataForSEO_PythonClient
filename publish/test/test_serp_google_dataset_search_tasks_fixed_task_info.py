# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.serp_google_dataset_search_tasks_fixed_task_info import SerpGoogleDatasetSearchTasksFixedTaskInfo

class TestSerpGoogleDatasetSearchTasksFixedTaskInfo(unittest.TestCase):
    """SerpGoogleDatasetSearchTasksFixedTaskInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SerpGoogleDatasetSearchTasksFixedTaskInfo:
        """Test SerpGoogleDatasetSearchTasksFixedTaskInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SerpGoogleDatasetSearchTasksFixedTaskInfo`
        """
        model = SerpGoogleDatasetSearchTasksFixedTaskInfo()
        if include_optional:
            return SerpGoogleDatasetSearchTasksFixedTaskInfo(
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
                    dataforseo_client.models.serp_google_dataset_search_tasks_fixed_result_info.SerpGoogleDatasetSearchTasksFixedResultInfo(
                        id = '', 
                        se = '', 
                        se_type = '', 
                        date_fixed = '', 
                        tag = '', 
                        endpoint_regular = '', 
                        endpoint_advanced = '', 
                        endpoint_html = '', )
                    ]
            )
        else:
            return SerpGoogleDatasetSearchTasksFixedTaskInfo(
        )
        """

    def testSerpGoogleDatasetSearchTasksFixedTaskInfo(self):
        """Test SerpGoogleDatasetSearchTasksFixedTaskInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

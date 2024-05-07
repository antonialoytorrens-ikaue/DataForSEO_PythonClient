# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.dataforseo_labs_locations_and_languages_task_info import DataforseoLabsLocationsAndLanguagesTaskInfo

class TestDataforseoLabsLocationsAndLanguagesTaskInfo(unittest.TestCase):
    """DataforseoLabsLocationsAndLanguagesTaskInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataforseoLabsLocationsAndLanguagesTaskInfo:
        """Test DataforseoLabsLocationsAndLanguagesTaskInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataforseoLabsLocationsAndLanguagesTaskInfo`
        """
        model = DataforseoLabsLocationsAndLanguagesTaskInfo()
        if include_optional:
            return DataforseoLabsLocationsAndLanguagesTaskInfo(
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
                    dataforseo_client.models.dataforseo_labs_locations_and_languages_result_info.DataforseoLabsLocationsAndLanguagesResultInfo(
                        location_code = 56, 
                        location_name = '', 
                        location_code_parent = 56, 
                        country_iso_code = '', 
                        location_type = '', 
                        available_languages = [
                            dataforseo_client.models.available_languages.AvailableLanguages(
                                available_sources = [
                                    ''
                                    ], 
                                language_name = '', 
                                language_code = '', 
                                keywords = 56, 
                                serps = 56, )
                            ], )
                    ]
            )
        else:
            return DataforseoLabsLocationsAndLanguagesTaskInfo(
        )
        """

    def testDataforseoLabsLocationsAndLanguagesTaskInfo(self):
        """Test DataforseoLabsLocationsAndLanguagesTaskInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

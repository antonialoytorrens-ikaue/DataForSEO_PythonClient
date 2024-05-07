# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.business_data_errors_request_info import BusinessDataErrorsRequestInfo

class TestBusinessDataErrorsRequestInfo(unittest.TestCase):
    """BusinessDataErrorsRequestInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BusinessDataErrorsRequestInfo:
        """Test BusinessDataErrorsRequestInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BusinessDataErrorsRequestInfo`
        """
        model = BusinessDataErrorsRequestInfo()
        if include_optional:
            return BusinessDataErrorsRequestInfo(
                limit = 56,
                offset = 56,
                filtered_function = '',
                datetime_from = '',
                datetime_to = ''
            )
        else:
            return BusinessDataErrorsRequestInfo(
        )
        """

    def testBusinessDataErrorsRequestInfo(self):
        """Test BusinessDataErrorsRequestInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

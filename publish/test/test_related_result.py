# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.related_result import RelatedResult

class TestRelatedResult(unittest.TestCase):
    """RelatedResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RelatedResult:
        """Test RelatedResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RelatedResult`
        """
        model = RelatedResult()
        if include_optional:
            return RelatedResult(
                type = '',
                xpath = '',
                domain = '',
                title = '',
                url = '',
                cache_url = '',
                related_search_url = '',
                breadcrumb = '',
                website_name = '',
                is_image = True,
                is_video = True,
                description = '',
                pre_snippet = '',
                extended_snippet = '',
                images = [
                    dataforseo_client.models.images_element.ImagesElement(
                        type = '', 
                        alt = '', 
                        url = '', 
                        image_url = '', )
                    ],
                amp_version = True,
                rating = dataforseo_client.models.rating_info.RatingInfo(
                    rating_type = '', 
                    value = 1.337, 
                    votes_count = 56, 
                    rating_max = 56, ),
                price = dataforseo_client.models.price_info.PriceInfo(
                    current = 1.337, 
                    regular = 1.337, 
                    max_value = 1.337, 
                    currency = '', 
                    is_price_range = True, 
                    displayed_price = '', ),
                highlighted = [
                    ''
                    ],
                about_this_result = dataforseo_client.models.about_this_result_element.AboutThisResultElement(
                    type = '', 
                    url = '', 
                    source = '', 
                    source_info = '', 
                    source_url = '', 
                    language = '', 
                    location = '', 
                    search_terms = [
                        ''
                        ], 
                    related_terms = [
                        ''
                        ], ),
                timestamp = ''
            )
        else:
            return RelatedResult(
        )
        """

    def testRelatedResult(self):
        """Test RelatedResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

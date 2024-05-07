# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.backlinks_page_intersection_info import BacklinksPageIntersectionInfo

class TestBacklinksPageIntersectionInfo(unittest.TestCase):
    """BacklinksPageIntersectionInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BacklinksPageIntersectionInfo:
        """Test BacklinksPageIntersectionInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BacklinksPageIntersectionInfo`
        """
        model = BacklinksPageIntersectionInfo()
        if include_optional:
            return BacklinksPageIntersectionInfo(
                type = '',
                domain_from = '',
                url_from = '',
                url_from_https = True,
                domain_to = '',
                url_to = '',
                url_to_https = True,
                tld_from = '',
                is_new = True,
                is_lost = True,
                backlink_spam_score = 56,
                rank = 56,
                page_from_rank = 56,
                domain_from_rank = 56,
                domain_from_platform_type = [
                    ''
                    ],
                domain_from_is_ip = True,
                domain_from_ip = '',
                domain_from_country = '',
                page_from_external_links = 56,
                page_from_internal_links = 56,
                page_from_size = 56,
                page_from_encoding = '',
                page_from_language = '',
                page_from_title = '',
                page_from_status_code = 56,
                first_seen = '',
                prev_seen = '',
                last_seen = '',
                item_type = '',
                attributes = [
                    ''
                    ],
                dofollow = True,
                original = True,
                alt = '',
                anchor = '',
                text_pre = '',
                text_post = '',
                semantic_location = '',
                links_count = 56,
                group_count = 56,
                is_broken = True,
                url_to_status_code = 56,
                url_to_spam_score = 56,
                url_to_redirect_target = '',
                is_indirect_link = True,
                indirect_link_path = [
                    dataforseo_client.models.redirect.Redirect(
                        type = '', 
                        status_code = 56, 
                        url = '', )
                    ]
            )
        else:
            return BacklinksPageIntersectionInfo(
        )
        """

    def testBacklinksPageIntersectionInfo(self):
        """Test BacklinksPageIntersectionInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

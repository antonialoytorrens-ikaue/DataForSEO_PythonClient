# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.google_business_info_business_data_serp_element_item import GoogleBusinessInfoBusinessDataSerpElementItem

class TestGoogleBusinessInfoBusinessDataSerpElementItem(unittest.TestCase):
    """GoogleBusinessInfoBusinessDataSerpElementItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GoogleBusinessInfoBusinessDataSerpElementItem:
        """Test GoogleBusinessInfoBusinessDataSerpElementItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GoogleBusinessInfoBusinessDataSerpElementItem`
        """
        model = GoogleBusinessInfoBusinessDataSerpElementItem()
        if include_optional:
            return GoogleBusinessInfoBusinessDataSerpElementItem(
                rank_group = 56,
                rank_absolute = 56,
                position = '',
                title = '',
                description = '',
                category = '',
                category_ids = [
                    ''
                    ],
                additional_categories = [
                    ''
                    ],
                cid = '',
                feature_id = '',
                address = '',
                address_info = dataforseo_client.models.address_info.AddressInfo(
                    borough = '', 
                    address = '', 
                    city = '', 
                    zip = '', 
                    region = '', 
                    country_code = '', ),
                place_id = '',
                phone = '',
                url = '',
                contact_url = '',
                domain = '',
                logo = '',
                main_image = '',
                total_photos = 56,
                snippet = '',
                latitude = 1.337,
                longitude = 1.337,
                is_claimed = True,
                questions_and_answers_count = 56,
                attributes = dataforseo_client.models.business_data_attributes_info.BusinessDataAttributesInfo(
                    available_attributes = {
                        'key' : [
                            ''
                            ]
                        }, 
                    unavailable_attributes = {
                        'key' : [
                            ''
                            ]
                        }, ),
                place_topics = {
                    'key' : 56
                    },
                rating = dataforseo_client.models.rating_info.RatingInfo(
                    rating_type = '', 
                    value = 1.337, 
                    votes_count = 56, 
                    rating_max = 56, ),
                hotel_rating = 56,
                price_level = '',
                rating_distribution = {
                    'key' : 56
                    },
                people_also_search = [
                    dataforseo_client.models.people_also_search.PeopleAlsoSearch(
                        cid = '', 
                        feature_id = '', 
                        title = '', 
                        rating = dataforseo_client.models.rating_info.RatingInfo(
                            rating_type = '', 
                            value = 1.337, 
                            votes_count = 56, 
                            rating_max = 56, ), )
                    ],
                work_time = dataforseo_client.models.work_info.WorkInfo(
                    work_hours = dataforseo_client.models.work_hours.WorkHours(
                        timetable = {
                            'key' : [
                                dataforseo_client.models.work_day_info.WorkDayInfo(
                                    open = dataforseo_client.models.work_time_info.WorkTimeInfo(
                                        hour = 56, 
                                        minute = 56, ), 
                                    close = dataforseo_client.models.work_time_info.WorkTimeInfo(
                                        hour = 56, 
                                        minute = 56, ), )
                                ]
                            }, 
                        current_status = '', ), ),
                popular_times = dataforseo_client.models.popular_times.PopularTimes(
                    popular_times_by_days = {
                        'key' : [
                            dataforseo_client.models.busy_working_time_info.BusyWorkingTimeInfo(
                                time = dataforseo_client.models.work_time_info.WorkTimeInfo(
                                    hour = 56, 
                                    minute = 56, ), 
                                popular_index = 56, )
                            ]
                        }, ),
                local_business_links = [
                    dataforseo_client.models.base_local_business_link.BaseLocalBusinessLink()
                    ],
                is_directory_item = True,
                directory = dataforseo_client.models.business_directory_info.BusinessDirectoryInfo(
                    title = '', 
                    items = [
                        dataforseo_client.models.base_business_data_serp_element_item.BaseBusinessDataSerpElementItem()
                        ], )
            )
        else:
            return GoogleBusinessInfoBusinessDataSerpElementItem(
        )
        """

    def testGoogleBusinessInfoBusinessDataSerpElementItem(self):
        """Test GoogleBusinessInfoBusinessDataSerpElementItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

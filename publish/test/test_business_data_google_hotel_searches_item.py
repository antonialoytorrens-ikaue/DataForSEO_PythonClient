# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.business_data_google_hotel_searches_item import BusinessDataGoogleHotelSearchesItem

class TestBusinessDataGoogleHotelSearchesItem(unittest.TestCase):
    """BusinessDataGoogleHotelSearchesItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BusinessDataGoogleHotelSearchesItem:
        """Test BusinessDataGoogleHotelSearchesItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BusinessDataGoogleHotelSearchesItem`
        """
        model = BusinessDataGoogleHotelSearchesItem()
        if include_optional:
            return BusinessDataGoogleHotelSearchesItem(
                type = '',
                hotel_identifier = '',
                title = '',
                stars = 56,
                is_paid = True,
                location = dataforseo_client.models.gps_coordinates_location_info.GpsCoordinatesLocationInfo(
                    latitude = 1.337, 
                    longitude = 1.337, ),
                reviews = dataforseo_client.models.hotel_review_info.HotelReviewInfo(
                    value = 1.337, 
                    votes_count = 56, 
                    mentions = [
                        dataforseo_client.models.review_mention_info.ReviewMentionInfo(
                            title = '', 
                            positive_score = 1.337, 
                            positive_count = 56, 
                            negative_count = 56, 
                            total_count = 56, 
                            visible_by_default = True, )
                        ], 
                    rating_distribution = {
                        'key' : 56
                        }, 
                    other_sites_reviews = [
                        dataforseo_client.models.other_sites_reviews_info.OtherSitesReviewsInfo(
                            title = '', 
                            url = '', 
                            review_text = '', 
                            rating = dataforseo_client.models.rating_info.RatingInfo(
                                rating_type = '', 
                                value = 1.337, 
                                votes_count = 56, 
                                rating_max = 56, ), )
                        ], ),
                overview_images = [
                    ''
                    ],
                prices = dataforseo_client.models.hotel_price_info.HotelPriceInfo(
                    price = 56, 
                    price_without_discount = 56, 
                    currency = '', 
                    discount_text = '', 
                    check_in = '', 
                    check_out = '', 
                    visitors = 56, 
                    items = [
                        dataforseo_client.models.hotel_price_item_info.HotelPriceItemInfo(
                            type = '', 
                            title = '', 
                            price = 56, 
                            currency = '', 
                            url = '', 
                            domain = '', 
                            is_paid = True, 
                            free_cancellation_until = '', 
                            offers = [
                                dataforseo_client.models.hotel_info_price_offer.HotelInfoPriceOffer(
                                    type = '', 
                                    title = '', 
                                    price = 56, 
                                    currency = '', 
                                    url = '', 
                                    max_visitors = 56, 
                                    offer_images = [
                                        ''
                                        ], 
                                    free_cancellation_until = '', )
                                ], )
                        ], )
            )
        else:
            return BusinessDataGoogleHotelSearchesItem(
        )
        """

    def testBusinessDataGoogleHotelSearchesItem(self):
        """Test BusinessDataGoogleHotelSearchesItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

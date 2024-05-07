# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.appendix_data_info import AppendixDataInfo

class TestAppendixDataInfo(unittest.TestCase):
    """AppendixDataInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppendixDataInfo:
        """Test AppendixDataInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppendixDataInfo`
        """
        model = AppendixDataInfo()
        if include_optional:
            return AppendixDataInfo(
                serp = dataforseo_client.models.appendix_serp_limits_rates_data_info.AppendixSerpLimitsRatesDataInfo(
                    task_post = 1.337, 
                    task_get = dataforseo_client.models.appendix_function_type_info.AppendixFunctionTypeInfo(
                        regular = 1.337, 
                        advanced = 1.337, 
                        html = 1.337, ), 
                    tasks_ready = 1.337, 
                    locations = 1.337, 
                    languages = 1.337, 
                    live = dataforseo_client.models.appendix_function_type_info.AppendixFunctionTypeInfo(
                        regular = 1.337, 
                        advanced = 1.337, 
                        html = 1.337, ), 
                    errors = 1.337, 
                    tasks_fixed = 1.337, 
                    jobs = dataforseo_client.models.appendix_jobs_serp_limits_rates_data_info.AppendixJobsSerpLimitsRatesDataInfo(
                        task_post = 1.337, ), 
                    screenshot = 1.337, ),
                total = 1.337,
                total_serp = 1.337,
                keywords_data = dataforseo_client.models.appendix_keywords_data_data_info.AppendixKeywordsDataDataInfo(
                    keywords_for_keywords = dataforseo_client.models.appendix_function_info.AppendixFunctionInfo(
                        task_post = 1.337, 
                        task_get = 1.337, 
                        tasks_ready = 1.337, 
                        live = 1.337, ), 
                    keywords_for_site = dataforseo_client.models.appendix_function_info.AppendixFunctionInfo(
                        task_post = 1.337, 
                        task_get = 1.337, 
                        tasks_ready = 1.337, 
                        live = 1.337, ), 
                    search_volume = , 
                    ad_traffic_by_keywords = , 
                    languages = 1.337, 
                    locations = 1.337, 
                    tasks_ready = 1.337, 
                    explore = , 
                    categories = 1.337, 
                    errors = 1.337, 
                    bing = dataforseo_client.models.appendix_bing_keywords_data_limits_rates_data_info.AppendixBingKeywordsDataLimitsRatesDataInfo(
                        keyword_performance = , 
                        search_volume_history = , ), 
                    keyword_performance = dataforseo_client.models.appendix_keyword_performance_keywords_data_limits_rates_data_info.AppendixKeywordPerformanceKeywordsDataLimitsRatesDataInfo(
                        task_get = 1.337, 
                        task_post = 1.337, 
                        locations_and_languages = 1.337, ), 
                    search_volume_history = , 
                    google_ads = dataforseo_client.models.appendix_google_ads_keywords_data_limits_rates_data_info.AppendixGoogleAdsKeywordsDataLimitsRatesDataInfo(
                        status = 1.337, ), 
                    dataforseo_trends = dataforseo_client.models.appendix_dataforseo_trends_keywords_data_limits_rates_data_info.AppendixDataforseoTrendsKeywordsDataLimitsRatesDataInfo(
                        subregion_interests = , 
                        demography = , 
                        merged_data = , ), 
                    naver = dataforseo_client.models.appendix_naver_keywords_data_data_info.AppendixNaverKeywordsDataDataInfo(
                        keywords_for_category = , ), 
                    google = dataforseo_client.models.appendix_bing_keywords_data_limits_rates_data_info.AppendixBingKeywordsDataLimitsRatesDataInfo(), 
                    keyword_ideas_ads_api = dataforseo_client.models.appendix_serp_limits_rates_data_info.AppendixSerpLimitsRatesDataInfo(
                        task_post = 1.337, 
                        task_get = dataforseo_client.models.appendix_function_type_info.AppendixFunctionTypeInfo(
                            regular = 1.337, 
                            advanced = 1.337, 
                            html = 1.337, ), 
                        tasks_ready = 1.337, 
                        locations = 1.337, 
                        languages = 1.337, 
                        live = dataforseo_client.models.appendix_function_type_info.AppendixFunctionTypeInfo(
                            regular = 1.337, 
                            advanced = 1.337, 
                            html = 1.337, ), 
                        errors = 1.337, 
                        tasks_fixed = 1.337, 
                        jobs = dataforseo_client.models.appendix_jobs_serp_limits_rates_data_info.AppendixJobsSerpLimitsRatesDataInfo(
                            task_post = 1.337, ), 
                        screenshot = 1.337, ), ),
                total_keywords_data = 1.337,
                appendix = dataforseo_client.models.appendix_appendix_data_info.AppendixAppendixDataInfo(
                    user_data = 1.337, 
                    errors = 1.337, 
                    test = 1.337, 
                    status = 1.337, ),
                total_appendix = 1.337,
                dataforseo_labs = dataforseo_client.models.appendix_dataforseo_labs_limits_rates_data_info.AppendixDataforseoLabsLimitsRatesDataInfo(
                    locations_and_languages = 1.337, 
                    categories = 1.337, 
                    errors = 1.337, 
                    product_competitors = dataforseo_client.models.appendix_function_info.AppendixFunctionInfo(
                        task_post = 1.337, 
                        task_get = 1.337, 
                        tasks_ready = 1.337, 
                        live = 1.337, ), 
                    product_keyword_intersections = dataforseo_client.models.appendix_function_info.AppendixFunctionInfo(
                        task_post = 1.337, 
                        task_get = 1.337, 
                        tasks_ready = 1.337, 
                        live = 1.337, ), 
                    product_rank_overview = , 
                    ranked_keywords = , 
                    serp_competitors = , 
                    subdomains = , 
                    relevant_pages = , 
                    competitors_domain = , 
                    related_keywords = , 
                    domain_rank_overview = , 
                    domain_intersection = , 
                    page_intersection = , 
                    bulk_traffic_estimation = , 
                    bulk_keyword_difficulty = , 
                    bulk_search_volume = , 
                    keywords_for_site = , 
                    keyword_suggestions = , 
                    keyword_ideas = , 
                    historical_search_volume = , 
                    categories_for_domain = , 
                    domain_metrics_by_categories = , 
                    top_searches = , 
                    domain_whois_overview = , 
                    historical_rank_overview = , 
                    keywords_for_categories = , 
                    historical_serps = , 
                    app_competitors = , 
                    keywords_for_app = , 
                    app_intersection = , 
                    bulk_app_metrics = , 
                    search_intent = , ),
                total_dataforseo_labs = 1.337,
                domain_analytics = dataforseo_client.models.appendix_domain_analytics_limits_rates_data_info.AppendixDomainAnalyticsLimitsRatesDataInfo(
                    tasks_ready = 1.337, 
                    errors = 1.337, 
                    whois = dataforseo_client.models.appendix_whois_domain_analytics_limits_rates_data_info.AppendixWhoisDomainAnalyticsLimitsRatesDataInfo(
                        overview = dataforseo_client.models.appendix_function_info.AppendixFunctionInfo(
                            task_post = 1.337, 
                            task_get = 1.337, 
                            tasks_ready = 1.337, 
                            live = 1.337, ), ), 
                    technologies = dataforseo_client.models.appendix_technologies_domain_analytics_limits_rates_data_info.AppendixTechnologiesDomainAnalyticsLimitsRatesDataInfo(
                        domain_technologies = dataforseo_client.models.appendix_function_info.AppendixFunctionInfo(
                            task_post = 1.337, 
                            task_get = 1.337, 
                            tasks_ready = 1.337, 
                            live = 1.337, ), 
                        domains_by_technology = , 
                        languages = 1.337, 
                        locations = 1.337, 
                        aggregation_technologies = , 
                        technologies_summary = , 
                        domains_by_html_terms = , 
                        technology_stats = , ), ),
                total_domain_analytics = 1.337,
                merchant = dataforseo_client.models.appendix_merchant_limits_rates_data_info.AppendixMerchantLimitsRatesDataInfo(
                    google = dataforseo_client.models.appendix_merchant_google_info.AppendixMerchantGoogleInfo(
                        products = dataforseo_client.models.appendix_serp_limits_rates_data_info.AppendixSerpLimitsRatesDataInfo(
                            task_post = 1.337, 
                            task_get = dataforseo_client.models.appendix_function_type_info.AppendixFunctionTypeInfo(
                                regular = 1.337, 
                                advanced = 1.337, 
                                html = 1.337, ), 
                            tasks_ready = 1.337, 
                            locations = 1.337, 
                            languages = 1.337, 
                            live = dataforseo_client.models.appendix_function_type_info.AppendixFunctionTypeInfo(
                                regular = 1.337, 
                                advanced = 1.337, 
                                html = 1.337, ), 
                            errors = 1.337, 
                            tasks_fixed = 1.337, 
                            jobs = dataforseo_client.models.appendix_jobs_serp_limits_rates_data_info.AppendixJobsSerpLimitsRatesDataInfo(
                                task_post = 1.337, ), 
                            screenshot = 1.337, ), 
                        sellers = dataforseo_client.models.appendix_sellers_google_merchant_limits_rates_data_info.AppendixSellersGoogleMerchantLimitsRatesDataInfo(
                            task_post = 1.337, 
                            tasks_ready = 1.337, 
                            ad_url = 1.337, ), 
                        product_spec = dataforseo_client.models.appendix_serp_limits_rates_data_info.AppendixSerpLimitsRatesDataInfo(
                            task_post = 1.337, 
                            tasks_ready = 1.337, 
                            locations = 1.337, 
                            languages = 1.337, 
                            errors = 1.337, 
                            tasks_fixed = 1.337, 
                            screenshot = 1.337, ), 
                        product_info = , ), 
                    amazon = dataforseo_client.models.appendix_merchant_amazon_info.AppendixMerchantAmazonInfo(
                        asin = , ), 
                    locations = 1.337, 
                    languages = 1.337, 
                    errors = 1.337, 
                    reviews = , ),
                total_merchant = 1.337,
                on_page = dataforseo_client.models.appendix_on_page_limits_rates_data_info.AppendixOnPageLimitsRatesDataInfo(
                    task_post = 1.337, 
                    tasks_ready = 1.337, 
                    summary = 1.337, 
                    resources = 1.337, 
                    pages = 1.337, 
                    non_indexable = 1.337, 
                    duplicate_tags = 1.337, 
                    links = 1.337, 
                    waterfall = 1.337, 
                    errors = 1.337, 
                    pages_by_resource = 1.337, 
                    duplicate_content = 1.337, 
                    raw_html = 1.337, 
                    instant_pages = 1.337, 
                    redirect_chains = 1.337, 
                    lighthouse = dataforseo_client.models.appendix_function_info.AppendixFunctionInfo(
                        task_post = 1.337, 
                        task_get = 1.337, 
                        tasks_ready = 1.337, 
                        live = 1.337, ), 
                    keyword_density = 1.337, 
                    page_screenshot = 1.337, 
                    content_parsing = 1.337, 
                    content_parsing_live = 1.337, ),
                total_on_page = 1.337,
                business_data = dataforseo_client.models.appendix_business_data_limits_rates_data_info.AppendixBusinessDataLimitsRatesDataInfo(
                    google = dataforseo_client.models.appendix_business_data_google_info.AppendixBusinessDataGoogleInfo(
                        my_business_info = dataforseo_client.models.appendix_function_info.AppendixFunctionInfo(
                            task_post = 1.337, 
                            task_get = 1.337, 
                            tasks_ready = 1.337, 
                            live = 1.337, ), 
                        my_business_updates = dataforseo_client.models.appendix_function_info.AppendixFunctionInfo(
                            task_post = 1.337, 
                            task_get = 1.337, 
                            tasks_ready = 1.337, 
                            live = 1.337, ), 
                        hotel_info = dataforseo_client.models.appendix_serp_limits_rates_data_info.AppendixSerpLimitsRatesDataInfo(
                            task_post = 1.337, 
                            task_get = dataforseo_client.models.appendix_function_type_info.AppendixFunctionTypeInfo(
                                regular = 1.337, 
                                advanced = 1.337, 
                                html = 1.337, ), 
                            tasks_ready = 1.337, 
                            locations = 1.337, 
                            languages = 1.337, 
                            live = dataforseo_client.models.appendix_function_type_info.AppendixFunctionTypeInfo(
                                regular = 1.337, 
                                advanced = 1.337, 
                                html = 1.337, ), 
                            errors = 1.337, 
                            tasks_fixed = 1.337, 
                            jobs = dataforseo_client.models.appendix_jobs_serp_limits_rates_data_info.AppendixJobsSerpLimitsRatesDataInfo(
                                task_post = 1.337, ), 
                            screenshot = 1.337, ), 
                        hotel_searches = , 
                        reviews = , 
                        questions_and_answers = , ), 
                    locations = 1.337, 
                    languages = 1.337, 
                    errors = 1.337, 
                    yelp = dataforseo_client.models.appendix_business_data_day_limits_rates_data_info.AppendixBusinessDataDayLimitsRatesDataInfo(
                        search = , ), 
                    social_media = dataforseo_client.models.appendix_social_media_business_data_limits_rates_data_info.AppendixSocialMediaBusinessDataLimitsRatesDataInfo(
                        facebook = , 
                        pinterest = , 
                        reddit = , ), 
                    tripadvisor = dataforseo_client.models.appendix_business_data_day_limits_rates_data_info.AppendixBusinessDataDayLimitsRatesDataInfo(), 
                    trustpilot = , 
                    business_listings = dataforseo_client.models.appendix_business_listings_business_data_limits_rates_data_info.AppendixBusinessListingsBusinessDataLimitsRatesDataInfo(
                        categories_aggregation = , 
                        categories = 1.337, 
                        locations = 1.337, ), ),
                total_business_data = 1.337,
                backlinks = dataforseo_client.models.appendix_backlinks_limits_rates_data_info.AppendixBacklinksLimitsRatesDataInfo(
                    summary = dataforseo_client.models.appendix_function_info.AppendixFunctionInfo(
                        task_post = 1.337, 
                        task_get = 1.337, 
                        tasks_ready = 1.337, 
                        live = 1.337, ), 
                    history = dataforseo_client.models.appendix_function_info.AppendixFunctionInfo(
                        task_post = 1.337, 
                        task_get = 1.337, 
                        tasks_ready = 1.337, 
                        live = 1.337, ), 
                    content_duplicates = , 
                    domain_intersection = , 
                    backlinks = , 
                    domain_pages = , 
                    anchors = , 
                    referring_domains = , 
                    page_intersection = , 
                    referring_networks = , 
                    bulk_ranks = , 
                    bulk_backlinks = , 
                    bulk_new_lost_backlinks = , 
                    bulk_new_lost_referring_domains = , 
                    bulk_referring_domains = , 
                    errors = 1.337, 
                    domain_pages_summary = , 
                    timeseries_summary = , 
                    timeseries_new_lost_summary = , 
                    competitors = , 
                    bulk_pages_summary = , ),
                total_backlinks = 1.337,
                app_data = dataforseo_client.models.appendix_app_data_limits_rates_data_info.AppendixAppDataLimitsRatesDataInfo(
                    app_info = dataforseo_client.models.appendix_serp_limits_rates_data_info.AppendixSerpLimitsRatesDataInfo(
                        task_post = 1.337, 
                        task_get = dataforseo_client.models.appendix_function_type_info.AppendixFunctionTypeInfo(
                            regular = 1.337, 
                            advanced = 1.337, 
                            html = 1.337, ), 
                        tasks_ready = 1.337, 
                        locations = 1.337, 
                        languages = 1.337, 
                        live = dataforseo_client.models.appendix_function_type_info.AppendixFunctionTypeInfo(
                            regular = 1.337, 
                            advanced = 1.337, 
                            html = 1.337, ), 
                        errors = 1.337, 
                        tasks_fixed = 1.337, 
                        jobs = dataforseo_client.models.appendix_jobs_serp_limits_rates_data_info.AppendixJobsSerpLimitsRatesDataInfo(
                            task_post = 1.337, ), 
                        screenshot = 1.337, ), 
                    app_list = dataforseo_client.models.appendix_serp_limits_rates_data_info.AppendixSerpLimitsRatesDataInfo(
                        task_post = 1.337, 
                        tasks_ready = 1.337, 
                        locations = 1.337, 
                        languages = 1.337, 
                        errors = 1.337, 
                        tasks_fixed = 1.337, 
                        screenshot = 1.337, ), 
                    app_reviews = , 
                    app_searches = , 
                    errors = 1.337, 
                    languages = 1.337, 
                    locations = 1.337, 
                    categories = 1.337, ),
                total_app_data = 1.337,
                content_analysis = dataforseo_client.models.appendix_content_analysis_limits_rates_data_info.AppendixContentAnalysisLimitsRatesDataInfo(
                    search = dataforseo_client.models.appendix_function_info.AppendixFunctionInfo(
                        task_post = 1.337, 
                        task_get = 1.337, 
                        tasks_ready = 1.337, 
                        live = 1.337, ), 
                    summary = dataforseo_client.models.appendix_function_info.AppendixFunctionInfo(
                        task_post = 1.337, 
                        task_get = 1.337, 
                        tasks_ready = 1.337, 
                        live = 1.337, ), 
                    sentiment_analysis = , 
                    rating_distribution = , 
                    phrase_trends = , 
                    category_trends = , 
                    locations = 1.337, 
                    languages = 1.337, 
                    categories = 1.337, 
                    errors = 1.337, ),
                total_content_analysis = 1.337,
                content_generation = dataforseo_client.models.appendix_content_generation_limits_rates_data_info.AppendixContentGenerationLimitsRatesDataInfo(
                    generate = dataforseo_client.models.appendix_function_info.AppendixFunctionInfo(
                        task_post = 1.337, 
                        task_get = 1.337, 
                        tasks_ready = 1.337, 
                        live = 1.337, ), 
                    generate_meta_tags = dataforseo_client.models.appendix_function_info.AppendixFunctionInfo(
                        task_post = 1.337, 
                        task_get = 1.337, 
                        tasks_ready = 1.337, 
                        live = 1.337, ), 
                    generate_text = , 
                    paraphrase = , 
                    check_grammar = dataforseo_client.models.appendix_content_generation_day_limits_rates_data_info.AppendixContentGenerationDayLimitsRatesDataInfo(
                        live = 1.337, 
                        languages = 1.337, ), 
                    text_summary = dataforseo_client.models.appendix_content_generation_day_limits_rates_data_info.AppendixContentGenerationDayLimitsRatesDataInfo(
                        live = 1.337, 
                        languages = 1.337, ), 
                    generate_sub_topics = , ),
                total_content_generation = 1.337,
                total_traffic_analytics = 1.337,
                traffic_analytics = dataforseo_client.models.appendix_serp_limits_rates_data_info.AppendixSerpLimitsRatesDataInfo(
                    task_post = 1.337, 
                    task_get = dataforseo_client.models.appendix_function_type_info.AppendixFunctionTypeInfo(
                        regular = 1.337, 
                        advanced = 1.337, 
                        html = 1.337, ), 
                    tasks_ready = 1.337, 
                    locations = 1.337, 
                    languages = 1.337, 
                    live = dataforseo_client.models.appendix_function_type_info.AppendixFunctionTypeInfo(
                        regular = 1.337, 
                        advanced = 1.337, 
                        html = 1.337, ), 
                    errors = 1.337, 
                    tasks_fixed = 1.337, 
                    jobs = dataforseo_client.models.appendix_jobs_serp_limits_rates_data_info.AppendixJobsSerpLimitsRatesDataInfo(
                        task_post = 1.337, ), 
                    screenshot = 1.337, ),
                total_reviews = 1.337,
                reviews = dataforseo_client.models.appendix_serp_limits_rates_data_info.AppendixSerpLimitsRatesDataInfo(
                    task_post = 1.337, 
                    task_get = dataforseo_client.models.appendix_function_type_info.AppendixFunctionTypeInfo(
                        regular = 1.337, 
                        advanced = 1.337, 
                        html = 1.337, ), 
                    tasks_ready = 1.337, 
                    locations = 1.337, 
                    languages = 1.337, 
                    live = dataforseo_client.models.appendix_function_type_info.AppendixFunctionTypeInfo(
                        regular = 1.337, 
                        advanced = 1.337, 
                        html = 1.337, ), 
                    errors = 1.337, 
                    tasks_fixed = 1.337, 
                    jobs = dataforseo_client.models.appendix_jobs_serp_limits_rates_data_info.AppendixJobsSerpLimitsRatesDataInfo(
                        task_post = 1.337, ), 
                    screenshot = 1.337, ),
                total_social = 1.337,
                social = dataforseo_client.models.appendix_serp_limits_rates_data_info.AppendixSerpLimitsRatesDataInfo(
                    task_post = 1.337, 
                    task_get = dataforseo_client.models.appendix_function_type_info.AppendixFunctionTypeInfo(
                        regular = 1.337, 
                        advanced = 1.337, 
                        html = 1.337, ), 
                    tasks_ready = 1.337, 
                    locations = 1.337, 
                    languages = 1.337, 
                    live = dataforseo_client.models.appendix_function_type_info.AppendixFunctionTypeInfo(
                        regular = 1.337, 
                        advanced = 1.337, 
                        html = 1.337, ), 
                    errors = 1.337, 
                    tasks_fixed = 1.337, 
                    jobs = dataforseo_client.models.appendix_jobs_serp_limits_rates_data_info.AppendixJobsSerpLimitsRatesDataInfo(
                        task_post = 1.337, ), 
                    screenshot = 1.337, )
            )
        else:
            return AppendixDataInfo(
        )
        """

    def testAppendixDataInfo(self):
        """Test AppendixDataInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

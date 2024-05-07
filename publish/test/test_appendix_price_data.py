# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.appendix_price_data import AppendixPriceData

class TestAppendixPriceData(unittest.TestCase):
    """AppendixPriceData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppendixPriceData:
        """Test AppendixPriceData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppendixPriceData`
        """
        model = AppendixPriceData()
        if include_optional:
            return AppendixPriceData(
                keywords_data = dataforseo_client.models.appendix_keywords_data_price_data.AppendixKeywordsDataPriceData(
                    tasks_ready = dataforseo_client.models.appendix_task_keywords_data_price_data_info.AppendixTaskKeywordsDataPriceDataInfo(
                        priority_low = [
                            dataforseo_client.models.appendix_priority_tasks_ready_keywords_data_price_data_info.AppendixPriorityTasksReadyKeywordsDataPriceDataInfo(
                                cost_type = '', 
                                cost = 1.337, )
                            ], 
                        priority_normal = [
                            dataforseo_client.models.appendix_priority_tasks_ready_keywords_data_price_data_info.AppendixPriorityTasksReadyKeywordsDataPriceDataInfo(
                                cost_type = '', 
                                cost = 1.337, )
                            ], 
                        priority_high = [
                            
                            ], ), 
                    ad_traffic_by_keywords = dataforseo_client.models.appendix_keywords_keywords_data_price_data_info.AppendixKeywordsKeywordsDataPriceDataInfo(
                        task_get = dataforseo_client.models.appendix_task_keywords_data_price_data_info.AppendixTaskKeywordsDataPriceDataInfo(), 
                        task_post = , ), 
                    bing = dataforseo_client.models.appendix_bing_keywords_data_price_data.AppendixBingKeywordsDataPriceData(
                        keyword_performance = dataforseo_client.models.appendix_keyword_bing_keywords_data_price_data_info.AppendixKeywordBingKeywordsDataPriceDataInfo(
                            live = , ), 
                        keywords_for_keywords = dataforseo_client.models.appendix_keyword_bing_keywords_data_price_data_info.AppendixKeywordBingKeywordsDataPriceDataInfo(), 
                        keywords_for_site = , 
                        search_volume_history = , 
                        search_volume = , ), 
                    categories = , 
                    errors = , 
                    google_ads = dataforseo_client.models.appendix_google_ads_keywords_data_price_data.AppendixGoogleAdsKeywordsDataPriceData(
                        status = , ), 
                    keyword_performance = dataforseo_client.models.appendix_keyword_performance_keywords_data_price_data.AppendixKeywordPerformanceKeywordsDataPriceData(
                        locations_and_languages = , ), 
                    keywords_for_keywords = dataforseo_client.models.appendix_keywords_keywords_data_price_data_info.AppendixKeywordsKeywordsDataPriceDataInfo(), 
                    keywords_for_site = , 
                    languages = , 
                    locations = , 
                    search_volume_history = , 
                    search_volume = , 
                    dataforseo_trends = dataforseo_client.models.appendix_dataforseo_trends_keywords_data_price_data.AppendixDataforseoTrendsKeywordsDataPriceData(
                        demography = , 
                        explore = , 
                        merged_data = , 
                        subregion_interests = , ), 
                    explore = dataforseo_client.models.appendix_explore_keywords_data_price_data.AppendixExploreKeywordsDataPriceData(), ),
                merchant = dataforseo_client.models.appendix_merchant_price_data.AppendixMerchantPriceData(
                    google = dataforseo_client.models.appendix_google_merchant_price_data.AppendixGoogleMerchantPriceData(
                        product_info = dataforseo_client.models.appendix_price_data_info.AppendixPriceDataInfo(
                            task_get = dataforseo_client.models.appendix_task_get_price_data_info.AppendixTaskGetPriceDataInfo(
                                advanced = dataforseo_client.models.appendix_task_keywords_data_price_data_info.AppendixTaskKeywordsDataPriceDataInfo(
                                    priority_low = [
                                        dataforseo_client.models.appendix_priority_tasks_ready_keywords_data_price_data_info.AppendixPriorityTasksReadyKeywordsDataPriceDataInfo(
                                            cost_type = '', 
                                            cost = 1.337, )
                                        ], 
                                    priority_normal = [
                                        dataforseo_client.models.appendix_priority_tasks_ready_keywords_data_price_data_info.AppendixPriorityTasksReadyKeywordsDataPriceDataInfo(
                                            cost_type = '', 
                                            cost = 1.337, )
                                        ], 
                                    priority_high = [
                                        
                                        ], ), ), 
                            tasks_ready = dataforseo_client.models.appendix_task_keywords_data_price_data_info.AppendixTaskKeywordsDataPriceDataInfo(), 
                            task_post = , ), 
                        product_spec = dataforseo_client.models.appendix_product_google_merchant_price_data_info.AppendixProductGoogleMerchantPriceDataInfo(), 
                        products = dataforseo_client.models.appendix_product_google_merchant_price_data_info.AppendixProductGoogleMerchantPriceDataInfo(), 
                        sellers = dataforseo_client.models.appendix_sellers_google_merchant_price_data.AppendixSellersGoogleMerchantPriceData(
                            ad_url = , ), ), 
                    amazon = dataforseo_client.models.appendix_amazon_merchant_price_data.AppendixAmazonMerchantPriceData(
                        asin = , ), 
                    errors = , 
                    languages = , 
                    locations = , 
                    reviews = , ),
                serp = dataforseo_client.models.appendix_serp_price_data.AppendixSerpPriceData(
                    tasks_fixed = dataforseo_client.models.appendix_task_keywords_data_price_data_info.AppendixTaskKeywordsDataPriceDataInfo(
                        priority_low = [
                            dataforseo_client.models.appendix_priority_tasks_ready_keywords_data_price_data_info.AppendixPriorityTasksReadyKeywordsDataPriceDataInfo(
                                cost_type = '', 
                                cost = 1.337, )
                            ], 
                        priority_normal = [
                            dataforseo_client.models.appendix_priority_tasks_ready_keywords_data_price_data_info.AppendixPriorityTasksReadyKeywordsDataPriceDataInfo(
                                cost_type = '', 
                                cost = 1.337, )
                            ], 
                        priority_high = [
                            
                            ], ), 
                    errors = dataforseo_client.models.appendix_task_keywords_data_price_data_info.AppendixTaskKeywordsDataPriceDataInfo(), 
                    jobs = dataforseo_client.models.appendix_keywords_keywords_data_price_data_info.AppendixKeywordsKeywordsDataPriceDataInfo(
                        task_get = , 
                        task_post = , ), 
                    languages = , 
                    live = dataforseo_client.models.appendix_serp_price_data_info.AppendixSerpPriceDataInfo(
                        regular = , 
                        advanced = , 
                        html = , ), 
                    locations = , 
                    screenshot = , 
                    task_get = dataforseo_client.models.appendix_serp_price_data_info.AppendixSerpPriceDataInfo(), 
                    task_post = , 
                    tasks_ready = , ),
                appendix = dataforseo_client.models.appendix_appendix_price_data.AppendixAppendixPriceData(
                    errors = dataforseo_client.models.appendix_task_keywords_data_price_data_info.AppendixTaskKeywordsDataPriceDataInfo(
                        priority_low = [
                            dataforseo_client.models.appendix_priority_tasks_ready_keywords_data_price_data_info.AppendixPriorityTasksReadyKeywordsDataPriceDataInfo(
                                cost_type = '', 
                                cost = 1.337, )
                            ], 
                        priority_normal = [
                            dataforseo_client.models.appendix_priority_tasks_ready_keywords_data_price_data_info.AppendixPriorityTasksReadyKeywordsDataPriceDataInfo(
                                cost_type = '', 
                                cost = 1.337, )
                            ], 
                        priority_high = [
                            
                            ], ), 
                    user_data = dataforseo_client.models.appendix_task_keywords_data_price_data_info.AppendixTaskKeywordsDataPriceDataInfo(), ),
                app_data = dataforseo_client.models.appendix_app_data_price_data.AppendixAppDataPriceData(
                    app_info = dataforseo_client.models.appendix_product_google_merchant_price_data_info.AppendixProductGoogleMerchantPriceDataInfo(
                        task_get = dataforseo_client.models.appendix_task_get_product_google_merchant_price_data_info.AppendixTaskGetProductGoogleMerchantPriceDataInfo(
                            advanced = dataforseo_client.models.appendix_task_keywords_data_price_data_info.AppendixTaskKeywordsDataPriceDataInfo(
                                priority_low = [
                                    dataforseo_client.models.appendix_priority_tasks_ready_keywords_data_price_data_info.AppendixPriorityTasksReadyKeywordsDataPriceDataInfo(
                                        cost_type = '', 
                                        cost = 1.337, )
                                    ], 
                                priority_normal = [
                                    dataforseo_client.models.appendix_priority_tasks_ready_keywords_data_price_data_info.AppendixPriorityTasksReadyKeywordsDataPriceDataInfo(
                                        cost_type = '', 
                                        cost = 1.337, )
                                    ], 
                                priority_high = [
                                    
                                    ], ), 
                            html = dataforseo_client.models.appendix_task_keywords_data_price_data_info.AppendixTaskKeywordsDataPriceDataInfo(), ), 
                        task_post = , 
                        tasks_ready = , ), 
                    app_list = dataforseo_client.models.appendix_product_google_merchant_price_data_info.AppendixProductGoogleMerchantPriceDataInfo(), 
                    app_reviews = dataforseo_client.models.appendix_price_data_info.AppendixPriceDataInfo(), 
                    app_searches = , 
                    categories = , 
                    errors = , 
                    languages = , 
                    locations = , ),
                backlinks = dataforseo_client.models.appendix_backlinks_price_data.AppendixBacklinksPriceData(
                    anchors = dataforseo_client.models.appendix_keyword_bing_keywords_data_price_data_info.AppendixKeywordBingKeywordsDataPriceDataInfo(
                        live = dataforseo_client.models.appendix_task_keywords_data_price_data_info.AppendixTaskKeywordsDataPriceDataInfo(
                            priority_low = [
                                dataforseo_client.models.appendix_priority_tasks_ready_keywords_data_price_data_info.AppendixPriorityTasksReadyKeywordsDataPriceDataInfo(
                                    cost_type = '', 
                                    cost = 1.337, )
                                ], 
                            priority_normal = [
                                dataforseo_client.models.appendix_priority_tasks_ready_keywords_data_price_data_info.AppendixPriorityTasksReadyKeywordsDataPriceDataInfo(
                                    cost_type = '', 
                                    cost = 1.337, )
                                ], 
                            priority_high = [
                                
                                ], ), ), 
                    backlinks = dataforseo_client.models.appendix_keyword_bing_keywords_data_price_data_info.AppendixKeywordBingKeywordsDataPriceDataInfo(), 
                    bulk_backlinks = , 
                    bulk_new_lost_backlinks = , 
                    bulk_new_lost_referring_domains = , 
                    bulk_pages_summary = , 
                    bulk_ranks = , 
                    bulk_referring_domains = , 
                    competitors = , 
                    content_duplicates = , 
                    domain_intersection = , 
                    domain_pages = , 
                    domain_pages_summary = , 
                    errors = dataforseo_client.models.appendix_task_keywords_data_price_data_info.AppendixTaskKeywordsDataPriceDataInfo(), 
                    history = , 
                    page_intersection = , 
                    referring_domains = , 
                    referring_networks = , 
                    summary = , 
                    timeseries_new_lost_summary = , 
                    timeseries_summary = , ),
                business_data = dataforseo_client.models.appendix_business_data_price_data.AppendixBusinessDataPriceData(
                    business_listings = dataforseo_client.models.appendix_business_listings_business_data_price_data.AppendixBusinessListingsBusinessDataPriceData(
                        categories = dataforseo_client.models.appendix_task_keywords_data_price_data_info.AppendixTaskKeywordsDataPriceDataInfo(
                            priority_low = [
                                dataforseo_client.models.appendix_priority_tasks_ready_keywords_data_price_data_info.AppendixPriorityTasksReadyKeywordsDataPriceDataInfo(
                                    cost_type = '', 
                                    cost = 1.337, )
                                ], 
                            priority_normal = [
                                dataforseo_client.models.appendix_priority_tasks_ready_keywords_data_price_data_info.AppendixPriorityTasksReadyKeywordsDataPriceDataInfo(
                                    cost_type = '', 
                                    cost = 1.337, )
                                ], 
                            priority_high = [
                                
                                ], ), 
                        categories_aggregation = dataforseo_client.models.appendix_keyword_bing_keywords_data_price_data_info.AppendixKeywordBingKeywordsDataPriceDataInfo(
                            live = dataforseo_client.models.appendix_task_keywords_data_price_data_info.AppendixTaskKeywordsDataPriceDataInfo(), ), 
                        locations = , 
                        search = dataforseo_client.models.appendix_keyword_bing_keywords_data_price_data_info.AppendixKeywordBingKeywordsDataPriceDataInfo(), ), 
                    errors = , 
                    social_media = dataforseo_client.models.appendix_social_media_business_data_price_data.AppendixSocialMediaBusinessDataPriceData(
                        facebook = , 
                        pinterest = , 
                        reddit = , ), 
                    google = dataforseo_client.models.appendix_google_business_data_price_data.AppendixGoogleBusinessDataPriceData(
                        hotel_info = dataforseo_client.models.appendix_hotel_info_google_business_data_price_data.AppendixHotelInfoGoogleBusinessDataPriceData(
                            task_get = dataforseo_client.models.appendix_task_get_product_google_merchant_price_data_info.AppendixTaskGetProductGoogleMerchantPriceDataInfo(
                                advanced = , 
                                html = , ), 
                            task_post = , 
                            tasks_ready = , ), 
                        hotel_searches = dataforseo_client.models.appendixs_google_business_data_price_data_info.AppendixsGoogleBusinessDataPriceDataInfo(), 
                        my_business_info = dataforseo_client.models.appendixs_google_business_data_price_data_info.AppendixsGoogleBusinessDataPriceDataInfo(), 
                        my_business_updates = , 
                        questions_and_answers = , 
                        reviews = , ), 
                    languages = , 
                    locations = , 
                    tripadvisor = dataforseo_client.models.appendix_tr_business_data_price_data_info.AppendixTrBusinessDataPriceDataInfo(), 
                    trustpilot = dataforseo_client.models.appendix_tr_business_data_price_data_info.AppendixTrBusinessDataPriceDataInfo(), 
                    yelp = , ),
                content_analysis = dataforseo_client.models.appendix_content_analysis_price_data.AppendixContentAnalysisPriceData(
                    categories = dataforseo_client.models.appendix_task_keywords_data_price_data_info.AppendixTaskKeywordsDataPriceDataInfo(
                        priority_low = [
                            dataforseo_client.models.appendix_priority_tasks_ready_keywords_data_price_data_info.AppendixPriorityTasksReadyKeywordsDataPriceDataInfo(
                                cost_type = '', 
                                cost = 1.337, )
                            ], 
                        priority_normal = [
                            dataforseo_client.models.appendix_priority_tasks_ready_keywords_data_price_data_info.AppendixPriorityTasksReadyKeywordsDataPriceDataInfo(
                                cost_type = '', 
                                cost = 1.337, )
                            ], 
                        priority_high = [
                            
                            ], ), 
                    category_trends = dataforseo_client.models.appendix_keyword_bing_keywords_data_price_data_info.AppendixKeywordBingKeywordsDataPriceDataInfo(
                        live = dataforseo_client.models.appendix_task_keywords_data_price_data_info.AppendixTaskKeywordsDataPriceDataInfo(), ), 
                    errors = , 
                    languages = , 
                    locations = , 
                    phrase_trends = dataforseo_client.models.appendix_keyword_bing_keywords_data_price_data_info.AppendixKeywordBingKeywordsDataPriceDataInfo(), 
                    rating_distribution = , 
                    search = , 
                    sentiment_analysis = , 
                    summary = , ),
                content_generation = dataforseo_client.models.appendix_content_generation_price_data.AppendixContentGenerationPriceData(
                    check_grammar = dataforseo_client.models.appendix_content_generation_price_data_info.AppendixContentGenerationPriceDataInfo(
                        live = dataforseo_client.models.appendix_task_keywords_data_price_data_info.AppendixTaskKeywordsDataPriceDataInfo(
                            priority_low = [
                                dataforseo_client.models.appendix_priority_tasks_ready_keywords_data_price_data_info.AppendixPriorityTasksReadyKeywordsDataPriceDataInfo(
                                    cost_type = '', 
                                    cost = 1.337, )
                                ], 
                            priority_normal = [
                                dataforseo_client.models.appendix_priority_tasks_ready_keywords_data_price_data_info.AppendixPriorityTasksReadyKeywordsDataPriceDataInfo(
                                    cost_type = '', 
                                    cost = 1.337, )
                                ], 
                            priority_high = [
                                
                                ], ), 
                        languages = dataforseo_client.models.appendix_task_keywords_data_price_data_info.AppendixTaskKeywordsDataPriceDataInfo(), ), 
                    generate = dataforseo_client.models.appendix_keyword_bing_keywords_data_price_data_info.AppendixKeywordBingKeywordsDataPriceDataInfo(), 
                    generate_meta_tags = dataforseo_client.models.appendix_keyword_bing_keywords_data_price_data_info.AppendixKeywordBingKeywordsDataPriceDataInfo(), 
                    generate_sub_topics = , 
                    generate_text = , 
                    paraphrase = , 
                    text_summary = dataforseo_client.models.appendix_content_generation_price_data_info.AppendixContentGenerationPriceDataInfo(), ),
                dataforseo_labs = dataforseo_client.models.appendix_dataforseo_labs_price_data.AppendixDataforseoLabsPriceData(
                    app_competitors = dataforseo_client.models.appendix_keyword_bing_keywords_data_price_data_info.AppendixKeywordBingKeywordsDataPriceDataInfo(
                        live = dataforseo_client.models.appendix_task_keywords_data_price_data_info.AppendixTaskKeywordsDataPriceDataInfo(
                            priority_low = [
                                dataforseo_client.models.appendix_priority_tasks_ready_keywords_data_price_data_info.AppendixPriorityTasksReadyKeywordsDataPriceDataInfo(
                                    cost_type = '', 
                                    cost = 1.337, )
                                ], 
                            priority_normal = [
                                dataforseo_client.models.appendix_priority_tasks_ready_keywords_data_price_data_info.AppendixPriorityTasksReadyKeywordsDataPriceDataInfo(
                                    cost_type = '', 
                                    cost = 1.337, )
                                ], 
                            priority_high = [
                                
                                ], ), ), 
                    app_intersection = dataforseo_client.models.appendix_keyword_bing_keywords_data_price_data_info.AppendixKeywordBingKeywordsDataPriceDataInfo(), 
                    bulk_app_metrics = , 
                    bulk_keyword_difficulty = , 
                    bulk_search_volume = , 
                    bulk_traffic_estimation = , 
                    categories = dataforseo_client.models.appendix_task_keywords_data_price_data_info.AppendixTaskKeywordsDataPriceDataInfo(), 
                    categories_for_domain = , 
                    competitors_domain = , 
                    domain_intersection = , 
                    domain_metrics_by_categories = , 
                    domain_rank_overview = , 
                    domain_whois_overview = , 
                    errors = , 
                    historical_rank_overview = , 
                    historical_search_volume = , 
                    historical_serps = , 
                    keyword_ideas = , 
                    keywords_for_app = , 
                    keywords_for_categories = , 
                    keywords_for_site = , 
                    keyword_suggestions = , 
                    locations_and_languages = , 
                    page_intersection = , 
                    product_competitors = , 
                    product_keyword_intersections = , 
                    product_rank_overview = , 
                    ranked_keywords = , 
                    related_keywords = , 
                    relevant_pages = , 
                    search_intent = , 
                    serp_competitors = , 
                    subdomains = , 
                    top_searches = , ),
                domain_analytics = dataforseo_client.models.appendix_domain_analytics_price_data.AppendixDomainAnalyticsPriceData(
                    whois = dataforseo_client.models.appendix_whois_domain_analytics_price_data.AppendixWhoisDomainAnalyticsPriceData(
                        overview = dataforseo_client.models.appendix_keyword_bing_keywords_data_price_data_info.AppendixKeywordBingKeywordsDataPriceDataInfo(
                            live = dataforseo_client.models.appendix_task_keywords_data_price_data_info.AppendixTaskKeywordsDataPriceDataInfo(
                                priority_low = [
                                    dataforseo_client.models.appendix_priority_tasks_ready_keywords_data_price_data_info.AppendixPriorityTasksReadyKeywordsDataPriceDataInfo(
                                        cost_type = '', 
                                        cost = 1.337, )
                                    ], 
                                priority_normal = [
                                    dataforseo_client.models.appendix_priority_tasks_ready_keywords_data_price_data_info.AppendixPriorityTasksReadyKeywordsDataPriceDataInfo(
                                        cost_type = '', 
                                        cost = 1.337, )
                                    ], 
                                priority_high = [
                                    
                                    ], ), ), ), 
                    technologies = dataforseo_client.models.appendix_technologies_domain_analytics_price_data.AppendixTechnologiesDomainAnalyticsPriceData(
                        languages = dataforseo_client.models.appendix_task_keywords_data_price_data_info.AppendixTaskKeywordsDataPriceDataInfo(), 
                        locations = , 
                        aggregation_technologies = dataforseo_client.models.appendix_keyword_bing_keywords_data_price_data_info.AppendixKeywordBingKeywordsDataPriceDataInfo(), 
                        domains_by_html_terms = , 
                        domains_by_technology = , 
                        domain_technologies = , 
                        technologies_summary = , 
                        technology_stats = , ), 
                    errors = , 
                    tasks_ready = , ),
                on_page = dataforseo_client.models.appendix_on_page_price_data.AppendixOnPagePriceData(
                    errors = dataforseo_client.models.appendix_task_keywords_data_price_data_info.AppendixTaskKeywordsDataPriceDataInfo(
                        priority_low = [
                            dataforseo_client.models.appendix_priority_tasks_ready_keywords_data_price_data_info.AppendixPriorityTasksReadyKeywordsDataPriceDataInfo(
                                cost_type = '', 
                                cost = 1.337, )
                            ], 
                        priority_normal = [
                            dataforseo_client.models.appendix_priority_tasks_ready_keywords_data_price_data_info.AppendixPriorityTasksReadyKeywordsDataPriceDataInfo(
                                cost_type = '', 
                                cost = 1.337, )
                            ], 
                        priority_high = [
                            
                            ], ), 
                    lighthouse = dataforseo_client.models.appendixs_google_business_data_price_data_info.AppendixsGoogleBusinessDataPriceDataInfo(
                        live = dataforseo_client.models.appendix_task_keywords_data_price_data_info.AppendixTaskKeywordsDataPriceDataInfo(), 
                        task_get = , 
                        task_post = , 
                        tasks_ready = , ), 
                    content_parsing = , 
                    content_parsing_live = , 
                    duplicate_content = , 
                    duplicate_tags = , 
                    instant_pages = , 
                    keyword_density = , 
                    links = , 
                    non_indexable = , 
                    pages = , 
                    pages_by_resource = , 
                    page_screenshot = , 
                    raw_html = , 
                    redirect_chains = , 
                    resources = , 
                    summary = , 
                    task_post = , 
                    tasks_ready = , 
                    waterfall = , )
            )
        else:
            return AppendixPriceData(
        )
        """

    def testAppendixPriceData(self):
        """Test AppendixPriceData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

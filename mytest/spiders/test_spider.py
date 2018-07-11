# -*- coding: utf-8 -*-
import scrapy


class TestSpiderSpider(scrapy.Spider):
    name = 'test_spider'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://zhihu.com/']

    def parse(self, response):
        pass

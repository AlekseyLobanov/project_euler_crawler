# -*- coding: utf-8 -*-

import scrapy

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from euler_parser.items import EulerItem

class EulerSpider(CrawlSpider):
    name = "euler"
    allowed_domains = ["projecteuler.net"]
    start_urls = [
        "https://projecteuler.net/archives",
    ]
    rules = (
        Rule(LinkExtractor(allow=("/archives.+"),),follow=True),
        Rule(LinkExtractor(allow=("/problem=.+", )),callback='parse_item',follow=True),
    )

    def parse_item(self, response):
        item = EulerItem()
        item['index'] = response.xpath("/html/head/title").extract()[0].split()[1]
        item['name'] = response.xpath("//h2/text()").extract()[0]
        cond = u""
        for i in response.xpath('//div[@role="problem"]/*').extract():
            cond += i
        item['condition'] = cond
        return item

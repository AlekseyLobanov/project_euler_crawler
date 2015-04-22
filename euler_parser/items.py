# -*- coding: utf-8 -*-

import scrapy

class EulerItem(scrapy.Item):
    index = scrapy.Field()
    name = scrapy.Field()
    condition = scrapy.Field()

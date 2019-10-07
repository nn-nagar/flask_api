# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuetetutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    name = scrapy.Field()
    market_cap = scrapy.Field()
    price = scrapy.Field()
    volume = scrapy.Field()
    circulating_supply = scrapy.Field()
    change = scrapy.Field()

    pass

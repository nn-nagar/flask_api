import scrapy
from ..items import QuetetutorialItem

class QueteSpider(scrapy.Spider):
    name = 'quetes'
    start_urls = [
        'https://coinmarketcap.com/'
    ]

    def parse(self,response):
        items = QuetetutorialItem()
        for i in range(100):

            name = response.css("a.currency-name-container::text").extract()
            market_cap = response.css("td.market-cap::text").extract()
            price = response.css("a.price::text").extract()
            volume = response.css("a.volume::text").extract()
            circulating_supply = response.css("span::text")[151:].extract()
            change = response.css("td.percent-change::text").extract()

            items['id'] = i
            items['name'] = name[i]
            items['market_cap'] = market_cap[i]
            items['price'] = price[i]
            items['volume'] = volume[i]
            items['circulating_supply'] = circulating_supply[i]
            items['change'] = change[i]

            yield items

            # yield {
            #         'id': i,
            #         'name':name[i],
            #         'market_cap':market_cap[i],
            #         'price':price[i],
            #         'volume':volume[i],
            #         'circulating_supply':circulating_supply[i],
            #         'change':change[i]
            #     }


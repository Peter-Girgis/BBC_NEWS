from scrapy import Spider
from scrapy.selector import Selector
from BBC_NEWS.items import StackItem, GuardianItem



class BBC_NEWS_Spider(Spider):
    name = "BBC_NEWS"
    allowed_domains = ["www.bbc.com"]
    start_urls = [
        "https://www.bbc.com/news", ]

    def parse(self, response):
        articles = response.xpath("//div" )

        for article in articles:
            item = GuardianItem()
            item['Article_Title'] = article.xpath('normalize-space(div/a/h3/text())').extract_first()
            item['Article_Summary'] = article.xpath('normalize-space(div/p/text())').extract_first()
            item['Article_Time_published'] = article.xpath('normalize-space(ul/li/span/time/@datetime)').extract_first()
            item['Article_Time'] = article.xpath('normalize-space(ul/li/span/time/span[1]/text())').extract_first()
            item['Aricle_Country'] = article.xpath('normalize-space(ul/li/a/@aria-label)').extract_first().replace('From ','').split()
            #item['Article_URL'] = 'https://www.bbc.com' + article.xpath('normalize-space(div/a/@href)').extract_first()
            item['Article_URL'] = article.xpath('normalize-space(div/a/@href)').extract_first()
            item['Article_URL'] = 'https://www.bbc.com' + item['Article_URL']
            yield item

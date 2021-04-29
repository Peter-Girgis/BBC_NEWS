# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy.item import Item, Field

# define the fields for your item here like:
# name = scrapy.Field()
class StackItem(scrapy.Item):
    Article_Title = Field()
    Article_Summary = Field()
    Article_Time_published = Field()
    Article_Time = Field()
    Aricle_Country = Field()
    Article_URL = Field()
    pass

# define the fields for your item here like:
# name = scrapy.Field()
class GuardianItem(scrapy.Item):
    Article_Title = Field()
    Article_Summary = Field()
    Article_Time_published = Field()
    Article_Time = Field()
    Aricle_Country = Field()
    Article_URL = Field()
    pass

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
#import pickle
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter
from scrapy.exceptions import DropItem
from BBC_NEWS.exporters import FanItemExporter
from scrapy import settings
import json
import codecs

#from scrapy import log
import logging
logging.warning("This is a warning")



class MongoPipeline(object):

    collection_name = 'BBCNEWS'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        ## pull in information from settings.py
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        ## initializing spider
        ## opening db connection
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        ## clean up when spider is closed
        self.client.close()

    def process_item(self, item, spider):
        ## how to handle each post
        self.db[self.collection_name].insert(dict(item))
        logging.debug("Post added to MongoDB")
        return item


# class to remove all duplication items (Title) or items have empty data.
class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item["Article_Title"] in self.ids_seen or item["Article_Title"] in 'empty' :
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item["Article_Title"])
        return item


class FanExportPipeline(object):
    def __init__(self, file_name):
        # Storing output filename
        self.file_name = file_name
        # Creating a file handle and setting it to None
        self.file_handle = None

    @classmethod
    def from_crawler(cls, crawler):
        # getting the value of FILE_NAME field from settings.py
        output_file_name = crawler.settings.get('FILE_NAME')

        # cls() calls FanExportPipeline's constructor
        # Returning a FanExportPipeline object
        return cls(output_file_name)

    def open_spider(self, spider):
        print('Custom export opened')

        # Opening file in binary-write mode
        file = open(self.file_name, 'wb')
        self.file_handle = file

        # Creating a FanItemExporter object and initiating export
        self.exporter = FanItemExporter(file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        print('Custom Exporter closed')

        # Ending the export to file from FanItemExport object
        self.exporter.finish_exporting()

        # Closing the opened output file
        self.file_handle.close()

    def process_item(self, item, spider):
        # passing the item to FanItemExporter object for expoting to file
        self.exporter.export_item(item)
        return item

# BBC NEWS CRAWLER
BBC News Content Collect and Store

## Details
  * This Python Application crawls BBC online news website using the SCRAPY crawler framework (http://scrapy.org/).
  * This appliction cleans the news articles to obtain only information relevant to the news story,
    e.g. News URL, News Text, News Headline, Author and Countries mentioned in news article.
  * News articles crawled are stored in Mongo Database hosted at (https://cloud.mongodb.com/v2/6088878fb4369139d0f7a513#clusters).
  * Search REST APIs are provided, to access the data stored at the mongo database. 
    * Using the search REST API, end user can fetch:
      * All the news articles in data base.
      * News Articles with a given keyword in News Text.
      * News Articles with a given keyword in News Headline.

## Directory Structure:
  * Directory ``BBC_NEWS/BBC_NEWS/spiders``: 
    * Contains the Scrapy Spider for BBC News Website.
  * Directory ``BBC_NEWS``: 
    * This directory have 'BBC_NEWS.json' file created at runtime.
    * It contains the output json file including the data cawled from BBC News Website.
  * Directory ```BBC_NEWS/BBC_NEWS```:
    * This directory contains script ```exporters.py``` 
      1. Extending JsonLinesItemExporter.  
      2. JsonLinesItemExporter provides the exact same implementation of export_item() method.
      3. Therefore only start_exporting() and finish_exporting() methods are overrided.
    
    * This directory contains script ```items.py``` 
      1. define the fields for your item by using (StackItem , GuardianItem).
    
    * This directory contains script ```middlewares.py```
      1. useful for handling different item types with a single interface with (BbcNewsSpiderMiddleware, BbcNewsDownloaderMiddleware).

    * This directory contains script ```pipelines.py```
      1. managing  classe MongoPipeline for API access mongo db programatically.
      2. managing  classe DuplicatesPipeline for removing any duplication information and cleanse the page of superfluous content such as advertising and HTML.
      3. managing  classe  FanExportPipeline for getting data field from ```settings.py```
    
    * This directory contains script ```settings.py```
      1. Identify Obey robots.txt rules.
      2. Identify Configure maximum concurrent requests performed by Scrapy.
      3. Identify delay for requests for the same website.
      4. Identify the output file path at (FILE_NAME).
      5. Identify ITEM_PIPELINES (DuplicatesPipeline, FanExportPipeline,MongoPipeline)
      6. Identify Mongo API URI (MONGO_URI, MONGO_DATABASE)
      7. Identify the output column category at (FEED_EXPORT_FIELDS).
      
      
  
## Execution:
 To execute BBC News Website Crawler,and save data locally at spefic path then upload it at mongo database by just execute the ```scrapy crawl BBC_NEWS``` only.

 

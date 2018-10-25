#!/usr/bin/env python
from scrapy.crawler import CrawlerProcess

from src.spiders.tsunami_spider import TsunamiSpider

process = CrawlerProcess()
process.crawl(TsunamiSpider)
process.start()

# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 16:42:15 2023

@author: LENOVO
"""

import scrapy

from scrapy.item import Item, Field

from scrapy.loader import ItemLoader


class IMDb_Movies(scrapy.Spider):
    name = "imdb_movies"
    def start_requests(self):
    
        start_urls = ["https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=action&sort=user_rating,desc&start=01&ref_=adv_nxt"]
    
        for url in start_urls:
            yield scrapy.Request(url = url, callback=self.parse)
        
    def parse(self,response):
        pass
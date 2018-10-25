import json
import os

import scrapy

from items.Tsunami import Tsunami

#BASE_URL = 'http://tsun.sscc.ru/tsunami-database/index.php/?YR%5Bfrom%5D=-6000&YR%5Bto%5D=2017&Dep%5Bfrom%5D=0&Dep%5Bto%5D=600&Ms%5Bfrom%5D=3.2&Ms%5Bto%5D=9.3&I%5Bfrom%5D=-5&I%5Bto%5D=4.5&M%5Bfrom%5D=-4&M%5Bto%5D=9&Hmax%5Bfrom%5D=0&Hmax%5Bto%5D=525&Mw%5Bfrom%5D=5.3&Mw%5Bto%5D=9.6&Mt%5Bfrom%5D=6&Mt%5Bto%5D=9.4&Lat%5Bfrom%5D=-90&Lat%5Bto%5D=90&Lon%5Bfrom%5D=-180&Lon%5Bto%5D=180&N%5Bfrom%5D=0&N%5Bto%5D=5772&TR=&BR=&SR%5Bcontain%5D=&d%5Bin%5D%5B%5D=N&d%5Bin%5D%5B%5D=S&d%5Bin%5D%5B%5D=M&d%5Bin%5D%5B%5D=H&V%5Bfrom%5D=0&V%5Bto%5D=4&limit=All&Search=&search=Search+Database'
BASE_URL = 'http://tsun.sscc.ru/tsunami-database/index.php/?YR%5Bfrom%5D=2017&YR%5Bto%5D=2017&Dep%5Bfrom%5D=0&Dep%5Bto%5D=600&Ms%5Bfrom%5D=3.2&Ms%5Bto%5D=9.3&I%5Bfrom%5D=-5&I%5Bto%5D=4.5&M%5Bfrom%5D=-4&M%5Bto%5D=9&Hmax%5Bfrom%5D=0&Hmax%5Bto%5D=525&Mw%5Bfrom%5D=5.3&Mw%5Bto%5D=9.6&Mt%5Bfrom%5D=6&Mt%5Bto%5D=9.4&Lat%5Bfrom%5D=-90&Lat%5Bto%5D=90&Lon%5Bfrom%5D=-180&Lon%5Bto%5D=180&N%5Bfrom%5D=0&N%5Bto%5D=5772&TR=&BR=&SR%5Bcontain%5D=&d%5Bin%5D%5B%5D=N&d%5Bin%5D%5B%5D=S&d%5Bin%5D%5B%5D=M&d%5Bin%5D%5B%5D=H&V%5Bfrom%5D=0&V%5Bto%5D=4&limit=25&Search=&search=Search+Database'


class TsunamiSpider(scrapy.Spider):
    name = "tsunami"

    def start_requests(self):
        yield scrapy.Request(url=BASE_URL, callback=self.parse)

    def parse(self, response):
        tsunamis = []
        rows = response.css(".results tr")[1:-1]
        for row in rows:
            items = row.css("td::text, td:empty")
            tsunamis.append(Tsunami(items).__dict__)

        print(os.path.relpath())
        with open('../data.json', 'w') as outfile:
            json.dump(tsunamis, outfile, indent=4, sort_keys=True)

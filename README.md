# Project Euler Crawler
It is a very simple crawler for [Project Euler](https://projecteuler.net). It collects only conditions of problems and their numbers.

Crawled data stored in `output` dir.

## Dependencies
Requires only [scrapy](http://scrapy.org/).

## Using
If you want recrawl data you need type:

    scrapy crawl euler -o PATH_TO_FILE.csv
or 

    scrapy crawl euler -o PATH_TO_FILE.xml

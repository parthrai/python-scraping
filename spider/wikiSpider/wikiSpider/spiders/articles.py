import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor



class ArticleSpider(CrawlSpider):
    name = 'articles'
    allowed_domains = ['wikipedia.org']

    start_urls = ['https://en.wikipedia.org/wiki/'

                  ]

    rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse_items',follow=True)]

    def parse_items(self,response):
        url = response.url
        title = response.css('h1::text').extract_first()
        text = response.xpath('//div[@id="mw-content-text"]//text()').extract()
        lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
        lastUpdated = lastUpdated.replace('This page was last edited on ','')

        print('URL is: {}'.format(url))
        print('title is: {} '. format(title))
        print('text is: {}'. format(text))
        print('Last Updated : {}'.format(lastUpdated))



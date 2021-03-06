import scrapy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from scrapy.spiders import BaseSpider


class BoardGameSpider(BaseSpider):

    name = 'board_games'

    custom_settings = {
        "DOWNLOAD_DELAY": 8,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 5,
        "HTTPCACHE_ENABLED": True
    }

    start_urls = [
        'https://boardgamegeek.com/browse/boardgame?sort=rank&sortdir=desc']
        #could load all the pages here
    def __init__(self, *args, **kwargs):
        super(BoardGameSpider, self).__init__(*args, **kwargs)
        chromedriver = "/Applications/chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(5)
        self.count = 0

    def parse(self, response):
        for href in response.xpath(
            '//td[@class="collection_thumbnail"]/a/@href').extract():
            yield scrapy.Request(
                url='https://boardgamegeek.com'+href,
                callback=self.parse_boardgame,
                meta={'url': 'https://boardgamegeek.com'+href})
            time.sleep(2)
        if self.count < 50:
            next_url = 'https://boardgamegeek.com'+ response.xpath('//div[@id="main_content"]/p/a[@title= "next page"]/@href').extract()[0]
            self.count += 1
            yield scrapy.Request(url=next_url,callback=self.parse)

    def parse_boardgame(self, response):
        self.driver.get(response.url)
        url = response.request.meta['url']

        title = self.driver.find_element_by_xpath('//div[@class = "game-header-title-info"]/h1/a').text

        rank = self.driver.find_element_by_xpath('//a[@ng-if = "::rankinfo.rank > 0"]').text

        rating = float(self.driver.find_element_by_xpath('//div[@class = "rating-overall-callout-container"]/a/span').text)

        game_type = self.driver.find_element_by_class_name('feature-description').text.split()

        play_time = self.driver.find_element_by_xpath('//span[@min = "::geekitemctrl.geekitem.data.item.minplaytime"]').text

        complexity = float(self.driver.find_element_by_xpath('//span[@ng-show = "geekitemctrl.geekitem.data.item.polls.boardgameweight.votes > 0"]/span').text)

        year = self.driver.find_element_by_class_name('game-year').text

        retail = self.driver.find_element_by_class_name('summary-sale-item-price-retail').text

        ebay = self.driver.find_element_by_xpath('//div[@class = "summary-sale-item-price"]/strong').text

        #goes to credits and gets full list of mechanics
        self.driver.find_element_by_link_text('See Full Credits').click()
        mechanics= self.driver.find_elements_by_class_name('outline-item-description')[7].text.split('\n')

        yield {
            'url': url,
            'rank': rank,
            'title': title,
            'rating': rating,
            'game_type': game_type,
            'time': play_time,
            'complexity': complexity,
            'year': year,
            'retail': retail,
            'ebay': ebay,
            'mechanics': mechanics
        }

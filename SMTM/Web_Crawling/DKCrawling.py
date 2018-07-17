
from wsite.notice import bobaedream, clien

class DKCrawler :

    def __init__(self):
        self.crawlers = []
        self.crawlers.append(bobaedream.WebCrawler())
        self.crawlers.append(clien.WebCrawler())

    def realTime_run(self):
        list = []
        for crawler in self.crawlers:
            crawler.run()
            list = list + crawler.get_list()

        return list

    def bobae_list(self):
        crawler = bobaedream.WebCrawler()
        crawler.run()
        return crawler.get_list()

    def clien_list(self):
        crawler = clien.WebCrawler()
        crawler.run()
        return crawler.get_list()

    # def all_site_title(self):
    #     list = []
    #     #list = list + clien_list()
    #     #list = list + bobae_list()
        
    #     return list



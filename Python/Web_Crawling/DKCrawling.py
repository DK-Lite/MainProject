
from wsite import bobaedream, clien

def bobae_list():
    crawler = bobaedream.WebCrawler()
    crawler.run()
    return crawler.get_list()

def clien_list():
    crawler = clien.WebCrawler()
    crawler.run()
    return crawler.get_list()

def all_site_title():
    list = []

    list = list + clien_list()
    list = list + bobae_list()
    
    return list


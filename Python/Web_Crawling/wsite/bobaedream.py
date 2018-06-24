#title Crawling
#clien version

from bs4 import BeautifulSoup
import requests

BOBAEDREAM_URL = 'https://www.clien.net/service/'
BOBAEDREAM_COMMUNITY_URL = 'http://www.bobaedream.co.kr/list?code=freeb'

class WebCrawler:
    
    def __init__(self):
        self.last_number = '0'
        self.title_list = []

    def run(self):
        # init
        self.title_list = []

        # approach site 
        sess = requests.Session()
        res = sess.get(BOBAEDREAM_COMMUNITY_URL)
        soup = BeautifulSoup(res.content, 'html.parser')

        # get title
        table = soup.find_all('tr', {'itemtype' : 'http://schema.org/Article'})
        table_size = len(table)
        for i in reversed(range(table_size)): 
            number = table[i].find_all('td', {'class' : 'num01'})
            title = table[i].find_all('a', {'class' : 'bsubject'})

            #select effective title 
            if( number[0].text > self.last_number ):
                self.last_number = number[0].text
                self.title_list.append("[bobae]"+title[0].text)

    def get_list(self):
        return self.title_list
        


def print_crawler(crawler):
    list = crawler.get_list()
    list_len = len(list)
    for i in range(list_len):
        print(list[i])

#debug 
TEST = 0
#site test
if TEST == 1 :
    crawler = WebCrawler()
    crawler.run()
    print_crawler(crawler)
    #return crawler.get_list()

































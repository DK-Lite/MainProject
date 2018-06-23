#title Crawling
#clien version

from bs4 import BeautifulSoup
import requests

CLIEN_URL = 'https://www.clien.net/service/'
CLIEN_COMMUNITY_URL = 'https://www.clien.net/service/group/community'

class WebCrawler:
    
    def __init__(self):
        self.last_time = '0000-00-00 00:00:00'
        self.title_list = []

    def run(self):
        # approach site 
        sess = requests.Session()
        res = sess.get(CLIEN_COMMUNITY_URL)
        soup = BeautifulSoup(res.content, 'html.parser')


        # get title
        table = soup.find_all('div', {'class' : 'list_item symph_row'})
        table_size = len(table)
        for i in reversed(range(table_size)): 
            title = table[i].find_all('span', {'data-role' : 'list-title-text'})
            #hits = table[i].find_all('span', {'class' : 'hit'})
            time = table[i].find_all('span', {'class' : 'timestamp'})

            #select effective title 
            if( time[0].text > self.last_time ):
                self.last_time = time[0].text
                self.title_list.append(title[0].text)
        
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







































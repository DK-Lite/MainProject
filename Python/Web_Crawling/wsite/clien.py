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
        # init
        self.title_list = []

        # approach site 
        sess = requests.Session()
        res = sess.get(CLIEN_COMMUNITY_URL)
        soup = BeautifulSoup(res.content, 'html.parser')


        # get title
        table = soup.find_all('div', {'class' : 'list_item symph_row'})
        table_size = len(table)
        for i in reversed(range(table_size)): 
            title = table[i].find_all('span', {'data-role' : 'list-title-text'})
            time = table[i].find_all('span', {'class' : 'timestamp'})

            #select effective title 
            if( time[0].text > self.last_time ):
                self.last_time = time[0].text
                self.title_list.append("[clien]:"+title[0].text)

        #print(self.last_time)

    def get_list(self):
        return self.title_list







































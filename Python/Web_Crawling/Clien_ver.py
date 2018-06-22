#title Crawling
#clien version

from bs4 import BeautifulSoup
import requests
import datetime

CLIEN_URL = 'https://www.clien.net/service/'
CLIEN_COMMUNITY_URL = 'https://www.clien.net/service/group/community'

def get_cur_title_list(lists, last_time):
    list = []
    list_len = len(lists)
    for i in reversed(range(list_len)):
        title = lists[i].find_all('span', {'data-role' : 'list-title-text'})
        hits = lists[i].find_all('span', {'class' : 'hit'})
        time = lists[i].find_all('span', {'class' : 'timestamp'})
        
        if( time[0].text > last_time ):
            last_time = time[0].text
            list.append(title[0].text)
    
    return list, last_time

def get_title_list(last_time):
    # Seession 생성
    with requests.Session() as s:
        res = s.get(CLIEN_COMMUNITY_URL)
        soup = BeautifulSoup(res.content, 'html.parser')
        titles = soup.find_all('div', {'class' : 'list_item symph_row'})
        cur_title_list, last_time = get_cur_title_list(titles, last_time)

    return cur_title_list, last_time





































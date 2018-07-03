import os, sys, re

from bs4 import BeautifulSoup
import requests

FOLDER_PATH = os.path.dirname(__file__) + '/'
NAVER_BREAKING_NEWS_URL = 'http://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001'


# open URL
def open_Url(URL):
    sess = requests.Session()
    res = sess.get(URL)
    soup = BeautifulSoup(res.content, 'lxml', from_encoding='utf-8')
    return soup

# get text at site
def get_text(URL) :
    html = open_Url(URL)

    #get article
    divs = html.find_all('div', {'id' : 'articleBodyContents'})

    #write text
    text = ""
    for div in divs:
        text = text + str(div.find_all(text=True)) 
 
    return text
 
 # clean text 
def clean_text(text):
    cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]','', text)
    cleaned_text = cleaned_text.strip(' \t\n\r')
    return cleaned_text

# get all headline
def get_headlines(html):

    divs = html.find_all('div', {'class' : 'list_body newsflash_body'})
    headlines = divs[0].find_all('li')

    list = []
    for headline in headlines:

        info     = headline.find_all('a')[1]

        _title   = clean_text(info.text)
        _url     = info.attrs['href']
        _article = get_text(_url)

        list.append( 
            {
                'title'     : _title,
                'url'       : _url,
                'article'   : _article
            }
        )

    return list

# refresh 
def get_refresh_site() :

    naver_html = open_Url(NAVER_BREAKING_NEWS_URL)

    return get_headlines(naver_html)

#file writer
def file_writer(path, str):
    f = open(path, 'w', encoding='utf-8')
    f.writelines(str)
    f.close()


# main fuc
def main():

    lists = get_refresh_site()
    
    for list in lists:
        file_name   = list['title'] + '.txt'
        file_text   = list['article']
        file_writer(FOLDER_PATH + file_name, file_text)


# run 
main()



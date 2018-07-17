import os, sys, re
import threading

from bs4 import BeautifulSoup
import requests

FOLDER_PATH = os.path.dirname(__file__) + '/'
NAVER_BREAKING_NEWS_URL = 'http://m.news.naver.com/officeMain.nhn'

term = 10

# open URL
def open_Url(URL):
    sess = requests.Session()
    res = sess.get(URL)
    soup = BeautifulSoup(res.content, 'lxml', from_encoding='utf-8')
    return soup

def get_effective_article(html) :

    if html.find_all('div', {'id' : 'dic_area'}):
        return html.find_all('div', {'id' : 'dic_area'})[0].text

    if html.find_all('div', {'id' : 'contentArea'}):
        return html.find_all('div', {'id' : 'contentArea'})[0].text

    if html.find_all('article', {'class' : 'main_article'}):
        return html.find_all('article', {'class' : 'main_article'})[0].text

    return ""

def get_effective_time(html) :

    if html.find_all('span', {'class' : 'media_end_head_info_datestamp_time'}):
        return html.find_all('span', {'class' : 'media_end_head_info_datestamp_time'})[0].text

    return ""

# get text in site
def get_article_parser(URL) :

    html = open_Url(URL)

    #get article and time
    _article    = get_effective_article(html)
    _time       = get_effective_time(html)

    return _article, _time
 
 # clean text 
def clean_text(text):
    cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]','', text)
    cleaned_text = cleaned_text.strip('\t')
    cleaned_text = cleaned_text.strip('\n')
    cleaned_text = cleaned_text.strip('\r')

    return cleaned_text

# get all headline
def get_headlines():

    html = open_Url(NAVER_BREAKING_NEWS_URL)
    divs = html.find_all('ul', {'class' : 'press_newsflash_ct'})
    headlines = divs[0].find_all('li')

    list = []
    for headline in headlines:

        _title              = headline.find_all('strong', {'class' : 'press_newsflash_headline'})[0].text
        _company            = headline.find_all('em', {'class' : 'press_newsflash_info_press'})[0].text
        _url                = headline.find_all('a')[0].attrs['href']
        _article, _time     = get_article_parser('http://m.news.naver.com' + _url)

        list.append( 
            {
                'title'     : _title,
                'url'       : _url,
                'article'   : _article,
                'company'   : _company,
                'time'      : _time
            }
        )

    return list

#file writer
def file_writer(path, str):
    f = open(path, 'w', encoding='utf-8')
    f.writelines(str)
    f.close()


# main fuc
def print_log(list) :
    log_msg = ""

    _title      = list['title']
    _url        = list['url']
    _article    = list['article']
    _company    = list['company']
    _time       = list['time']

    if _title == "" or _url == "" or _article == "" or _company == "" or _time == "":
        log_msg = log_msg + "--------start log--------" + "\n"
        log_msg = log_msg + "_title" + "\n"
        log_msg = log_msg + "_url" + "\n"
        log_msg = log_msg + "_article" + "\n"
        log_msg = log_msg + "_company" + "\n"
        log_msg = log_msg + "_time" + "\n"
        log_msg = log_msg + "--------end log----------" + "\n"



# def startTimer():

#     lists = get_headlines()

#     for list in lists:

#         # clean text 
#         file_name   = clean_text(list['title']) + '.txt'
#         file_text   = list['article']
#         file_writer("./" + file_name, file_text)
        
#         print_log(list)

#     # timer standard logic
#     timer = threading.Timer(term, startTimer)
#     timer.start()


 #main start point
#if __name__ == '__main__':
    #startTimer()





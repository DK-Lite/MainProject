import os, sys, re
import threading

from bs4 import BeautifulSoup
import requests

FOLDER_PATH = os.path.dirname(__file__) + '/'
NAVER_BREAKING_NEWS_URL = 'http://m.news.naver.com/officeMain.nhn'

companys = {
    'AP연합뉴스',
    'enews24',
    'EPA연합뉴스',
    'KBS 연예',
    'MBC연예',
    'MBN',
    'MK스포츠 ',
    'OSEN',
    'TV리포트',
    'YTN',
    '경향신문',
    '노컷뉴스',
    '뉴스1',
    '뉴시스',
    '데일리안',
    '매일경제',
    '머니S',
    '머니투데이',
    '서울경제',
    '스타뉴스',
    '스포츠서울',
    '스포츠조선',
    '스포티비뉴스',
    '엑스포츠뉴스',
    '여성신문',
    '연합뉴스',
    '인터풋볼',
    '조선일보',
    '조이뉴스24',
    '중앙일보',
    '파이낸셜뉴스',
    '한국경제',
    '한국경제TV',
    '한국일보',
    '헤럴드POP'
}

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

    return ""

# get text in site
def get_article_parser(URL) :

    html = open_Url(URL)

    #get article and time
    _article = get_effective_article(html)
    _time = html.find_all('span', {'class' : 'media_end_head_info_datestamp_time'})[0].text

    return _article, _time
 
 # clean text 
def clean_text(text):
    cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]','', text)
    cleaned_text = cleaned_text.strip(' \t\n\r')
    return cleaned_text

# get all headline
def get_headlines(URL):

    html = open_Url(URL)
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
def startTimer():

    lists = get_headlines(NAVER_BREAKING_NEWS_URL)

    for list in lists:

        # clean text 


        file_name   = list['company'] + '.txt'
        file_text   = list['article']
        file_writer("./" + file_name, file_text)

    # timer standard logic
    timer = threading.Timer(term, startTimer)
    timer.start()


 #main start point
if __name__ == '__main__':
    startTimer()





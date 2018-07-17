# standard
import threading

# install package
import pymongo

#user function
from DKCrawling import *
from mongodb import *
from Konlpy import *
from wsite.news.naver import *

term = 10
ip = '127.0.0.1'
port = 27017
crw = DKCrawler()
db = DKDatabase()

lastTime = '0'

companys = {
    #'AP연합뉴스',
    'enews24',
    #'EPA연합뉴스',
    'KBS 연예',
    'MBC연예',
    'MBN',
    #'MK스포츠 ',
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

def is_company(company_name):
    global companys
    for cpny in companys:
        if company_name == cpny :
            return True
    return False

def startTimer():

    global lastTime
    #get titles in all site
    #titles = crw.realTime_run()
    news_list = get_headlines()

    curTime = ""
    for news in reversed(news_list) :
        if lastTime < news['time'] and is_company(news['company']):
            print(news['title'])
            #db.insert_list(news)
            curTime = news['time']

    lastTime = curTime

    timer = threading.Timer(term, startTimer)
    timer.start()
 
 #main start point
if __name__ == '__main__':
    db.connect(ip, port)
    startTimer()

    
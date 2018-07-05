# standard
import threading

# install package
import pymongo

#user function
from DKCrawling import *
from mongodb import *
from Konlpy import *

term = 3
ip = '127.0.0.1'
port = 27017
crw = DKCrawler()
db = DKDatabase()
def startTimer():

    #get titles in all site
    titles = crw.realTime_run()

    #print titles
    for title in titles:
        db.insert_str(title)
        print("-----------------------------------------------------")
        print(title)
        print(konlpy_api(title))
        break


    # timer standard logic
    timer = threading.Timer(term, startTimer)
    timer.start()
 
 #main start point
if __name__ == '__main__':
    db.connect(ip, port)
    startTimer()

    
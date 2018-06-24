# standard
import threading

# install package
import pymongo

#user function
from DKCrawling import *

term = 3
crw = DKCrawler()
def startTimer():

    #get titles in all site
    titles = crw.realTime_run()

    #print titles
    for title in titles:
        print(title)

    # timer standard logic
    timer = threading.Timer(term, startTimer)
    timer.start()
 
 #main start point
if __name__ == '__main__':
    startTimer()

    
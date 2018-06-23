# standard
import threading

# install package
import pymongo

#user function
#from Clien_ver import *
from DKCrawling import *

term = 3

def startTimer():

    #get titles in all site
    titles = all_site_title()

    #print titles
    for i in range(len(titles)):
        print(titles[i])

    # timer standard logic
    timer = threading.Timer(term, startTimer)
    timer.start()
 

 #main start point
if __name__ == '__main__':
    startTimer()

    
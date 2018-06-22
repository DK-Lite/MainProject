# standard
import threading

# install package
import pymongo

#user function
from Clien_ver import *


  
term = 3
last_time = '0000-00-00 00:00:00'

def startTimer():
    global last_time

    clien_list, last_time = get_title_list(last_time)
    

    for i in range(len(clien_list)):
        print(clien_list[i])

    timer = threading.Timer(term, startTimer)
    timer.start()
 
if __name__ == '__main__':
    startTimer()
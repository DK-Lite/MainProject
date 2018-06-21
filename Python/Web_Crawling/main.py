from bs4 import BeautifulSoup
import urllib
import urllib.request
import urllib.parse
import requests

if __name__ == "__main__":
    print("start")




    html = urllib.urlopen('http://gall.dcinside.com/board/lists/?id=japanese')

    soup = BeautifulSoup(html, "lxml")

    print(soup) 


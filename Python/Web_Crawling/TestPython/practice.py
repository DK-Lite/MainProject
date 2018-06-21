from bs4 import BeautifulSoup
import urllib.request
import urllib.parser
import requests


WEB_URL = 'google.com'

with open("example.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

with urllib.request.urlopen(WEB_URL) as response:
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')



>>> r = requests.get(WEB_URL)
>>> r.status_code
200
>>> r.header['content-type']
'text/html; charset=UTF-8'
>>> r.encoding
'UTF-8'
>>> r.text<!DOCTPYE html>
<html class='client-nojs' lang='en' dir='ltr'>


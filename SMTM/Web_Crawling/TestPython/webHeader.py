import urllib.request
import urllib.parse
import requests

if __name__ == "__main__":
    print("start")
  

    hdr = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13F69 Safari/601.1', 
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3', 
    'Accept-Encoding': 'none', 'Accept-Language': 
    'en-US,en;q=0.8', 'Connection': 'keep-alive'}

    req = urllib.request.Request("http://www.daum.net", headers = hdr)
    data = urllib.request.urlopen(req).read() 
    print(data) 
    
    with open("./response_iphone.html", "wb") as f:
        f.write(data) 



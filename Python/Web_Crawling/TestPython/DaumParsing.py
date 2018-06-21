from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import requests

# with open("example.html") as fp:
#     soup = BeautifulSoup(fp, 'html.parser')
#     all_divs = soup.find_all('div')
#     print(all_divs)

WEB_URL = 'http://media.daum.net/digital/'
TEST_URL = 'example.html'
DAHYEON_DC_WEB_URL = 'http://gall.dcinside.com/board/lists?id=dahyeon

# with open(TEST_URL) as fp:
#     soup = BeautifulSoup(fp, 'html.parser')
#     all_divs = soup.find('div')
#     print(all_divs)

# with open(TEST_URL) as fp:
#     soup = BeautifulSoup(fp, 'html.parser')
#     ex_id_divs = soup.find('div', {'id':'ex_id'})
#     print(ex_id_divs)


from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import requests

res = requests.get(WEB_URL)
soup = BeautifulSoup(res.content, 'html.parser')

link_title = soup.find_all('a', {'class':'link_txt #article_main'})


for num in range(len(link_title)):
    print(link_title[num].get_text().strip())



# 위키피디아 크롤링

# 위피피디아 검색 → 검색 된 페이지에서 Corpus 추출 → 해당 Corpus에서 단어추출
# → 추출된 단어로 DB 삽입후 BFS 탐색 반복


import wikipediaapi as wk
import threading

from konlpy.tag import Hannanum
from data_manager import dataManager

class WikiPaser:

    def __init__(self):
        self.word_Q = []


    def konlpy_api(self, str) :
        han = Hannanum()
        return han.nouns(str)

    def SyntacticAnalysis(self, str, method=None, name=None):
        return self.konlpy_api(str)


    def getCorpus(self, text):
        corpus_list =[]

        text_f = text.replace('.','\n')
        text_f = text.replace(',','\n')

        text_line = text_f.split('\n')

        for line in text_line:
            corpus_len = len(line)
            if 10 < corpus_len & corpus_len < 40 :
                corpus_list.append(line)

        return corpus_list

    def wiki_checker(self, word):
        wiki_ck = wk.Wikipedia( language='ko', extract_format=wk.ExtractFormat.WIKI)
        page_ = wiki_ck.page(word)
        if page_.exists():
            self.word_Q.append(word)
            print(word)
            return True
        return False
    
    def word_finder(self, word):
        for wq in self.word_Q:
            if wq == word : return True
        
        return False

    def word_filter(self, words):
        # 필요없는 단어 & 중복 단어 제거
        word_res = []
        for word in words:
            if any(c in word for c in '!@#$%^&*()0123456789'): 
                continue

            if self.word_finder(word) :continue

            word_res.append(word)

        return word_res


    def insert_Q(self, page):
        corpus_list = self.getCorpus(page.text)
        for corpus in corpus_list :
            words = self.SyntacticAnalysis(corpus, method="Hannanum", name="")
            words = self.word_filter(words)
            for word in words :
                t = threading.Thread(target=self.wiki_checker, args=(word,))
                t.start()


    def run(self):

        rear = 0
        # first input
        self.word_Q.append("부산")

        while(True) :

            q_len = len(self.word_Q)
            if q_len == rear : break
            if q_len > 1000 : break

            search_word = self.word_Q[rear]
            rear += 1

            wiki = wk.Wikipedia( language='ko', extract_format=wk.ExtractFormat.WIKI)
            _page = wiki.page(search_word)

            self.insert_Q(_page)


#WikiPaser   
        
paser = WikiPaser()
paser.run()



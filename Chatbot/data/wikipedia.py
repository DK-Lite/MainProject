# 위키피디아 크롤링

# 위피피디아 검색 → 검색 된 페이지에서 Corpus 추출 → 해당 Corpus에서 단어추출
# → 추출된 단어로 DB 삽입후 BFS 탐색 반복

import os

import pickle
import wikipediaapi as wk
import threading

from queue import Queue
from konlpy.tag import Hannanum
from dictionary import dictionary

class WikiParser:

    def __init__(self, path=None, max_num=None, interval=None):
        self.word_Q = Queue()
        self.max_num = max_num
        self.interval = interval
        # road dic
    def set_dict(self, dictionary):
        self.dictionary = dictionary

    def konlpy_api(self, str) :
        han = Hannanum()
        return han.nouns(str)

    def SyntacticAnalysis(self, str, method=None, name=None):
        return self.konlpy_api(str)

    ### Private method
    def _get_Corpus(self, text):
        corpus_list =[]

        text_f = text.replace('.','\n')
        text_f = text.replace(',','\n')

        text_line = text_f.split('\n')

        for line in text_line:
            corpus_len = len(line)
            if 10 < corpus_len & corpus_len < 40 :
                corpus_list.append(line)

        return corpus_list

    def _exist_in_Wiki(self, word):

        wiki_ck = wk.Wikipedia( language='ko', extract_format=wk.ExtractFormat.WIKI)
        page_ = wiki_ck.page(word)

        if page_.exists():
            return True

        return False

    def _insert_word_thread(self, word):
        if self._exist_in_Wiki(word):
            self.word_Q.put(word)
            self.dictionary.add(word)

            print(" find word in wiki : ", word )

    def _word_filter(self, words):
        word_res = []
        words = list(set(words))

        for word in words:
            if any(c in word for c in '-=+!@#$%^&*()0123456789'): continue
            if self.dictionary.search(word) : continue

            word_res.append(word)

        print("# [Success] Word filter")
        return word_res


    def _get_words_in(self, page):
        words = []
        corpus_list = self._get_Corpus(page.text)

        for corpus in corpus_list :
            words += self.SyntacticAnalysis(corpus, method="Hannanum", name="")

        print("# [Success] get word in page")
        return words

    def _insert_Q(self, page):

        words = self._get_words_in(page)
        words = self._word_filter(words)

        threads = []
        for word in words :
            t = threading.Thread(target=self._insert_word_thread, args=(word,))
            t.start()
            threads.append(t)
        
        for thread in threads:
            thread.join()
        print("# [Success] search words & End all thread")

    def set_init_word(self, word):
        self.word_Q.put(word)

    def run(self):

        if self.word_Q.empty():
            print("Empty Q")

        while(True) :

            if self.word_Q.qsize() % self.interval == 0 :
               self.dictionary.update()

            if self.word_Q.empty() : break
            if self.word_Q.qsize() > self.max_num : break

            search_word = self.word_Q.get()

            wiki = wk.Wikipedia( language='ko', extract_format=wk.ExtractFormat.WIKI)
            _page = wiki.page(search_word)
            
            print("# [Success] find word:",search_word)
            self._insert_Q(_page)



def __main__():

    folder_name = 'wordset'
    file_name = '{}.txt'.format('word5000')
    path = os.path.join(folder_name, file_name)

            
    #한글 사전 호출
    korea_words = dictionary()
    korea_words.load(path)
    #korea_words.print()

    #WikiPaser
    parser = WikiParser(max_num=5000, interval=1000)
    parser.set_dict(korea_words)
    parser.set_init_word("스파게티")
    parser.run()


__main__()

        # first input
        # self.word_Q.put("부산")
        # self.word_Q.put("밀면")
        # self.word_Q.put("국밥")
        # self.word_Q.put("음식")

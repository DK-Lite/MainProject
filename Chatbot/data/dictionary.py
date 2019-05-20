#  이곳은 모은 한국어 단어 데이터를 관리하는 클래스

import os
import codecs

class dictionary:

    def __init__(self, path=None):
        self.data = []
        self.path = path
        if not path is None:
            self.load(path)
    
    def load(self, path):
        self.path = path
        with codecs.open(path, 'r', encoding='utf8') as f:
            line = f.read()
            self.data = line.split('|')

    def self_duplicate(self):
        self.data = list(set(self.data))
        self._sort()

    def add(self, word):
        self.data.append(word)
    def size(self):
        return len(self.data)
    # def add(self, words):
    #     # remove duplicate word 
    #     words = list(set(words))
    #     for word in words:
    #         self.data.append(word)

    # 단어 사전 txt 파일 업데이트
    def update(self):
        self._sort()
        with codecs.open(self.path, 'w', encoding='utf8') as f:
            for word in self.data:
                f.write(word+'|')

    def print(self):
        for word in self.data:
            print(word)

    def search(self, word):
        return word in self.data

    def _sort(self):
        self.data.sort()
        
        



def __main__():
    folder_name = 'wordset'
    file_name = '{}.txt'.format('word')

    path = os.path.join(folder_name, file_name)


    korea_words = dictionary()
    korea_words.load(path)
    korea_words.self_duplicate()
    korea_words.print()

    korea_words.update()
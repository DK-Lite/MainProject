
# 사용자의 영화 추천
# 각 사용자별로 영화리스트를 윈도우를 이동시키면서 학습
# N : 영화 갯수
# V : 차원
# O : 영화 갯수
# W : N x V , W` : V x O


# EX) prefs['11']
from data_manager import *

prefs = load_movielens("data")

print (prefs['196'])

for movie in prefs['196'] :
    print ("movie : %s" % movie )
    print (prefs['196'][movie])


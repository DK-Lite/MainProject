from konlpy.tag import Hannanum

def konlpy_api(str) :
    han = Hannanum()
    return han.nouns(str)


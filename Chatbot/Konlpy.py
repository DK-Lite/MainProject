from konlpy.tag import Hannanum

def konlpy_api(str) :
    han = Hannanum()
    return han.nouns(str)



def SyntacticAnalysis(str, method=None, name=None):

    return konlpy_api(str)
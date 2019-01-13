from Konlpy import *




class NLU :
    

    
    def __init(self):
        self.corpus = ""
        
    def setCorpus(self, corpus):
        self.corpus = corpus

    def getEntity(self):
        return 0

    def predict(self):

        # 구문분석
        y = SyntacticAnalysis(self.corpus, method="Hannanum", name="")
        
        # Word2Vec


        # Intent


        # Entity

        # reply
    
         
        return y




#Test

test = NLU()
while(True) :
    corpus = input()
    if corpus == 'exit' :
        break

    test.setCorpus(corpus)
    print(test.predict())

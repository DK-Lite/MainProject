from Konlpy import *




class NLU :
    

    
    def __init(self):
        self.corpus = ""
        self.dictionary = []
        
    def setCorpus(self, corpus):
        self.corpus = corpus

    def getEntity(self):
        return 0

    def reply(self):

        # 구문분석
        y = SyntacticAnalysis(self.corpus, method="Hannanum", name="")
        
        # Word2Vec
        input_vec = Word2Vec(dictionary)

        intent = get_intent(input_vec)

        intent

        # Intent


        # Entity

        # reply
    

    NLP

    self.NLU.add(Skipgram())
    self.NLU.add(Entity())
    self.NLU.add(Intent()) 


        return y




#Test

test = NLU()
while(True) :
    corpus = input()
    if corpus == 'exit' :
        break

    test.setCorpus(corpus)
    print(test.predict())

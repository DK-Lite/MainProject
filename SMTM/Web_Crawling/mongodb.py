import pymongo
import sys

class DKDatabase:
    #def __init__(self):
       

    def connect(self, ip, port):
        self.connection = pymongo.MongoClient(ip, port)
        self.db = self.connection.NaverNews
        self.users = self.db.users


    def insert(self, doc):
        try:
            self.users.insert(doc)
        except:
            print("insert faild",sys.exc_info()[0])

    #def delete(self, str):
    
    #def update(self, str):

    def insert_str(self, str):
        doc = {
            'title' : str
        }
        self.insert(doc)

    def insert_list(self, list):
        self.insert(list)



import pickle

class dataManager:

    def __init__(self, folder_path):
        self.path = folder_path
        self.data = []
        

    def set_data(self, text):
        self.data = text

    def get_data(self):
        return self.data

    def read(self):
        with open(self.path, 'rb')as file:
            while True:
                try:
                    line = pickle.load(file)
                except EOFError:
                    break
                
                self.data.append(line)

    def write_all(self):
        with open(self.path, 'wb') as file:
            for line in self.data:
                pickle.dump(line, file)

    def write(self, text):
    
        with open(self.path, 'wb') as file:
            for line in text:
                pickle.dump(line, file)
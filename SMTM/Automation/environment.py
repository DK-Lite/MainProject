#agent가 투자할 종목의 차트 데이터를 관리


class Envinorment:
    
    PRICE_IDX = 4 
    
    def __init__(self, char_data=None):
        self.char_data = char_data
        self.observation =None
        self.idx = -1

    def reset(self):
        self. observation = None
        self.idx = -1

    def observe(self):
        if len(self.char_data) > self.idx + 1:
            self.idx += 1
            self.observation = self.char_data.iloc[self.idx]
            return self.observation

        return None
    
    def get_price(self):
        if self.observation is not None:
            return self.observation[self.PRICE_IDX]
        return None
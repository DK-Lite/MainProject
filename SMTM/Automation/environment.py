#agent가 투자할 종목의 차트 데이터를 관리


class Envinorment:
    
    PRICE_IDX = 4 
    
    def __init__(self, chart_data=None):
        self.chart_data = chart_data
        self.observation =None
        self.idx = -1

    def reset(self):
        self.observation = None
        self.idx = -1


    # 차트 상태를 반환
    def observe(self):
        if len(self.chart_data) > self.idx + 1:
            self.idx += 1
            self.observation = self.chart_data.iloc[self.idx]
            return self.observation

        return None
    
    # 현재 차트에서 가격을 반환
    def get_price(self):
        if self.observation is not None:
            return self.observation[self.PRICE_IDX]
        return None
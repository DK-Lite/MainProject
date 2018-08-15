#특정 시점의 주식 데이터가 제공 되었을때 매수할지 매도 할지 판단 하는 에이전트의 뇌같은 역할
# LSTM 신경망으로 구성되어짐
# - 매수, 매도, 관망 행위에 대해서 PV를 높일수 있을지의 확률을 계산
import numpy as np
from keras.models import Sequential
from keras.layers import Activation, LSTM, Dense, BatchNormalization
from keras.optimizers import sgd

class PolicyNetwork:
    
    def __init__(self, input_dim=0,ouput_dim=0, lr= 0.01):
        self.input_dim = input_dim
        self.lr = lr

        self.model = Sequential()
        self.model.add(LSTM(256, input_shape=(1, input_dim), return_sequences=True, stateful=False, dropout=0.5))
        self.model.add(BatchNormalization())
        self.model.add(LSTM(256, return_sequences=True, stateful=False, dropout=0.5))
        self.model.add(BatchNormalization())
        self.model.add(LSTM(256, return_sequences=True, stateful=False, dropout=0.5))
        self.model.add(BatchNormalization())
        self.model.add(Dense(ouput_dim))
        self.model.add(Activation('sigmoid'))

        self.model.compile(optimizer=sgd(lr=lr), loss='mse')
        self.prob = None

    def reset(self):
        self.prob = None

    def predict(self, sample):
        self.prob = self.model.predict(np.array(sample).reshape((1, -1, self.input_dim)))[0]
        return self.prob[0]

    def train_on_batch(self, x, y):
        return self.model.train_on_batch(x, y)

    def save_model(self,model_path):
        if model_path is not None and self.model is not None:
            self.model.save_weights(model_path, overwrite=True)
        
    def load_model(self, model_path):
        if model_path is not None:
            self.model.load_weights(model_path)

        

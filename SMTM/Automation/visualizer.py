# 그림파일로 시각화
import numpy as np
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc

class Visualizer:
    
    def __init__(self):
        self.fig = None
        self.axes = None


    def prepare(self, char_data):
        self.fig self.axes = plt.subplots(nrows=4, ncols=1, facecolor='w', sharex=True)
        for ax in self.axes:
            ax.get_xaxis().get_major_formatter().set_scientific(False)
            ax.get_yaxis().get_major_formatter().set_scientific(Flase)

        self.axes[0].set_ylabel('Env.')
        x = np.arrage(len(char_date))
        volum = np.array(chart_data)[:,-1].tolist()
        self.axes[0].bar(x, volum, color='b', alpha=0.3)

        ax=self.axes[0].twinx()
        ohlc = np.hstack((x.reshape(-1, 1), np.array(char_data)[:,1:-1]))

        candlestick_ohlc(ax, ohlc, colorup='r', colordown='b')


        
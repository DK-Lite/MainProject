import pandas as pd
import numpy as np

def load_chart_data(fpath):
    chart_data = pd.read_csv(fpath, thousands=',', header=None)
    chart_data.columns = ['date', 'open', 'high', 'low', 'close', 'volume']
    return chart_data

def preprocess(chart_data):
    prep_data = chart_data
    windows = [5, 10, 20, 60, 120]
    for window in windows:
        prep_data['close_ma{}'.format(window)] = prep_data['close'].rolling(window).mean()
        prep_data['volume_ma{}'.format(window)] = prep_data['volume'].rolling(window).mean()

    return prep_data

def build_training_data(prep_data):
    training_data = prep_data

    high_data        = training_data['high'].values
    low_data         = training_data['low'].values
    close_data       = training_data['close'].values

    cur_open_data    = training_data['open'][1:].values
    cur_volume_data  = training_data['volume'][1:].values
    cur_close_data   = training_data['close'][1:].values

    last_close_data  = training_data['close'][:-1].values
    last_volume_data = training_data['volume'][:-1].replace(to_replace=0, method='ffill').replace(to_replace=0, method='bfill').values

    training_data['high_close_ratio']   = (high_data - close_data) / close_data
    training_data['low_close_ratio']    = (low_data - close_data) / close_data

    training_data['open_lastclose_ratio']       = np.zeros(len(training_data))
    training_data['close_lastclose_ratio']      = np.zeros(len(training_data))
    training_data['volume_lastvolume_ratio']    = np.zeros(len(training_data))

    training_data['open_lastclose_ratio'].iloc[1:]      = (cur_open_data - last_close_data) / last_close_data
    training_data['close_lastclose_ratio'].iloc[1:]     = (cur_close_data - last_close_data) / last_close_data
    training_data['volume_lastvolume_ratio'].iloc[1:]   = ( cur_volume_data - last_volume_data ) / last_volume_data

    windows = [5, 10, 20, 60, 120]
    for window in windows:
        training_data['close_ma%d_ratio' % window]  = \
            (training_data['close'] - training_data['close_ma%d' % window]) / training_data['close_ma%d' % window]
        training_data['volume_ma%d_ratio' % window] = \
            (training_data['volume'] - training_data['volume_ma%d' % window]) / training_data['volume_ma%d' % window]

    return training_data
        

# chart_data = load_chart_data('chart_data/005930.csv')
# chart_data = preprocess(chart_data)
# chart_data = build_training_data(chart_data)

# print(chart_data)




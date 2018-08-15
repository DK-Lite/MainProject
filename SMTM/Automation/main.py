import logging
import os
import settings
import data_manager
from policy_learner import PolicyLearner

if __name__ == '__main__':

    stock_code = '005930'

    timestr         = settings.get_time_str()

    # log_dir         = os.path.join(settings.BASE_DIR, 'logs/%s' % stock_code)
    # log_file_path   = os.path.join(log_dir, "%s_%s.log" % (stock_code, settings.get_time_str()))

    # file_handler    = logging.FileHandler(filename=log_file_path, encoding='utf-8')
    # stream_handler  = logging.StreamHandler()

    # file_handler.setLevel(logging.DEBUG)
    # stream_handler.setLevel(logging.INFO)
    # logging.basicConfig(format="%(message)s", handlers = [file_handler, stream_handler], level=logging.DEBUG)


   
    chart_data_path = os.path.join(settings.BASE_DIR, "chart_data/{}.csv".format(stock_code))

    chart_data      = data_manager.load_chart_data(chart_data_path)
    prep_data       = data_manager.preprocess(chart_data)
    training_data   = data_manager.build_training_data(prep_data)



    # filtering date
    training_data   = training_data[  (training_data['date'] >= '2017-01-01') & (training_data['date'] <= '2017-12-31') ]
    training_data   = training_data.dropna()

    featuers_chart_data = ['date', 'open', 'high', 'low', 'close', 'volume']
    chart_data = training_data[featuers_chart_data]

    featuers_chart_data =[
        'open_lastclose_ratio', 'high_close_ratio', 'low_close_ratio',
        'close_lastclose_ratio', 'volume_lastvolume_ratio',
        'close_ma5_ratio', 'volume_ma5_ratio',
        'close_ma10_ratio', 'volume_ma10_ratio',
        'close_ma20_ratio', 'volume_ma20_ratio',
        'close_ma60_ratio', 'volume_ma60_ratio',
        'close_ma120_ratio', 'volume_ma120_ratio',
    ]

    training_data = training_data[featuers_chart_data]

    policy_learner = PolicyLearner(
        stock_code=stock_code, chart_data=chart_data, training_data=training_data,
        min_trading_unit=1, max_trading_unit=2, delayed_reward_threshold=.2, lr=.001)
    policy_learner.fit(balance=10000000, num_epoches=10, discount_factor=0, start_epsilon=0.5)

    model_dir = os.path.join(settings.BASE_DIR, 'models/%s' % stock_code)
    model_path = os.path.join(model_dir, 'model_%s.h5' % timestr)
    if not os.path.isdir(model_path):
        os.makedirs(model_path)

    policy_learner.policy_network.save_model(model_path)

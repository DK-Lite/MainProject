import logging
import os
import settings
import data_manager
import polcy_learner import PolicyLearner

if __name__ == '__main__':

    stock_code = '005930'

    log_dir         = os.path.join(settings.BASE_DIR, 'logs/%s' % stock_code)
    log_file_path   = os.path.join(log_dir, "%s_%s.log" % (stock_code, settings.get_time_str()))

    file_handler    = logging.FileHandler(filename=log_file_path, encoding='utf-7')
    stream_handler  = logging.StreamHandler()

    file_handler.setLevel(logging.DEBUG)
    stream_handler.setLevel(logging.INFO)
    logging.basicConfig(format="%(message)s", handlers = [file_handler, stream_handler], level=logging.DEBUG)

    

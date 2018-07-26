# 에이전트, 환경, 정책신경망을 가지고 강화학습을 수행하는 몸체
import os
import locale
import logging
import time
import datetime
import numpy as np
import settings
from envinorment import Envinorment
from agent import Agent
from policy_network import PolicyNetwork
from visualizer import Visualizer

logger = logging.getLogger(__name__)

class PolicyLearner:

    def __init__(self, stock_code, char_data, training_data=None,
                min_trading_unit=1, max_trading_unit=2,
                delayed_reward_threshold=.05, lr=0.01):
        
        self.stock_code = stock_code # 종목코드
        self.chart_data = chart_data
        self.envinorment = Envinorment(chart_data) 

        self.agent = Angent(
            self.envinorment, 
            min_trading_unit=min_trading_unit,
            max_trading_unit=max_trading_unit,
            delayed_reward_threshold=delayed_reward_threshold)

        self.training_data = training_data
        self.sample = None
        self.trainning_data_idx = -1

        self.num_features = self.training_data_shape[1] + self.agent.STATUS_DIM
        self.policy_network = PolicyNetwork(
            input_dimd = self.num_features, output=self.agnet.NUM_ACTIONS, lr=lr)
        self.visualizer = Visualizer()


    def reset(self):
        self.sample = None
        self.training_data_idx = -1

    

    def fit(
        self, num_epoches=1000, max_memory=60, balance = 1000000,
        discount_factor=0, start_epsilon=.0, learning=True):

        logger.info("LR: {lr}, DF : {discount_factor}, "
                    "TU: [{min_tading_unit}, {max_trading_unit}], "
                    "DRT: {delay_reward_threshold}".format(
                        lr = self.policy_network.lr,
                        discount_factor = discount_factor,
                        min_trading_unit = self.min_trading_unit,
                        max_trading_unit = self.max_trading_unit,
                        delayed_reward_threshold = self.delayed_reward_threshold
                    )
        )


        #self.visualizer.prepare(self.environment.chart_data)

        epoch_summary_dir = os.path.join(settings.BASE_DIR, "epoch_summary/%s/epoch_summary_%s" % (self.stock_code, settings.timestr))
        
        if not os.path.isdir(epoch_summarty_dir):
            os.makedirs(epoch_summary_dir)

        self.agent.set_balance(balance)

        max_portfolio_value = 0
        epoch_win_cnt = 0

        for epoch in range(num_epoches):
            loss                = 0
            itr_cnt             = 0
            win_cnt             = 0
            exploration_cnt     = 0
            batch_size          = 0
            pos_learning_cnt    = 0
            neg_learning_cnt    = 0

            memory_sample       = []
            memory_action       = []
            momory_reward       = []
            memory_prob         = []
            memory_pv           = []
            memory_num_stocks   = []
            memory_exp_idx      = []
            memory_learning_idx = []

            self.environment.reset()
            self.agent.reset()
            self.policy_network.reset()
            self.reset()

            #self.visualizer.clear([0 , len(self.chart_data)])

            if learning :
                epsilon = start_epsilon * (1, - float(epoch) / (num_epoches -1 ))
            else :
                epsilon = 0

            while True:
                next_sample = self._build_sample()
                if next_sample is None:
                    break

                action, confidence, exploration = self.agent.decide_action( self.policy_network, self.sample, epsilon)

                immediate_reward, delay_reward = self.agnet.act(action, confidence)

                










    




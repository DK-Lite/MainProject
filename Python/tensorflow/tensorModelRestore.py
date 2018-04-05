#restore , tensorboard
# Loss 가 너무 낮으면 오버피팅이 됨
# RBM, 볼츠만 머신



import tensorflow as tf
import numpy as np

input_data = [[1, 5, 3, 7, 8, 10, 12],
              [5, 8,10, 3, 0,  1,  3]]
lable_data = [[0, 0, 0, 1, 0],
              [1, 0, 0, 0, 0]]

INPUT_SIZE = 7
HIDDEN1_SIZE = 10
HIDDEN2_SIZE = 8
CLASSES = 5

Learning_Rate = 0.05

x = tf.placeholder( tf.float32, shape=[None, INPUT_SIZE] )
y_ = tf.placeholder ( tf.float32, shape=[None, CLASSES] )

tensor_map = { x: input_data, y_: lable_data }

W_h1 = tf.Variable( tf.truncated_normal(shape=[INPUT_SIZE, HIDDEN1_SIZE], dtype=tf.float32) )
b_h1 = tf.Variable( tf.zeros(shape=[HIDDEN1_SIZE]), dtype=tf.float32 )

W_h2 = tf.Variable( tf.truncated_normal(shape=[HIDDEN1_SIZE,HIDDEN2_SIZE], dtype=tf.float32) )
b_h2 = tf.Variable( tf.zeros(shape=[HIDDEN2_SIZE], dtype=tf.float32))

W_o = tf.Variable( tf.truncated_normal(shape=[HIDDEN2_SIZE,CLASSES], dtype=tf.float32) )
b_o = tf.Variable( tf.zeros(shape=[CLASSES], dtype=tf.float32))
# [model save]
# test model weight 가 끝나는 시점
# savor 를 생성해준다
param_list = [W_h1, b_h1, W_h2, b_h2, W_o, b_o]
saver = tf.train.Saver(param_list)

hidden1 = tf.sigmoid ( tf.matmul( x , W_h1) + b_h1 )
hidden2 = tf.sigmoid ( tf.matmul(hidden1, W_h2) + b_h2 )
y = tf.sigmoid ( tf.matmul(hidden2, W_o) + b_o )


sess = tf.Session()
#sess.run( tf.initialize_all_variables())
saver.restore(sess, './data/tensorflow_live.ckpt')
result = sess.run(y, tensor_map)

print(result)



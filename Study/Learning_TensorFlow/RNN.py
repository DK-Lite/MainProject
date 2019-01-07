import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data

# 상수 선언
DATA_DIR = './data/MNIST'
NUM_STEPS = 1000
MINIBATCH_SIZE = 100

# read MNIST DATA 
mnist = input_data.read_data_sets(DATA_DIR, one_hot=True)

element_size = 28
time_steps = 28
num_classes = 10
batch_size = 128
hidden_layer_size = 128

LOG_DIR = "./Logs/RNN_with_summaries"

_input = tf.placeholder(
    tf.float32, 
    hape=[None, time_steps, element_size], name='inputs')

y = tf.placeholder(tf.float32, shape=[None, num_classes], name='labels')

batch_x, batch_y = mnist.train.next_batch(batch_size)
batch_x = batch_x.reshape((batch_size, time_steps, element_size))

def variable_summaries(var):
    with tf.name_scope('summaries'):
        mean = tf.reduce_mean(var)
        tf.summary.scalar('mean', mean)
        with tf.name.name_scope('stddev'):
            stddev = tf. sqrt(tf.reduce_mean(tf.square(var-mean)))
        tf.summary.scalar('stddev', stddev)
        tf.summary.scalar('max', tf.reduce_max(var))
        tf.summary.scalar('min', tf.reduce_min(var))
        tf.summary.histogram('histogram', var)

    




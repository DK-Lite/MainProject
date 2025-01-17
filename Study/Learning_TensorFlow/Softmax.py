import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
# 상수 선언
DATA_DIR = './data/MNIST'
NUM_STEPS = 1000
MINIBATCH_SIZE = 100

# read MNIST DATA 
data = input_data.read_data_sets(DATA_DIR, one_hot=True)

# Placeholder 셋팅
x = tf.placeholder(tf.float32, [None, 784])
y_true = tf.placeholder(tf.float32, [None, 10])

# set weight
W = tf.Variable(tf.zeros([784, 10]))

# y = x * w
y_pred = tf.matmul(x,W)

# softmax and cross entropy
softmax = tf.nn.softmax_cross_entropy_with_logits(logits=y_pred, labels=y_true)
cross_entropy = tf.reduce_mean(softmax)

# Optimizer is gradient Descent
gd_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# calculate accuracy
correct_mask = tf.equal(tf.argmax(y_pred, 1), tf.argmax(y_true, 1))
accuracy = tf.reduce_mean(tf.cast(correct_mask, tf.float32))


# run TensorFlow
with tf.Session() as sess :

    sess.run(tf.global_variables_initializer())

    for _ in range(NUM_STEPS):
        batch_x, batch_y = data.train.next_batch(MINIBATCH_SIZE)
        sess.run(gd_step, feed_dict={x:batch_x, y_true:batch_y})

    res = sess.run(accuracy, feed_dict={x:data.test.images, y_true:data.test.labels})


# print result
print("Accuracy: {:.4}%".format(res*100))




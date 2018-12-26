import tensorflow as tf

# 상수 선언
DATA_DIR = './data/MNIST'
NUM_STEPS = 5000
MINIBATCH_SIZE = 50


# convolution NN 구성 함수
def weight_variable(shape) :
    init = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(init)

def bias_variable(shape) :
    init = tf.constant(0.1, shape=shape)
    return tf.Variable(init)

def conv2d(x, W):
    return tf.nn.conv2d(x, W , strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

def conv_layer(input, shape):
    W = weight_variable(shape)
    b = bias_variable([shape[3]])
    return tf.nn.relu(conv2D(input, W) + b)

def full_layer(input, size):
    in_size = int(input.get_shape()[1])
    W = weight_variable([in_size, size])
    b = bias_variable([size])
    return tf.matmul(input, W) + b


# placeholder 지정
x = tf.placeholder(tf.float32, shape=[None, 784])
y_true = tf.placeholder(tf.float32, shape=[None, 10])


# reshape [None, 784] -> [-1, 28, 28, 1]
x_image = tf.reshape(x, [-1, 28, 28, 1])

# Convolution Layer 
conv1 = conv_layer(x_image, shape=[5,5,1,32])
conv1_pool = max_pool_2x2(conv1)

conv2 = conv_layer(conv1_pool, shape=[5,5,32,64])
conv2_pool = max_pool_2x2(conv2)

conv2_flat = reshape(conv2_pool, [-1, 7*7*64])
full_1 = tf.nn.relu(full_layer(conv2_flat, 1024))

# dropout 계수
keep_prob = tf.placeholder(tf.float32)
full1_drop = tf.nn.dropout(full_1, keep_prob=keep_prob)

# fully Connected Layer 
y_conv = full_layer(full1_drop, 10)



##################################################################


# input data
data = input_data.read_data_sets(DATA_DIR, one_hot=True)

# 에러 측정 방식은 Softmax and Cross Entropy
softmax = tf.nn.softmax_cross_entropy_with_logits(logits=y_conv, labels=y_true)
cross_entropy = tf.reduce_mean(softmax)

# Optimizer는 Adam
train = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

# Accuracy 
correct_predict = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_true,1))
accuracy = tf.reduce_mean(tf.cast(correct_predict, tf.float32))


# run tensorFlow
with tf.Session() as sess :

    sess.run(tf.global_variables_initializer())
  
    # mini batch 
    for i in range(NUM_STEPS):
        batch_x, batch_y = data.train.next_batch(MINIBATCH_SIZE)

        if i % 100 = 0:
            train_accuracy = sess.run(accuracy, feed_dict={x:data.test.images, y_true:data.test.labels})

        sess.run(train, feed_dict={x:batch_x, y_true:batch_y})


    X = data.test.images.reshape(10, 1000, 784)
    Y = data.test.labels.reshape(10, 1000, 10)

    test_accurcy = np.mean([
        sess.run(
            accuracy, 
            feed_dict={x : x[i], y_true : Y[i], keep_prob:1.0})
            for i in range(10)
            ])



# print result
print("Accuracy: {:.4}%".format(test_accurcy))

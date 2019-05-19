import tensorflow as tf



# X input 5
# output 1

_X = [ [1, 2, 3, 4, 5],
        [2,3,,5,3,2],
        [2,3,2,3,2],
]
_Y = [1 ,2 , 3]
# 모델
X = tf.placeholder(tf.float32, shape=[None, 5])
Y = tf.placeholder(tf.float32, shape=[None, 1])

W = tf.Variable(tf.float32, shape=[5, 1])
B = tf.Variable( tf.zeros(shape=[None, 1], dtype=tf.float32))

Y = tf.mul(X,W) + B 

Y = tf.sigmoid( Y)
cost_func = -y_ * tf.log(y) - (1-y_)*tf.log(1-y)
cross_entropy = tf.reduce_mean(tf.reduce_sum(cost_func, reduction_indices=1))

train = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy) 
#cost = tf.reduce_mean(cost_matrix)
train = 


sess = tf.Session()
init = tf.initialize_all_variables()
sess.run(init)

for i in range(10):
    Y =sess.run(train, feed_dict=[_X,_Y] )









 
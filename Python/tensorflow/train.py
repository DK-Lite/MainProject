import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

num_points = 200

vectors_set = []

for i in range(num_points):

  x = np.random.normal(5,5)+15

  y =  x*1000+ (np.random.normal(0,3))*1000

  vectors_set.append([x,y])

  

x_data = [v[0] for v in vectors_set ]

y_data = [v[1] for v in vectors_set ]

W = tf.Variable(tf.random_uniform([1],-1.0,1.0))

b = tf.Variable(tf.zeros([1]))

y = W * x_data + b


loss = tf.reduce_mean(tf.square(y-y_data))

optimizer = tf.train.GradientDescentOptimizer(0.0015)

train = optimizer.minimize(loss)


init = tf.initialize_all_variables()

sess = tf.Session()

sess.run(init)


for step in range(10):

  sess.run(train)

  print(step,sess.run(W),sess.run(b))

  print(step,sess.run(loss))

  

  plt.plot(x_data,y_data,'ro')

  plt.plot(x_data,sess.run(W)*x_data + sess.run(b))

  plt.xlabel('x')

  plt.ylabel('y')

  plt.legend()

  plt.show()


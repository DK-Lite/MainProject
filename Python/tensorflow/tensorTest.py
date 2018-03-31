# Train data 테스트
# 80% Train, 20% 테스트


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

#cross entropy
cost_func = -y_ * tf.log(y) - (1-y_)*tf.log(1-y)
cross_entropy = tf.reduce_mean(tf.reduce_sum(cost_func, reduction_indices=1))
#cost = tf.reduce_mean(cost_matrix)
train = tf.train.GradientDescentOptimizer(Learning_Rate).minimize(cross_entropy) 

# 위까지는 그래프를 만드는 과정 



# argmax로 vector 내에서 큰 값의 위치를 찾고 
# 그것을 equal 시키면 comp_pred는 bool로 나온다
# 해당 comp_pred를 mean하면 정확도가 나온다(이때 tf.float32 타입 변환 필요 )
comp_pred = tf.equal( tf.argmax(y, 1), tf.argmax(y_,1) )
accuracy = tf.reduce_mean( tf.cast(comp_pred, tf.float32 ) ) 


sess = tf.Session()
init = tf.initialize_all_variables()
sess.run(init)

#loss = sess.run(cost_matrix, tensor_map)
#print (loss)

for i in range(1000):
    _, loss, acc = sess.run([train, cross_entropy, accuracy], feed_dict=tensor_map)
    #pred = sess.run(tf.argmax(y,1/), tensor_map)
    if i % 100 == 0 :
        #print(pred)
        print("--------------------------")
        print("Step : ", i)        
        print ("loss : ", loss )
        print ("accuracy : ", acc * 100 ,"%")
        saver.save(sess, './data/tensorflow_live.ckpt')


sess.close()



#tensor flow Model save 방법
# tensor flow 는 테스트 모델와 트레인 모델 두개가 생성된다.
# tensor flow에서는 check point 라는걸 만들어서 저장시키고
# train 모델의 weight 정보를 저장 하여 test model 의 check point 위치에 올린다
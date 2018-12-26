import tensorflow as tf 
# 그래프를 생성합니다.
a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
c = tf.matmul(a, b)
# log_device_placement을 True로 설정하여 세션을 만듭니다.
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
# op를 실행합니다.
print(sess.run(c))
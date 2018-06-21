import numpy as np
import tensorflow as tf
print ( "Package Load")
print (" tensorflow version : %s " % (tf.__version__))

sess = tf.Session()


def print_tf(x):
    print("type is %s" %(type(x)))
    print("value is %s" % (x))

hello = tf.constant("HELLO> IT`s ME. ")
print_tf(hello)
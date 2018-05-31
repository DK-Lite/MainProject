import numpy as np
import tensorflow as tf
import os
from scipy.misc import imread, imresize
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
print ("PACKAGES LOADED")

cwd = os.getcwd()
print("Current folder is %s" % (cwd))

mnist = input_data.read_data_sets("data/", one_hot=True)

def print_np(x):
    print('SHAPE OF is %s' % (x.shape,))
    print('VALUES LOOK LIKE \n %s' % (x))


def print_typeshape(img):
    print("type is %s" % (type(img)))
    print("shape is %s" % (img.shape,))


#cat = imread("./data/cat.jpg")
#print_typeshape(cat)
#plt.figure(figsize=(10, 8))
#plt.imshow(cat)
#plt.title("ORIGINAL CAT")
#plt.draw()

print_np(mnist.train.images)
print_np(mnist.train.labels)

































































# mnist 실습
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
#mnist.train.num_examples 
 

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

#print_np(mnist.train.images)
#print_np(mnist.train.labels)



ntrain = mnist.train.images.shape[0] #row 갯수
nsample = 3 
randidx = np.random.randint(ntrain, size = nsample)

for i in randidx :
    imgvec = mnist.train.images[i,:]
    labelvec = mnist.train.labels[i,:]
    img = np.reshape(imgvec, (28,28))
    label = np.argmax(labelvec)
    plt.matshow(img, cmap=plt.get_cmap('gray'))
    plt.title("[%d] DATA / LABEL IS [%d]" %(i,label))


ntrain = 10
randindices = np.random.permutation(ntrain)
print (randindices.shape)

ntrain = 10
nbatch = 4

niter = ntrain // nbatch + 1
for i in range(niter):
    currindices = randindices(i*nbatch:(i+1)*nbatch)
    print ("iTER : [ %d ] BATCH INDEX : %s " % (i, currindices))

    xbatch = mnist.train.images(currindices, :)
    ybatch = mnist.train.labels(currindices, :)

    print (" Shape of 'xbatch' is %s" % (xbatch.shape,))
    print (" Shape of 'ybatch' is %s" % (ybatch.shape,))
































































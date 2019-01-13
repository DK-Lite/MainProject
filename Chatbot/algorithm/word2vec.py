#의미 있는 내용 뽑아내기
#단어 문맥을 예측


# 단어 벡터 필요 → 단어 사전 필요


# 주어진 인풋을 매칭

# Word2Vec API

class Word2Vec:
    def __init__(self):
        return 0

# Word2Vec Train





# Wrod2Vec Test


# Skip-Gram

import os
import math
import numpy as np
import tensorflow as tf
from tensorflow.contrib.tensorboard.plugins import projector

digit_to_word_map = {
    1:"One", 2:'Two', 3:"Three", 
    4:"Four", 5:"Five", 6:"Six", 
    7:"Seven", 8:"Eight", 9:"Nine"}

sentences = []

for i in range(10000):
    rand_odd_ints = np.random.choice(range(1, 10, 2), 3)
    sentences.append(" ".join([digit_to_word_map[r] for r in rand_odd_ints]))
    rand_even_ints = np.random.choice(range(2, 10, 2),3)
    sentences.append(" ".join([digit_to_word_map[r] for r in rand_even_ints]))

#print(sentences[0:10])



word2index_map = {}

index= 0
for sent in sentences:
    for word in sent.lower().split():
        if word not in word2index_map:
            word2index_map[word] = index
            index += 1

index2word_map = { index : word for word, index in word2index_map.items()}

vocabulary_size = len(index2word_map)

skip_gram_pairs = []
for sent in sentences:
    tokenized_sent = sent.lower().split()
    for i in range(1, len(tokenized_sent)-1 ):
        word_context_pair = [[
            word2index_map[tokenized_sent[i-1]],
            word2index_map[tokenized_sent[i+1]]],
            word2index_map[tokenized_sent[i]]]

        skip_gram_pairs.append([word_context_pair[1],
                                word_context_pair[0][0]])
        skip_gram_pairs.append([word_context_pair[1],
                                word_context_pair[0][1]])

def get_skipgram_batch(batch_size):
    instance_indices = list(range(len(skip_gram_pairs)))
    np.random.shuffle(instance_indices)
    batch = instance_indices[:batch_size]
    x = [skip_gram_pairs[i][0] for i in batch]
    y = [[skip_gram_pairs[i][1] for i in batch]]
    return x, y




print( skip_gram_pairs[0:10])


with tf.name_scorpe("embeddings") :
    embeddings = tf.Variable(tf.random_uniform([vocabulary_size, embedding_dimension],
    -1.0, 1.0), name='embedding')

    embed = tf.nnembedding_lookup(embeddings, train_inputs)


nce_weights = tf.Variable(
    tf.truncated_normal([vocabulary_size, embedding_dimension],
    stddev=1.0 / math.sqrt(embedding_dimension)))

nce_biases = tf.Variable(tf.zeros([vocabulary_size]))

loss = tf.reduce_mean(
    tf.nn.nce_loss(weights = nce_weights, biases = nce_biases, inputs = embed,
    labels = train_labels, num_sampled = negative_samples, num_classes = vocabulary_size)

)


#!/usr/bin/env python

import csv
from sklearn.metrics import mean_squared_error
from math import sqrt
import sys

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

filename = sys.argv[1]

def get_tweet(f):
    with open(f, 'rb') as csvfile:
        datareader = csv.reader(csvfile, delimiter='\t')
        count = 0
        for row in datareader:
            yield row

def test_harness(test_tweets, test_scores, test_model, test_vectorizer):
    vectorized_test_tweets = test_vectorizer.transform(test_tweets).toarray()
    predicted_scores = test_model.predict(vectorized_test_tweets).tolist()
    rms = sqrt(mean_squared_error(test_scores, predicted_scores))
    return rms




yielded = 0
tweets = []
scores = []
test_tweets = []
test_scores = []

import random

for r in get_tweet(filename):
    if random.random() < .8:
        tweets.append(r[0])
        scores.append(int(r[1]))
    else:
        test_tweets.append(r[0])
        test_scores.append(int(r[1]))
        
import numpy as np
print np.mean(scores)
print len(test_tweets)
print len(tweets)

from sklearn import linear_model



for i in xrange(1,10):
    mf = i*1000
    bigram_vectorizer = CountVectorizer(ngram_range=(1,1), token_pattern=r'\b\w+\b', min_df=1, analyzer='word', max_features=mf, stop_words='english')
    analyzer = bigram_vectorizer.build_analyzer()
    x_2 = bigram_vectorizer.fit_transform(tweets).toarray()
    clf = linear_model.PassiveAggressiveRegressor()
    clf.fit(x_2, scores)
    rmse = test_harness(test_tweets, test_scores, clf, bigram_vectorizer)
    print "rmse at maxfeatures: {} is {}".format(mf, rmse)

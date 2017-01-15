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
l = []
scores = []


for r in get_tweet(filename):
    if len(r) >= 2:
            l.append(r[0])
            scores.append(int(r[1]))

import numpy as np
print np.mean(scores)
print len(scores)
cutoff = int(len(scores) * .7)
print cutoff

from sklearn import linear_model



for i in xrange(1,10):
    mf = i*1000
    bigram_vectorizer = TfidfVectorizer(ngram_range=(1,1), token_pattern=r'\b\w+\b', min_df=1, analyzer='word', max_features=mf, stop_words='english')
    analyzer = bigram_vectorizer.build_analyzer()
    train_set = l[:cutoff]
    x_2 = bigram_vectorizer.fit_transform(train_set).toarray()
    clf = linear_model.LogisticRegression()
    clf.fit(x_2, scores[:cutoff])
    print "rmse at maxfeatures = {}".format(mf)
    print test_harness(l[cutoff:], scores[cutoff:], clf, bigram_vectorizer)
    


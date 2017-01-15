#!/usr/bin/env python

import csv
from sklearn.metrics import mean_squared_error
from math import sqrt
import sys

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn import linear_model
from sklearn import neural_network
from sklearn import decomposition

filename = sys.argv[1]

def get_tweet(f):
    with open(f, 'rb') as csvfile:
        datareader = csv.reader(csvfile, delimiter='\t')
        count = 0
        for row in datareader:
            yield row

def test_harness(test_tweets, test_scores, test_model, test_vectorizer, dim_red):
    vectorized_test_tweets = test_vectorizer.transform(test_tweets).toarray()
    vtt = dim_red.transform(vectorized_test_tweets)
    predicted_scores = test_model.predict(vtt).tolist()
    rms = sqrt(mean_squared_error(test_scores, predicted_scores))
    return rms


# Parameters: lists of tweets and scores to train regression on and a single tweet to analyze. Returns a predicted score.
def analyze_one_tweet(tweets, scores, tweet):
    bigram_vectorizer = TfidfVectorizer(ngram_range=(1,3), token_pattern=r'\b\w+\b', min_df=1, analyzer='word', max_features=3000)
    analyzer = bigram_vectorizer.build_analyzer()
    x_2 = bigram_vectorizer.fit_transform(tweets).toarray()
    dim_red = decomposition.TruncatedSVD(n_components=100)
    x_prime = dim_red.fit_transform(x_2)
    #clf = neural_network.MLPRegressor(max_iter=800, solver='adam')
    clf = linear_model.LogisticRegression()
    clf.fit(x_prime, scores)
    return clf.predict(dim_red.fit_transform(bigram_vectorizer.transform(tweet)))[0]



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

for i in xrange(1,10):
    mf = i*1000
    bigram_vectorizer = TfidfVectorizer(ngram_range=(1,3), token_pattern=r'\b\w+\b', min_df=1, analyzer='word', max_features=mf)
    analyzer = bigram_vectorizer.build_analyzer()
    x_2 = bigram_vectorizer.fit_transform(tweets).toarray()
    dim_red = decomposition.TruncatedSVD(n_components=100)
    x_prime = dim_red.fit_transform(x_2)
    #clf = neural_network.MLPRegressor(max_iter=800, solver='adam')
    clf = linear_model.LogisticRegression()
    clf.fit(x_prime, scores)
    rmse = test_harness(test_tweets, test_scores, clf, bigram_vectorizer, dim_red)
    tweet = "Make America Great Again! Crooked Jeb!"
    print "rmse at maxfeatures: {} is {}".format(mf, rmse)

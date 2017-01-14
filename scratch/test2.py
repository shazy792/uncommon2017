#!/usr/bin/env python

import csv

from sklearn.feature_extraction.text import TfidfVectorizer

filename = '/home/geoffowens/training.1600000.processed.noemoticon.csv'

def get_tweet(f):
    with open(f, 'rb') as csvfile:
        datareader = csv.reader(csvfile)
        count = 0
        for row in datareader:
            yield row

yielded = 0
l = []


for r in get_tweet(filename):
    if yielded == 1:
        print r
    l.append(r[5])
    yielded += 1
    if yielded == 1000:
        break



vectorizer = TfidfVectorizer(min_df=1)

X = vectorizer.fit_transform(l)
print vectorizer.transform(['@bob what an incredible morning!']).toarray()

bigram_vectorizer = TfidfVectorizer(ngram_range=(1,2), token_pattern=r'\b\w+\b', min_df=1, stop_words='english', max_features=10)
analyzer = bigram_vectorizer.build_analyzer()

corpus = ['This is the first document.', 'This is the second second document.', 'And the third one.', 'Is this the first document?']

import random
corpus_scores = [random.randint(1, 10) for _ in xrange(1000)]


x_2 = bigram_vectorizer.fit_transform(l).toarray()
print x_2

test = bigram_vectorizer.transform(['@scott i\'m so upset we have Facebook on school tomorrow'])
test2 = bigram_vectorizer.transform(['This is a highly technical message which would be improbable to appear in a tweet'])

from sklearn import linear_model

clf = linear_model.LinearRegression()
clf.fit(x_2, corpus_scores)

print clf.coef_
print clf.predict(test)
print clf.predict(test2)

NUM_COLLECTING = 2000
#TODO: user will need to be inuput-based
uname = "realDonaldTrump"

import os

import csv

from flask import Flask, request
from flask_cors import CORS, cross_origin

import flask

import urllib2
import tweepy


#Our ML testing file
from test2 import analyze_one_tweet


consumer_key = "fB7SCLvFfHslwnzd4Ep3q85Wa"
secret_key = "KObsOCggBvNULofmJrZvgg0F8lzWKrbSDEgrDP0pHJiXeFsbgX"
access_token = "820464951475273728-yGkpylHOnap6GlFxMFoLCnfhbjwvrxr"
access_secret = "at0oNkQ0ytta2hWH1HrJjhq6oQHXlMDVhhkXXaSJRUrGJ"




def main():
    return "Hello, Twitter"
def calculate_retweets():
    return 0

def get_timeline(api, IDsince):
    timeline = api.user_timeline(screen_name=uname, max_id=IDsince, include_rts=True, count =200)
    return timeline


# EB looks for an 'application' callable by default.
application = Flask(__name__)
CORS(application)


@application.route('/')
def index():
    return "Hello World"

@application.route('/twit', methods=['GET'])
def twit():
    print request.headers['uname']
    return "request"

@application.route('/tweets', methods=['GET'])
def count_tweets():
    uname = request.headers['uname']
    twweet = request.headers['tweet']
    tweets = []
    scores = []
    outstring = ""
    i = 0

    auth = tweepy.OAuthHandler(consumer_key, secret_key)

    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    user = api.get_user(uname);

    #Max of querying 200 tweets at a time
    timeline = api.user_timeline(screen_name=uname, include_rts=True, count =200)

    lastID = 0
    #Collects tweets back as far as our ceiling
    while i < NUM_COLLECTING :
        if (len(timeline)<20):
            i += NUM_COLLECTING

        for tweet in timeline:
            i += 1
            tweets.append( {tweet.text : tweet.retweet_count} )
            scores.append(tweet.retweet_count)
            lastID = tweet.id
        timeline = get_timeline(api, lastID)




    #TODO this string will need to come from the request
    return str( analyze_one_tweet(tweets,scores,"This is a test") )


if __name__ == "__main__":
    application.debug = True
    application.run()

from flask import Flask, request, make_response
import webbrowser

import flask


import urllib2
import tweepy

#TODO: user will need to be inuput-based
uname = "realDonaldTrump"

consumer_key = "fB7SCLvFfHslwnzd4Ep3q85Wa"
secret_key = "KObsOCggBvNULofmJrZvgg0F8lzWKrbSDEgrDP0pHJiXeFsbgX"
access_token = "820464951475273728-yGkpylHOnap6GlFxMFoLCnfhbjwvrxr"
access_secret = "at0oNkQ0ytta2hWH1HrJjhq6oQHXlMDVhhkXXaSJRUrGJ"

#Tweet frequency object
class tweet_Freq():
    def __init__(self,text,retweets):
        self.text = text
        self.frequency = retweets

app = Flask(__name__)
@app.route('/tweets')
def get_tweets():
    tweets = []
    outstring = ""

    auth = tweepy.OAuthHandler(consumer_key, secret_key)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    user = api.get_user(uname);



    timeline = api.user_timeline(screen_name=uname, include_rts=True, count =4000)
    for tweet in timeline:
        print ("ID:", tweet.id)
        print ("User ID:", tweet.user.id)
        print ("Text:", tweet.text)
        print ("Created:", tweet.created_at)
        print ("Geo:", tweet.geo)
        print ("Contributors:", tweet.contributors)
        print ("Coordinates:", tweet.coordinates)
        print ("Favorited:", tweet.favorited)
        print ("In reply to screen name:", tweet.in_reply_to_screen_name)
        print ("In reply to status ID:", tweet.in_reply_to_status_id)
        print ("In reply to status ID str:", tweet.in_reply_to_status_id_str)
        print ("In reply to user ID:", tweet.in_reply_to_user_id)
        print ("In reply to user ID str:", tweet.in_reply_to_user_id_str)
        print ("Place:", tweet.place)
        print ("Retweeted:", tweet.retweeted)
        print ("Retweet count:", tweet.retweet_count)
        print ("Source:", tweet.source)
        print ("Truncated:", tweet.truncated)
        elem = tweet_Freq(tweet.text, tweet.retweet_count)
        tweets.append(elem)

    tsv = ""

    for tweet in tweets:
        print tweet.text + ' : ' + str(tweet.frequency)
        tsv += tweet.text + "\t"+str(tweet.frequency)+"\n"
        outstring += tweet.text + ',' + str(tweet.frequency) + '</br>'


    return outstring
def handle_verifier(auth):
    #TODO auth cannot depend on raw_input
    verifier = raw_input('Verifier: ')


    print verifier

    try:
        auth.get_access_token(verifier)
        access_token = auth.access_token
        access_secret = auth.access_token_secret
        print access_token
        print access_secret
    except tweepy.TweepError:
        print 'Error! Failed to get access token.'

    return "Hello, Verifier"


@app.route('/')
def index():
    auth = tweepy.OAuthHandler(consumer_key, secret_key)

    print auth

    try:
        redirect_url = auth.get_authorization_url()
        #webbrowser.open_new_tab(redirect_url)
        #return handle_verifier(auth)
    except tweepy.TweepError:
        print "Error! Failed to get request token."



    return "Hello, World"




if __name__ == '__main__':
    app.run(debug=True)

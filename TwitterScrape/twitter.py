import urllib2
import tweepy

consumer_key = "KrRt2ZVFSUG8xEiNLVucLhd0E"
secret_key = "sqX8deTdvVJw8WjcwksmjRq7VrAhh69YW1NRhsbnoNaT2EV9Nw"

domain = "localhost:5000"

def main():
    print "Hello, Twitter"
    auth = tweepy.OAuthHandler(consumer_key, secret_key)

    try:
        redirect_url = auth.get_authorization_url()
        print redirect_url
    except tweepy.TweepError:
        print "Error! Failed to get request token."





    '''

    try:
        auth.get_access_token(verifier)
    except tweepy.TweepError:
        print "ERROR Failed to get access token"
    '''

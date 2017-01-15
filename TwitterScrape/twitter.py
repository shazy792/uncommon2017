NUM_COLLECTING = 2000
uname = "coffee_dad"


import urllib2
import tweepy
'''
consumer_key = "KrRt2ZVFSUG8xEiNLVucLhd0E"
secret_key = "sqX8deTdvVJw8WjcwksmjRq7VrAhh69YW1NRhsbnoNaT2EV9Nw"
access_token = "718548015779311616-r3AcIskbnvQvKnZX4rOKYrCp9TtgR9e"
access_secret = "QPZkRr49Ogpovwe3t4rJAc9GFkzmLKTqVCIcWXeFtypGL"
'''
consumer_key = "fB7SCLvFfHslwnzd4Ep3q85Wa"
secret_key = "KObsOCggBvNULofmJrZvgg0F8lzWKrbSDEgrDP0pHJiXeFsbgX"
access_token = "820464951475273728-yGkpylHOnap6GlFxMFoLCnfhbjwvrxr"
access_secret = "at0oNkQ0ytta2hWH1HrJjhq6oQHXlMDVhhkXXaSJRUrGJ"
#Clean a string
def clean(instring):
    outstring = ""
    for char in instring:
        if ( (char!="\n") & (char!="\t") & (char!=",") ):
            outstring+=char
        else:
            outstring += " "

    return outstring


class tweet_Freq():
    def __init__(self,text,retweets):
        self.text = clean(text)
        self.frequency = retweets


def get_timeline(api, IDsince):
    timeline = api.user_timeline(screen_name=uname, max_id=IDsince, include_rts=True, count =200)
    return timeline

def main():
        tweets = []
        outstring = ""
        i = 0

        auth = tweepy.OAuthHandler(consumer_key, secret_key)
        ###
        #Comment out when not harvesting new keys
        '''
        try:
            redirect_url = auth.get_authorization_url()
            print "Go to " + redirect_url
        except tweepy.TweepError:
            print 'Error! Failed to get request token.'

        verifier = raw_input("Verifier: ")

        try:
            auth.get_access_token(verifier)
        except tweepy.TweepError:
            print 'Error! Failed to get access token.'

        access_token = auth.access_token
        access_secret = auth.access_token_secret
        print access_token
        print access_secret
        '''
        ###
        auth.set_access_token(access_token, access_secret)
        api = tweepy.API(auth)

        user = api.get_user(uname);

        #Max of querying 200 tweets at a time
        timeline = api.user_timeline(screen_name=uname, include_rts=True, count =200)
        '''
        #Would enable query of current dataset
        while(1):
            index = int(raw_input("Inspect: "))
            tweet = timeline[index]
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
        '''
        lastID = 0
        #Collects tweets back as far as our ceiling
        while i < NUM_COLLECTING :
            if (len(timeline)<20):
                i += NUM_COLLECTING

            for tweet in timeline:
                i += 1
                elem = tweet_Freq(tweet.text, tweet.retweet_count)
                tweets.append(elem)
                lastID = tweet.id
            timeline = get_timeline(api, lastID)

        file = open('./data/'+uname+'_data.tsv','w')

        for tweet in tweets:
            i += 1
            try:
                file.write( tweet.text + "\t"+str(tweet.frequency)+"\n")
            except:
                print "ERROR in writing"

        file.close()


main()

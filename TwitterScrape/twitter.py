import urllib2
import tweepy

uname = "realDonaldTrump"

consumer_key = "KrRt2ZVFSUG8xEiNLVucLhd0E"
secret_key = "sqX8deTdvVJw8WjcwksmjRq7VrAhh69YW1NRhsbnoNaT2EV9Nw"
access_token = "718548015779311616-r3AcIskbnvQvKnZX4rOKYrCp9TtgR9e"
access_secret = "QPZkRr49Ogpovwe3t4rJAc9GFkzmLKTqVCIcWXeFtypGL"

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
    timeline = api.user_timeline(screen_name=uname, since_id=IDsince, include_rts=True, count =200)
    return timeline

def main():
        tweets = []
        outstring = ""
        i = 0

        auth = tweepy.OAuthHandler(consumer_key, secret_key)
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
        while i < 1000 :

            for tweet in timeline:
                i += 1
                elem = tweet_Freq(tweet.text, tweet.retweet_count)
                tweets.append(elem)
                lastID = tweet.id
            timeline = get_timeline(api, lastID)

        file = open('data.tsv','w')

        for tweet in tweets:
            i += 1
            try:
                file.write( tweet.text + "\t"+str(tweet.frequency)+"\n")
            except:
                print "ERROR in writing"

        file.close()


main()

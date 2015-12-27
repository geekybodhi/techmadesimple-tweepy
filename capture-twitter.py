from tweepy import StreamListener
from tweepy import Stream
import tweepy, sys
import os,io

## insert your keys and token here
consumer_key = "ENTER YOUR API KEY"
consumer_secret = "ENTER YOUR API SECRET"
access_token = "ENTER YOUR ACCESS TOKEN"
access_secret = "ENTER YOUR ACCESS TOKEN SECRET"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

class StdOutListener(StreamListener):

    def __init__(self):
        self.tweet_data=[]

    def on_data(self, data):
        # process stream data here
        print(data)
        
        ##Display only particular elements instead of the entire JSON stream
        #tweet=data.split(',"text":"')[1].split('","source')[0] 
        #print (tweet)
        
        ##Save tweets to a file
        #self.tweet_data.append(data)
        #saveFile = io.open('privacyTweets.json', 'w', encoding='utf-8')
        #saveFile.write(u'[\n')
        #saveFile.write(','.join(self.tweet_data))
        #saveFile.write(u'\n]')
        #saveFile.close()

        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    listener = StdOutListener()
    twitterStream = Stream(auth, listener)
    #twitterStream.filter(follow=['5637652'])  ##Display tweets from a particular account
    twitterStream.filter(track=["privacy"])

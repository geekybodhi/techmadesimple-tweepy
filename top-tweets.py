import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys
import json
import operator

## insert your keys and token here
consumer_key = "ENTER YOUR API KEY"
consumer_secret = "ENTER YOUR API SECRET"
access_token = "ENTER YOUR ACCESS TOKEN"
access_secret = "ENTER YOUR ACCESS TOKEN SECRET"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

def main(tweetsFile):
  tweets_file = open(tweetsFile)                        
  tweets_hash = {}                                     
  for tweet_line in tweets_file:                       
    if tweet_line.strip():
      tweet = json.loads(tweet_line)                    
      if "entities" in tweet.keys():                    
        hashtags = tweet["entities"]["hashtags"]
        for ht in hashtags:                             
          if ht != None:
            if ht["text"].encode("utf-8") in tweets_hash.keys():  
              tweets_hash[ht["text"].encode("utf-8")] += 1        
            else:
              tweets_hash[ht["text"].encode("utf-8")] = 1

  sortedHashTags = dict(sorted(tweets_hash.items(), key=operator.itemgetter(1), reverse=True)[:10])

  print("\nHashtag   -   Occurrence\n")

  for count,value in sorted(sortedHashTags.items(), key=lambda kv: (kv[1],kv[0]),reverse=True):
    print("#%s -  %d times" % (count.decode("utf-8"), value)) 


if __name__ == '__main__':
  if len(sys.argv) == 2:
    main(sys.argv[1])
  else:
    print('Usage: python top_tweets.py [file-with-tweets.json]')

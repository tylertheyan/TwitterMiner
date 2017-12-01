#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search
#  - performs a basic keyword search for tweets containing the keywords
#    "lazy" and "dog"
#-----------------------------------------------------------------------

from twitter import *

#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------
config = {}
execfile("config.py", config)

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(
                auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))


# get tweets based on names

with open("positives_names") as f:
    content = f.readlines()
content = [x.strip() for x in content] 

# get statuses
t1 = open('timeline_1', 'w')
for name in content:
    query = twitter.statuses.user_timeline(screen_name=name, count=1000)
    for result in query:
        t1.write(result['text'].encode('utf-8'))
    t1.write("**END**")

# TODO: FEATURE EXTRACTION

# ngrams
# total_tweets
# tweet_length
# tweet_rate
# tweet_time
# num_followers
# % @mentions
# % RTs
# % Replies
# Sentiment score



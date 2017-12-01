#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search
#  - performs a basic keyword search for tweets containing the keywords
#    "lazy" and "dog"
#-----------------------------------------------------------------------

from twitter import *
import feature_helper

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

# EXTRACT FEATURES FROM USERS AND TIMELINES

# get list of names
with open("positives_names") as f:
    content = f.readlines()
content = [x.strip() for x in content] 

# get statuses based on names
t1 = open('timeline_1', 'w')
for name in content:
    query = twitter.statuses.user_timeline(screen_name=name, count=1000)
    for result in query:
        t1.write(result['text'].encode('utf-8'))
    t1.write("**END**")

    # TODO: get this info and put into CSV, with each tweet corresponding to a user

    # total_tweets
    # num_followers
    # tweet_time
    # is @mention?
    # is RT?
    # is Reply?
    # tweet_length (probs need to calc later)
    # tweet_rate (probs need to calc later)



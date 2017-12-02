#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search
#  - performs a basic keyword search for tweets containing the keywords
#    "lazy" and "dog"
#-----------------------------------------------------------------------

from twitter import *
import json
import pickle
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

print len(content)
# creates a user dictionary with the key being the username, and value will be a list of tweets
tweet_dict = {}

# get statuses based on names
count = 0
for name in content:
    count += 1
    print count
    # gets at most 1000 tweets from each user timeline
    try:
        query = twitter.statuses.user_timeline(screen_name=name, count=1000)
    except:
        continue
    # print query
    tweet_list = []
    # for every tweet in the query
    for result in query:
        tweet_time = result['created_at']
        
        tweet_text = result['text']
        
        # if the tweet is replying to another, tweet_is_reply = 1, else 0
        if result['in_reply_to_status_id']:
            tweet_is_reply = 1
        else:
            tweet_is_reply = 0
        
        tweet_geo_coordinates = result['coordinates']
        
        tweet_is_retweet = int(result['retweeted'] == True)
        tweet_favorites = result['favorite_count']
        tweet_num_hashtags = len(result['entities']['hashtags'])
        tweet_mentions = len(result['entities']['user_mentions'])
        # print tweet_num_hashtags
        # creates a dictionary of attributes
        tweet_attributes = {}
        tweet_attributes['time'] = tweet_time
        tweet_attributes['text'] = tweet_text
        tweet_attributes['is_reply'] = tweet_is_reply
        tweet_attributes['coordinates'] = tweet_geo_coordinates
        tweet_attributes['is_rt'] = tweet_is_retweet
        tweet_attributes['favorites'] = tweet_favorites
        tweet_attributes['hashtags'] = tweet_num_hashtags
        tweet_attributes['mentions'] = tweet_mentions

        tweet_list += [tweet_attributes]

        # t1.write(result['text'].encode('utf-8'))

    tweet_dict[name] = tweet_list
    # print tweet_dict

# generate pickle vals of dictionary
output = open('positives.pkl', 'wb')
pickle.dump(tweet_list, output)

# generate JSON
with open('result.json', 'w') as fp:
    json.dump(tweet_dict, fp)
    # t1.write("**END**")

    # TODO: get this info and put into CSV, with each tweet corresponding to a user

    # total_tweets
    # num_followers
    # tweet_time
    # is @mention?
    # is RT?
    # is Reply?
    # tweet_length (probs need to calc later)
    # tweet_rate (probs need to calc later)



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

# Get usernames of positives

depression_phrases = [
    "I have depression",
    "I use antidepressants",
    "I was diagnosed with depression"
    ]

names = open('positives_names', 'w')
count = 0
for phrase in depression_phrases:
    
    #-----------------------------------------------------------------------
    # perform a basic search 
    # Twitter API docs:
    # https://dev.twitter.com/rest/reference/get/search/tweets
    #-----------------------------------------------------------------------
    query = twitter.search.tweets(q=phrase, result_type='recent', lang='en', count=100)

    #-----------------------------------------------------------------------
    # How long did this query take?
    #-----------------------------------------------------------------------
    print "Search complete (%.3f seconds)" % (query["search_metadata"]["completed_in"])

    #-----------------------------------------------------------------------
    # Loop through each of the results, and print its content.
    #-----------------------------------------------------------------------

    f = open('positives' + str(count), 'w')
    for result in query["statuses"]:
        f.write("(%s) @%s %s \n" % (result["created_at"].encode('utf-8'), result["user"]["screen_name"].encode('utf-8'), result["text"].encode('utf-8')))
        names.write("%s \n" % (result["user"]["screen_name"].encode('utf-8')))
    count += 1

# Get usernames for negatives - how to do this??


import feature_helper
import numpy
import pickle

# FEATURE EXTRACTION INTO MATRIX MODEL TEST SET

# TODO: import data from csv
tweets = []
users = []
pkl_file = open('positives.pkl', 'rb')
positive_tweets = pickle.load(pkl_file)
pkl_file.close()
print positive_tweets

# TO DO: create probability lists for each feature -> convert to number

for user in users:
    # TOD0: total_tweets (given in data)
    # TODO: num_followers (given in data)

    length_sum = 0.
    mentions_sum  = 0.
    RTs_sum = 0.

    for tweet in tweets:
        # TODO: ngrams
        ngrams = ngram(tweet)

        # Sentiment score
        sentiment = get_tweet_sentiment(tweet)

        length_sum += len(tweet)
    
    # tweet_length (average)
    tweet_length = length_sum / len(tweets)

    # tweet_rate: average tweets per day
    # % of tweets between midnight and 4am in timezone
    # % @mentions
    # % RTs
    # % Replies

# TODO: print this out into a file, for a fully formatted model, we can use to make predictions.


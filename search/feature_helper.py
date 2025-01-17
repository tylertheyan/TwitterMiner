import string
import re
from textblob import TextBlob
# do pip install textblob
# python -m textblob.download_corpora

t = "i fucking love pumpernickel"

# http://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/
def clean_tweet(tweet):
    '''
    Utility function to clean tweet text by removing links, special characters
    using simple regex statements.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

# Removes punctuation and converts to lowercase.
def format(text):
    # https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
    text = text.translate(None, string.punctuation).lower()
    return text

# bag of words
def words(text):
    text = format(text)
    return text.split(" ")

print(words(t))

# ngram
# https://stackoverflow.com/questions/14617601/implementing-ngrams-in-python
def ngram(text,grams):  
    text = format(text)
    words = text.split(" ")
    model = []  
    count = 0  
    for token in words[:len(words) - grams + 1]:  
       model.append(" ".join(words[count:count + grams]))  
       count = count + 1  
    return model

print(ngram(t, 5))

# SENTIMENT ANALYSIS

def get_tweet_sentiment(tweet):
    analysis = TextBlob(clean_tweet(tweet))
    return  analysis.sentiment.polarity

print(get_tweet_sentiment(t))

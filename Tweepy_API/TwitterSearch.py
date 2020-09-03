import tweepy
import OAuth
import pandas as pd
import numpy as np


# Search module to collect tweets of query hashtags
class TwitterSearch():

    def __init__(self, query):
        self.auth = OAuth.TwitterAuthenticator().authenticateTwitter()
        self.twitter_api = tweepy.API(self.auth)
        self.query = query

    def getTweets(self, num_tweets):
        tweets = []
        for tweet in tweepy.Cursor(self.twitter_api.search, q=self.query, lang="en").items(num_tweets):
            tweets.append(tweet)

        return tweets


tweets = TwitterSearch("#nvidia +gaming -amd").getTweets(10)
for i, tweet in enumerate(tweets):
    print(i, tweet.text)

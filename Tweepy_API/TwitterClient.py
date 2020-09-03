import tweepy
import OAuth
import pandas as pd
import numpy as np


# Client module to collect user data
class TwitterClient():

    def __init__(self, twitter_user=None):
        self.auth = OAuth.TwitterAuthenticator().authenticateTwitter()
        self.twitter_client = tweepy.API(self.auth)
        self.twitter_user = twitter_user

    def getTweets(self, num_tweets):
        tweets = []
        for tweet in tweepy.Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

    # def get_frds(self, num_frds):
    #     frds = []
    #     for tweet in Cursor(self.twitter_client.friends, id=self.twitter_user).items(num_frds):
    #         frds.append(tweet)
    #     return frds


tweets = TwitterClient("therock").getTweets(30)
print(len(tweets))

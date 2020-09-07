import Tweepy_API.OAuth as OAuth
import tweepy
import pandas as pd
import numpy as np


# Client module to collect user data
class TwitterClient():

    def __init__(self, twitter_user=None):
        self.auth = OAuth.TwitterAuthenticator().authenticateTwitter()
        self.twitter_client = tweepy.API(self.auth)
        self.twitter_user = twitter_user
        self.client_tweets = []

    def getTweets(self, num_tweets):
        for tweet in tweepy.Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            self.client_tweets.append(tweet)

        return self

    def getTweetDataFrame(self):
        df = pd.DataFrame(
            data=[tweet.id for tweet in self.client_tweets], columns=["Id"])
        df["Date"] = np.array(
            [tweet.created_at for tweet in self.client_tweets])
        df["Tweet"] = np.array([tweet.text for tweet in self.client_tweets])
        df["Likes"] = np.array(
            [tweet.favorite_count for tweet in self.client_tweets])
        df["Retweets"] = np.array(
            [tweet.retweet_count for tweet in self.client_tweets])
        df["Geo"] = np.array(
            [tweet.coordinates for tweet in self.client_tweets])

        return df

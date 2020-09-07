import Tweepy_API.config as config
import tweepy


# Authentication module
class TwitterAuthenticator():
    def authenticateTwitter(self):
        auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET_KEY)
        auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
        return auth

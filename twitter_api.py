import tweepy as tw
import json

with open("apiTwitterConfig.json","r")  as config_file :
    config_file = json.load(config_file)

consumer_key= config_file['key']
consumer_secret= config_file['secret']
access_token= config_file['access_token']
access_token_secret= config_file['secret_access_token']

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)


def get_tweet() :
    search_words = "a"
    tweets = tw.Cursor(api.search,
                q=search_words,
                tweet_mode='extended',
                result_type='popular',
                lang="en").items(1)

    for tweet in tweets :
        return tweet

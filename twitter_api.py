import tweepy as tw

consumer_key= ''
consumer_secret= ''
access_token= ''
access_token_secret= ''

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

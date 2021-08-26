import tweepy as tw

consumer_key= 'U2rLmrQqRWZxWk1tIUmVGTzVQ'
consumer_secret= '6oJK35VUYddavMKjywwISknny36DqtDLx7Z01iykNpI6ZjYf7c'
access_token= '1180935927885156353-BfsGe1UdA1hDuNWmSVCdZMjmRaGixt'
access_token_secret= 'mpr7ZNz691X0x9P3sp4sdkjPJXneHzvanTYV1UpCQDLWB'

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
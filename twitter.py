import tweepy
from config import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def search_tweets(query, count=100):
    return tweepy.Cursor(api.search, query, count=100).items(1000)
    # return api.search(q=query, count=100, tweet_mode="extended")

if __name__ == '__main__':
    tweets = search_tweets('covid')
    print(type(tweets))
    # for tweet in tweets:
    #     print(tweet.text)
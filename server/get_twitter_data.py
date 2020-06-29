import os
import tweepy as tw
import pandas as pd
from unicodedata import normalize

def get_tweets(amount, date = "2020-06-15"):
    consumer_key = 'RQRtTNJZ1LgQE79vyHzKq4nSX'
    consumer_secret = '8cuiS5UYFEGLkVb1QpBGlitrSVU7pffJvTQ6FA3xm5J6BV9XwB'
    access_token = '926460072-k7vVuOHnirDYGYAVoUbrf7AxdVZxavU9S89YblUC'
    access_token_secret = 'wrohLbqI79iC6HXDgAL401pNPfkph8jlQQvhqpaG281nq'

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)

    # Define the search term and the date_since date as variables
    search_words = "@Minsa_Peru" + " -filter:retweets"
    # start of quarentine in Peru
    date_since = date

    # Collect tweets
    tweets = tw.Cursor(api.search,
                    q=search_words,
                    lang="es",
                    tweet_mode='extended',
                    since=date_since).items(amount)

    # replace special chracters
    trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
    users_tweets = [[
        str(tweet._json['id']),
        normalize(
            'NFKC',
            normalize('NFKD',
                    tweet._json['full_text'].rstrip()).translate(trans_tab))
    ] for tweet in tweets]
    tweets_frame = pd.DataFrame(data=users_tweets, columns=['user', 'text'])
    tweets_frame.to_csv(
        'data.csv',
        index=False,
    )

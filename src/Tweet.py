import tweepy
import os
from dotenv import load_dotenv
import db

load_dotenv()

# importing environment variables
bearer_token = os.getenv('BEARER_TOKEN')
consumer_key = os.getenv('API_KEY')
consumer_secret = os.getenv('API_KEY_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

# V1 API authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# V2 API authentication
client = tweepy.Client(
    bearer_token,
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

def tweet():
    while True:
        try:
            randomQuote = db.getRandomQuote()
            quote = randomQuote['quote']
            author = randomQuote['author']
            client.create_tweet(text=f"{quote}\n-{author}")
            break
        except:
            print('error tweeting')

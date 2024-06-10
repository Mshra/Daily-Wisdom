from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv('DB_URI'))
db = client['daily-wisdom']
collection = db['philosophy-quotes']

def getRandomQuote() -> dict:
    randomQuote = list(collection.aggregate([{"$sample": {"size": 1}}]))[0]
    quote = {
        "author": randomQuote['author'],
        "quote": randomQuote['quote']
    }
    return quote

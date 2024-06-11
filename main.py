import sys
from flask import Flask
sys.path.append('src')
from Tweet import tweet

app = Flask(__name__)

@app.route('/')
def index():
    return f"hello"

@app.route('/tweet')
def post():
    tweet()
    return 'tweeted'

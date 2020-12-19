from flask import Flask, render_template, request
import requests
import twitter
import tweepy
from secrets import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET

app = Flask(__name__)

def OAuth():
    try:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
        return auth 
    except Exception as e:
        return None

def post_tweet(tweet):
    oauth = OAuth()
    api = tweepy.API(oauth)

    api.update_status(tweet)

@app.route('/')
def show_address_form():
    return render_template("post_tweet.html")

@app.route('/post_tweet')
def show_tweet():
    tweet = request.args["post_tweet"]
    post_tweet(tweet)
    return render_template("post_tweet.html", tweet=tweet)

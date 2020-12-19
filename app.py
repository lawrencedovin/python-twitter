from flask import Flask, render_template, request
import requests
import twitter
from secrets import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET

# location = '11911 Rocking Horse Rd, Rockville, MD'
# API_BASE_URL = 'http://www.mapquestapi.com/geocoding/v1/address'

# app = Flask(__name__)

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN_KEY,
                  access_token_secret=ACCESS_TOKEN_SECRET)

# def get_coords(address):
#     response = requests.get(API_BASE_URL, 
#                             params={"key": API_SECRET_KEY, "location": address})
    
#     data = response.json()
#     results = data["results"]
#     latitude = data["results"][0]["locations"][0]["latLng"]["lat"]
#     longitude = data["results"][0]["locations"][0]["latLng"]["lng"]
#     coords = {"latitude": latitude, "longitude": longitude}
#     return coords

# @app.route('/')
# def show_address_form():
#     return render_template("address_form.html")

# @app.route('/geocode')
# def show_coordinates():
#     address = request.args["address"]
#     coords = get_coords(address)
#     return render_template("address_form.html", coords=coords)

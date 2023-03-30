# get current weather and also get full information at any location

# Get API key

# step 1. visit (https://www.weatherapi.com/) this site then sign up and log in
# step 2. get the API key from this site
# step 3. visit (https://api.weatherapi.com/v1/current.json?key=f31e559b51a74413a3b152727233003&q=kolkata)
# this website and paste your own API key here [key = "paste your own API key"]
# step 4. copy step 3 wesbite link with your own API key

import requests # this library helps to collect all the inforantion at any location
import json # this library helps to convert it into dictionary

city = input("Enter your city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=f31e559b51a74413a3b152727233003&q={city}" # follow step 4 and paste the link

r = requests.get(url) # get info from url

# print full information
print(r.text) # r.text type is String

# print only temperature

wDic = json.loads(r.text) # convert into dictionary

print(f"weather of {city}: ")
print(wDic["current"]["temp_c"]) # get key and print the value

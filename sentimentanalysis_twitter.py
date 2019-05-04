#sentiment analysis using twitter api and textblob

import tweepy
from textblob import TextBlob

consumer_key='Your key'
consumer_secret='Your secret token'

access_key='Your access key '
access_secret='Your access secret token '

#creating authentication variable
#to login into twitter via code 
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_key,access_secret)

api=tweepy.API(auth)

twwets=api.search("Key word you are searching for")

for a in twwets:
	# print(a.text)
	analysis=TextBlob(a.text)
	if(analysis >= 0):
		print("Positive")
		print(a.text)
	else:
		print("Negative")
		print(a.text)

#sentiment analysis using twitter api and textblob

import tweepy
from textblob import TextBlob

consumer_key='2aBkhROslozQWBzap6zFxYFIe'
consumer_secret='bLts6bAzUn9VNWRPCoGMjowugcEkAvMHmQjoTn6U3TBKxCbBv5'

access_key='895640034488991744-l4ADTbL74WehprC8hpVxcBEfgAxpTfH'
access_secret='bgETlXZH2MERcQbEwM4he0QqEfY0pKgsTVHUuk1mgLvBn'

#creating authentication variable
#to login into twitter via code 
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_key,access_secret)

api=tweepy.API(auth)

twwets=api.search("fani")

for a in twwets:
	# print(a.text)
	analysis=TextBlob(a.text)
	if(analysis >= 0):
		print("Positive")
		print(a.text)
	else:
		print("Negative")
		print(a.text)
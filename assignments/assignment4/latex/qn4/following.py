import tweepy
import time
import sys
import re

# Authentication Keys to Connect to Twitter API
consumer_key="vjemit5xYQdhgrEPa1FeFf5ZO";
consumer_secret="0PoNwIkHk29kUweChIIhGzVD3ZfXwRVqqwxYY3zPadY1BZeNq8";
access_token="3485785534-4FlFNlJtg1uNAlMummglVi9feR7fyvkUS0STp0G";
access_token_secret="EpzAYEpf6tHdGFKj43HhnBeAhLNgkyXPdZyH72ec8Ew8d";
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth) #Accessing tweepy API
counter=0

file1=open('following.csv','wb')

for user in tweepy.Cursor(api.friends, screen_name="Manoj_Chandra11",count=200).items#gets all my friends details on twitter
	print user.screen_name
	print user.friends_count
	file1.write("%s"% user.screen_name)
	file1.write(",%s\n"% user.friends_count)
         
import tweepy
import json
import time
import sys
import re

# Authentication Keys to Connect to Twitter API
consumer_key="4b8YancHWbKNEH0TUacuIcWtV";
consumer_secret="SxEB55jiA0iqtbQFr2H18ey848nN5JVvfhkyamxC7qshLAC9oP";
access_token="54493821-U0YHBtEr6LsODZh6QizuhtL6eCOTwkZEuLtFH56Yu";
access_token_secret="hRTDURCuaOaG8Ri8XqCzBLJ0HlL4PhBDyf13gBqn95ZjH";
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth) #Accessing tweepy API
counter=0

file1=open('follower.json','w')
file2=open('connections.json','w')
myarray={}
file1.write('{"nodes": [\n' )

for user in tweepy.Cursor(api.followers, screen_name="Manoj_Chandra11").items():
	counter+=1
	myarray['id']=counter
	myarray['screen_name']=user.screen_name
	myarray['name']=user.name
	file1.write(json.dumps(myarray))
	file1.write(',' )
file1.write('],' )
file1.write('\n"links": [\n' )
count=0
array2={}
for c in range(0,counter):
	array2['source']=0
	array2['target']=c+1
	file1.write(json.dumps(array2))
	file1.write(',' )
file1.write(']}' )
array3={}
for user in tweepy.Cursor(api.followers, screen_name="Manoj_Chandra11").items():
	

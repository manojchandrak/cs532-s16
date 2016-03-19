import tweepy
import json
import time
import sys
import re

consumer_key="4b8YancHWbKNEH0TUacuIcWtV"
consumer_secret="SxEB55jiA0iqtbQFr2H18ey848nN5JVvfhkyamxC7qshLAC9oP"
access_token="54493821-U0YHBtEr6LsODZh6QizuhtL6eCOTwkZEuLtFH56Yu"
access_token_secret="hRTDURCuaOaG8Ri8XqCzBLJ0HlL4PhBDyf13gBqn95ZjH"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
file1=open('follower.json','r')
# file2=open('processed.json','w')
# file3=open('file3.json','a')
file4=open('file4.json','w')
file5=open('file5.json','w')
line=json.load(file1)
counter=0
result={}
output={}
my_dict={}
names={}
def screens():
	file3=open('file3.json','r')
	line1=json.load(file3)
	for each in line1:
		if(each['following']==True or each['followed_by']==True):
			names['source']=each['source']
			names['target']=each['target']
			
			file4.write(json.dumps(names)+',\n')
			
def ids():
	file4=open('file4.json','r')
	line1=json.load(file4)
	# for each in line1:
		# if each['source']==line['nodes'][x]['screen_name'] and each['target']==line['nodes'][x]['screen_name']
			# names['source']=line['nodes'][x]['screen_name'] 
		
		for x in range(0,54):
			for each in line1:
				source1=each['source']
				target1=each['target']
			
				source=line['nodes'][x]['screen_name']
			
				names['source']=line['nodes'][x]['id']

			for y in range(x,54):
				if(source==source1 or source==target1):
				target=line['nodes'][y+1]['screen_name']
				output['target']=target
			
	
	
		
def function():
	file2=open('processed.json','r')
	line1=json.load(file2)
	for each in line1:
		source=each['source']
		target=each['target']
		con=api.show_friendship(source_screen_name=source,target_screen_name=target)
		my_dict['source']=con[0].screen_name
		my_dict['target']=con[1].screen_name
		my_dict['followed_by']=con[0].followed_by
		my_dict['following']=con[0].following
		file3.write(json.dumps(my_dict)+',\n')
	# for user in tweepy.Cursor(api.followers, screen_name="Manoj_Chandra11").items():
	# while True:
		# try:
		
			# counter+=1

def abc():
	for x in range(1,54):
		source=line['nodes'][x]['screen_name']
		output['source']=source

		for y in range(x,54):
			target=line['nodes'][y+1]['screen_name']
			output['target']=target
			file2.write(json.dumps(output)+',\n')




abc()	
function()
screens()					
				
	
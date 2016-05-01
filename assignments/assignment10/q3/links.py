import tweepy
import json
import time
import sys
import re
import urllib2
# Authentication Keys to Connect to Twitter API
consumer_key="vjemit5xYQdhgrEPa1FeFf5ZO";
consumer_secret="0PoNwIkHk29kUweChIIhGzVD3ZfXwRVqqwxYY3zPadY1BZeNq8";
access_token="3485785534-4FlFNlJtg1uNAlMummglVi9feR7fyvkUS0STp0G";
access_token_secret="EpzAYEpf6tHdGFKj43HhnBeAhLNgkyXPdZyH72ec8Ew8d";
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

outputFile = open('output2.json', 'w')  #opens the file with write permissions                          
        
all_urls = set()#for unique data
api = tweepy.API(auth) #Accessing tweepy API                                      
searches = tweepy.Cursor(api.search,q="news").items()#Querying for news related tweets

while True:                                                   # Infinite loop through tweets
    try:
        tweet = searches.next()# iterating through all the matched tweets
        item= tweet._json# converting the tweet object to JSON object
        myitem={}# declaring an empty array to store the details
		
        tweet_id= item['id_str']
        myitem['tweet_id'] = tweet_id# fetching the id of tweet and storing in JSON object
        #myitem['createdDate'] = created_date
        for link in item['entities']['urls']:
			  all_urls.add(link['url'])
			  
			  myitem['link']=link['expanded_url']#expanded url for full url
			  outputFile.write(json.dumps(myitem) + '\n')# writing JSON data to an output JSON file line by line
			  
			  
			
        
           
			
          
           
        if len(all_urls) == 1000:                        #Checks for 1000 urls in the list and breaks out if more
            break
    except tweepy.TweepError:# catching tweepy error which which occurs frequently enough
        time.sleep(60*10)
        continue
    except StopIteration:
        break

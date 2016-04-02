#!/usr/local/bin/python

import sys
import recommendations 
import operator 
def getRatings(ratingsfile):
	itemsdict = {}
	count=0
	for line in ratingsfile:
		(user_id, item_id, rating, timestamp) = line.split('\t')
		if user_id in itemsdict:
			itemsdict[user_id][item_id] = float(rating)
			
		else:
			count=count+1
			itemsdict[user_id]={}
	output= recommendations.topMatches(itemsdict,'33',n=count)
	top = output[:5]
	print 'top 5 correlated users to user 33 are'
	print top
	bot = output[-5:]
	print 'bottom 5 correlated users to user 33 are'
	print bot 
if __name__ == '__main__':
    

    ratingsfile = open ("../ml-100k/u.data", "r")
    ratings     = getRatings(ratingsfile)
    
    
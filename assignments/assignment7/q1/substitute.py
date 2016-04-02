import collections
import sys
from itertools import groupby
favmovies=[]
itemsdict ={}
itemsdict2={}
itemsdict3={}
leastdict={}
leastdict2={}
leastdict3={}
def userMovies(movilefile):
	c=0
	
	
	
	
	print 'top movies for user 33'
	print 'itemid  rating'
	for line in movilefile:
		(user_id, item_id, rating, timestamp ) = line.split('\t')
    
		rating = float(rating)
		try:
			if(user_id=='33'):      
				itemsdict[item_id].append(rating)
				
		except KeyError:
			itemsdict[item_id] = list()
			itemsdict[item_id].append( rating )
	for key, value in sorted(itemsdict.iteritems(),reverse=True, key=lambda (k,v): (v,k)):
		c=c+1
		if(c<4):
			print "%s: %s" % (key, value)
			favmovies.append(key)
		
	c=0
	moviefile.seek(0)
	print 'least favourite movies for user 33'
	print 'itemid  rating'
	for line in movilefile:
		(user_id, item_id, rating, timestamp ) = line.split('\t')
    
		rating = float(rating)
		try:
			if(user_id=='33'):      
				leastdict[item_id].append(rating)
				
		except KeyError:
			leastdict[item_id] = list()
			leastdict[item_id].append( rating )
	for key, value in sorted(leastdict.iteritems(), key=lambda (k,v): (v,k)):
		c=c+1
		if(c<4):
			print "%s: %s" % (key, value)
	
	c=0
	moviefile.seek(0)
	print 'top movies for user 37'
	print 'itemid  rating'
	for line in movilefile:
		(user_id, item_id, rating, timestamp ) = line.split('\t')
    
		rating = float(rating)
		try:
			if(user_id=='37'):
				itemsdict2[item_id].append(rating)
				
		except KeyError:
			itemsdict2[item_id] = list()
			itemsdict2[item_id].append( rating )
	for key, value in sorted(itemsdict2.iteritems(),reverse=True, key=lambda (k,v): (v,k)):
		c=c+1
		if(c<4):
			print "%s: %s" % (key, value)
			favmovies.append(key)
	c=0		   
	moviefile.seek(0)
	print 'least favourite movies for user 37'
	print 'itemid  rating'
	for line in movilefile:
		(user_id, item_id, rating, timestamp ) = line.split('\t')
    
		rating = float(rating)
		try:
			if(user_id=='37'):      
				leastdict2[item_id].append(rating)
				
		except KeyError:
			leastdict2[item_id] = list()
			leastdict2[item_id].append( rating )
	for key, value in sorted(leastdict2.iteritems(), key=lambda (k,v): (v,k)):
		c=c+1
		if(c<4):
			print "%s: %s" % (key, value)
	
	c=0
	moviefile.seek(0)
	print 'top movies for user 66'
	print 'itemid  rating'
	for line in movilefile:
		(user_id, item_id, rating, timestamp ) = line.split('\t')
    
		rating = float(rating)
		try:
			if(user_id=='66'):
				itemsdict3[item_id].append(rating)
				
		except KeyError:
			itemsdict3[item_id] = list()
			itemsdict3[item_id].append( rating )
	for key, value in sorted(itemsdict3.iteritems(),reverse=True, key=lambda (k,v): (v,k)):
		c=c+1
		if(c<4):
			print "%s: %s" % (key, value)
			favmovies.append(key)
	c=0
	moviefile.seek(0)
	print 'least favourite movies for user 66'
	print 'itemid  rating'
	for line in movilefile:
		(user_id, item_id, rating, timestamp ) = line.split('\t')
    
		rating = float(rating)
		try:
			if(user_id=='66'):      
				leastdict3[item_id].append(rating)
				
		except KeyError:
			leastdict3[item_id] = list()
			leastdict3[item_id].append( rating )
	for key, value in sorted(leastdict3.iteritems(), key=lambda (k,v): (v,k)):
		c=c+1
		if(c<4):
			print "%s: %s" % (key, value)
	
	c=0
	moviefile.seek(0)
def getUsers(userfile):
	count=0
	for line in userfile:
		line=line.split("|")
		id=line[0]
		age=line[1]
		gender=line[2]
		occupation=line[3]
		
		if(age=='23' and gender=='M' and occupation=='student' and count<3):
			count=count+1
			print 'top 3 substitutes'
			print 'id'+' '+ 'count'+' '+ 'occupation'+' '+' '+'gender'+ ' '+'age'
			print id,count,occupation,gender,age
		

def getTitles(imdbfile):
	ct=0	
	namesdict = {}
	print 'top movies of my substitutes' 
	for line in imdbfile:
		# print line
		line  = line.split("|")         
		id    = line[0]
		title = line[1]
        
		namesdict[ id ] = title
		for key,value in namesdict.items():
			try:
				if key==favmovies[ct] and ct<9:
					ct=ct+1
					print(key,value)
			except:
				pass
	print 'my final substitute is user 33 because i like 2 of his movies titanic and tomorrow never dies'			
       
  
	



if __name__=='__main__':
	userfile=open("u.user","r")
	moviefile=open("u.data","r")
	imdbfile=open("u.item","r")
	users=getUsers(userfile)
	movies=userMovies(moviefile)
	titles=getTitles(imdbfile)
	
	

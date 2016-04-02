import recommendations
import sys
from itertools import groupby
itemsdict ={}
def getTitles(imdbfile, movie_list):
	ct=0	
	namesdict = {}
	movie_id = []
	ratings=[]
	for i in movie_list:
		movie_id.append(i[1])
		ratings.append(i[0])
	movie_titles = []
	
	for line in imdbfile:
		# print line
		line  = line.split("|")         
		id    = line[0]
		title = line[1]
        
		namesdict[ id ] = title
		if id in movie_id:
			movie_titles.append(title)
			
	return movie_titles,ratings
	 
if __name__=='__main__':
	moviefile   = open("u.data","r")	
	
	pref_dic = {}
	rec=[]
	for line in moviefile:
		(user_id, item_id, rating, timestamp ) = line.split('\t')
		if user_id in pref_dic:
			pref_dic[user_id][item_id] = rating 
		else:
			pref_dic[user_id] = {}
	result = recommendations.getRecommendations(pref_dic, '33')
	rec.append(result)
	
	
		
		
		

	bottom5= result[-5:]
	
	top5 = result[:5]
	imdbfile=open("u.item","r")
	
	top_titles,rate=getTitles(imdbfile, top5)
	print "Top Movies are"
	for i in range(0,len(top_titles)):
		print top_titles[i],rate[i]
	
	imdbfile=open("u.item","r")
	bottom_titles,rate = getTitles(imdbfile, bottom5)
	print "Bottom Movies are"
	for j in range(0,len(bottom_titles)):
		print bottom_titles[j],rate[j]
	


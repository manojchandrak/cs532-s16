#!/usr/local/bin/python3
import re
import sys
import urllib2
import json

mymementos = re.compile(r'rel.*?=.*?"memento".*?')#use regular expressions to find mementos
file3=open('abovezerocounts.json','w')
file4=open('abovezerourls.json','w')

def getTimeMap(url):
    mem_url = "http://mementoproxy.cs.odu.edu/aggr/timemap/link/1/" + url #plug in the url to a timemap
    try:
        response = urllib2.urlopen(mem_url)
        timemap = response.read()
    except urllib2.HTTPError:
        timemap = None
    return timemap
    
def countMementos(mem_url):
	time_map = getTimeMap(mem_url)
	if not time_map:# if no time maps
		count=0
	else:
		
		
		count=len(mymementos.findall(str(time_map)))#finds the count of all mementos per url
		if count>0:
			file3.write("%s\n"% count)
			file4.write("%s\n"% time_map)
		#print count
	return count

if __name__=="__main__":
	file1=open('output.json','r')# input a json file that contains 1000 urls
	file2=open('memcount.json','w')
	#memcountlist=[]
	for line in file1.readlines():
		one_line = json.loads(line)# loads a json object
		link = one_line['link']
		counter=countMementos(link)# counter has count of the urls
		file2.write("%s"% counter)#outputs count of mementos of each url to a json file 
		file2.write("\r\n")
	#for item in memcountlist:
		
		
file1.close()
file2.close()
	
	
	 
	 
	 

    
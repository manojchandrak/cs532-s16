import os
import requests
import feedparser
import re
import sys

def getBlogs():
	# link='http://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117'
	# cmd="curl -I -L "+"'"+link+"'"
	link='http://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117'
	
	
	durls=set()
	
	while len(durls)<98:
		req=requests.get(link)
		durls.add(req.url)
		# link=req.url
	# print durls
	# file1=open('urls','w')
	file2=open('urlsappended','w')
	# for item in durls:
		# #print item + '\n'
		# file1.write(item + '\n')
	file2.write('http://f-measure.blogspot.com'+'/feeds/posts/default?alt=rss' +'\n')
	file2.write('http://ws-dl.blogspot.com/'+'/feeds/posts/default?alt=rss' +'\n')
	

	for item in durls:
		#print item + '\n'
		file2.write(item.strip('/?expref=next-blog')+'/feeds/posts/default?alt=rss' +'\n')
	


	


if __name__== '__main__':
	getBlogs()
	
import re
import json
import sys
import urllib
import urllib2
import urlparse
url='https://api.genderize.io/?name='

details={}
file1=open('gender.json','w')
file2=open('follower.json','r')
line=json.load(file2)
file1.write('[\n')
for x in range(1,54):
	name=line['nodes'][x]['name'].split()[0]
	
	uri=url+name
	url_response = urllib2.urlopen(uri)
	
	file1.write(urllib2.urlopen(uri).read())
	file1.write(',\n')
file1.write(']')
def function():
	file1=open('gender.json','r')
	file2=open('follower.json','w')
	line1=json.load(file1)
	for x in range(1,54):
		gender=line1[x]['name']
		line[x]['gender']=gender
		file2.write(line[x]['gender'])
		
# function()	
		

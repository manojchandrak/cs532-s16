#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
import commands
import math
import re
import json
import string
file=open('ten_files.txt','r')
file1=open('links.json','r').readlines()
count=0
count1=0
total=17000000000#corpus value for bing approx. 17 billion
doc_term=18000000#bing results for the queried word "crime""
idf_big=total/doc_term
print'TF       IDF        TFIDF          URIS'
for line in file.readlines():
	count=count+1
	all=string.maketrans('','')
	nodigs=all.translate(all, string.digits)
	found=line.translate(all, nodigs)
	foundint=int(found)
	
	
	occurence='grep -c ' +'crime '+ line.strip()
	words='wc -w '+line.strip()
	
	occur_doc=commands.getoutput(occurence)
	words_doc=commands.getoutput(words)
	words_total= words_doc.split(' ')[0]
	tf=round(float(occur_doc)/float(words_total),5)

	idf =round(math.log(idf_big)/math.log(2),5)
	tfidf=round(tf*idf,5)
	
	

	b=line.rstrip("processed.txt")
	
	for line1 in file1:
		try:
			
			count1=count1+1
			
			one_line1 = json.loads(line1)
			link1 = one_line1['link']
			
			if(count1==foundint):
					
				
				
				
				print tf,'  ',idf,'  ',tfidf,'  ',link1
				
				count1=0
				break
			else:
				continue
			
		
		except:
			pass

	
	
	

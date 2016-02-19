import re
import os
import json

if __name__=="__main__":
	f2name='raw.txt'
	f3name='processed.txt'
	count=0
	count1=0
	file1=open('links.json','r')# file which contains 1000 uris

	for line in file1.readlines():
		count=count+1
		newfile=str(count)+f2name #concatenates counter value to a string 
		one_line = json.loads(line)
		link = one_line['link']
	
		cmd="curl -s -L "+ link+" >./rawurls/"+ newfile # shell script to print raw html content of each uri
		os.system(cmd)
	for line in file1.readlines():
		count1=count1+1
		newfile1=str(count1)+f3name #concatenates counter value to a string 
		one_line1 = json.loads(line)
		link1 = one_line1['link']
		
		cmd1="lynx -dump -force_html "+ link1+" >./processedurls/"+ newfile1 # shell script to print processed html content of each uri
		os.system(cmd1)


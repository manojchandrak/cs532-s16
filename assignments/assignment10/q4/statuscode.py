
import requests
import json

file2 = open("links.json","r")
file= open("codecount.txt","w")


count=0

for line in file2:
	
	short=line.strip()
	one_line = json.loads(line)
	link = one_line['link']
	
	try:
		info=requests.get(link)
		if info.status_code==200:
			
			count=count+1
			print count
	except Exception, e:
		print e
		continue
file.write(count)
file.close()
	
	

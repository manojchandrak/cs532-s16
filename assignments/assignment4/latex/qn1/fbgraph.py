#!/usr/local/bin/python3
import csv
import sys
import numpy

from xml.dom.minidom import parseString


def friendData(xml):
    

    dom = parseString(xml)
    totalCount = {}

    for element in dom.getElementsByTagName("data"):
        if (element.attributes['key'].value == 'name'):
            name = element.childNodes[0].data 

        if (element.attributes['key'].value == 'friend_count'):
            count = element.childNodes[0].data
            
			
			

            totalCount[name] = count
            
			
			
            name = ''
            count = ''

    return totalCount

def countFriends(xml):

    dom = parseString(xml)
    return len(dom.getElementsByTagName("node"))


if __name__ == "__main__":
	sum=0
	counter=0
	

	graphmlFile = sys.argv[1]
	f = open(graphmlFile)
	f2=open('output.csv','w')
	xml = f.read()
	f.close()
	countProfFriend = countFriends(xml)
	fbFriends = friendData(xml)
	print("Friend _Name,Friend_Count")
	print('Michael Nelson,' + str(countProfFriend))
	f2.write("Friend,")
	f2.write("Count")
	f2.write("\r\n")
	f2.write("Michael Nelson ,")
	f2.write("%s\n" %str(countProfFriend))
	
	# f2.write("\r\n")


	for friend in fbFriends:
		# print(friend + ',' + fbFriends[friend])
		f2.write("%s ,"%friend)
		
		friend1=int(fbFriends[friend])
		sum+=friend1
		counter+=1
		# print friend1
		
		
		
	
		f2.write("%s\n"%fbFriends[friend])
	print "Mean = ",sum/counter 
	

	
	

	
	
	
	
	

	
    


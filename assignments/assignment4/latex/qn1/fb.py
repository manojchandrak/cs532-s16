#!/usr/local/bin/python3
import csv
import sys
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

	graphmlFile = sys.argv[1]
	f = open(graphmlFile)
	f2=open('output.txt','w')
	xml = f.read()
	f.close()
	countProfFriend = countFriends(xml)
	fbFriends = friendData(xml)
	print("Friend _Name,Friend_Count")
	print('Michael Nelson ' + str(countProfFriend))
	f2.write("%s " %str(countProfFriend))
	# f2.write("Friend,")
	# f2.write("Count")
	# f2.write("\r\n")
	f2.write("Michael Nelson ")
	
	f2.write("\r\n")


	for friend in fbFriends:
		print(friend + ',' + fbFriends[friend])
		f2.write("%s "%fbFriends[friend])
		f2.write("%s "%friend)
		
		f2.write("\r\n")
	# in_file = open("in.csv", "rb")
	# reader = csv.reader(in_file)
	# out_file = open("out.csv", "wb")
	# writer = csv.writer(out_file)
	# for row in fbFriends:
		# # row[1] = row
		# # row[2]=fbFriends[row]
		# writer.writerow(row)
	
  
		
	# with open('file.csv', 'wb') as f:
		# writer = csv.writer(f, delimiter=' ')
        # # takes the first `max` dictionaries from the list
		# for item in fbFriends[:limit]:
			# writer.writerow([item['year'], item['name']])
	

	
	
	
	
	

	
    


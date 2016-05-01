from random import random,randint
import math
import json

def cosine_similarity(v1,v2):
  "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
  sumxx, sumxy, sumyy = 0, 0, 0
  for i in range(0,len(v1)-1):
    x = int(v1[i]); y = int(v2[i])
    sumxx += x*x
    sumyy += y*y
    sumxy += x*y
  return sumxy/math.sqrt(sumxx*sumyy)


def getdistances(data,vec1):
  distancelist=[]
  
  # Loop over every item in the dataset
  for i in data:
		# print item
    for subitem in i:
      if subitem != 'F-Measure':
        vec2= i[subitem]
    
    # Add the distance and the index
    distancelist.append((cosine_similarity(vec1,vec2),i))
  
  # Sort by distance
  distancelist.sort()
  
  return distancelist

def knnestimate(data,vec1,k=20):
  # Get sorted distances
  print 'For Web Science blog and k=20'
  dlist=getdistances(data,vec1)
  avg=0.0
  # print dlist
  # Take the average of the top k results
  for i in range(k):
    idx=dlist[i]
    value = idx[0]
    for item in idx[1]:
		blogname= item
    print blogname +'\t'+ str(value)

def main():
	file1= open('bloglist','r')
	data = json.load(file1)
	
	for data1 in data:
	
		for data2 in data1:
			if data2 == 'Web Science and Digital Libraries Research Group':
				vec1= data1[data2]
				knnestimate(data,vec1)
			
main()
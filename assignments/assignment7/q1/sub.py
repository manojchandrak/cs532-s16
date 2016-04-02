def userMovies(movilefile):
	ratings=[]
	ratings2=[]
	ratings3=[]
	firstthree=[]
	count=0
	k=0
	# print 'top 3 for first substitute'
	for line in moviefile:
		line=line.split("\t")
		id=line[0]
		item=line[1]
		rating=line[2]
		
		
		
		
		
		if(id=='33'):
			count+=1
			ratings.append(rating)
	ratings.sort()
	ratings.reverse()
	# print ratings[0]
	moviefile.seek(0)
	c=0
	
	for line in moviefile:
		
		line=line.split("\t")
		id=line[0]
		item=line[1]
		rating=line[2]
		
		if (id=='33' and c<3):
		
			if(rating==ratings[0]):
				
				c=c+1
				k=k+1
				firstthree.insert(0,item)	
			if(rating==ratings[1] and k==1):
				firstthree.insert(1,item)
	
	# for i in firstthree[:3]:
		# print i
	print '-------------------'
	print 'for user 37'
	moviefile.seek(0)
	for line in moviefile:
		line=line.split("\t")
		id=line[0]
		item=line[1]
		rating=line[2]
		if(id=='37'):
			count+=1
			ratings2.append(rating)
	ratings2.sort()
	ratings2.reverse()
	print ratings2[0]
	moviefile.seek(0)
		
		
		
		
		if(id=='37'):
			count+=1
			ratings.append(rating)
	ratings2.sort()
	ratings2.reverse()
		
	
			
			
			

	
	

		
		
def getUsers(userfile):
	count=0
	for line in userfile:
		line=line.split("|")
		id=line[0]
		age=line[1]
		gender=line[2]
		occupation=line[3]
		
		if(age=='23' and gender=='M' and occupation=='student' and count<3):
			count=count+1
			print 'top 3 substitutes'
			print 'id'+' '+ 'count'+' '+ 'occupation'+' '+' '+'gender'+ ' '+'age'
			print id,count,occupation,gender,age
		
		

if __name__=='__main__':
	userfile=open("u.user","r")
	moviefile=open("u.data","r")
	# users=getUsers(userfile)
	movies=userMovies(moviefile)


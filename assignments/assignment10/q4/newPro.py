import os 


path= "/home/mkompal/wsprograms/a10/q4/processedurls/"

file1 = open('newprocessed','w')
directory = os.listdir(path)

for file in directory:

	final = path + file
	print final
	size= os.path.getsize(final)
	file1.write(str(size)+'\n')
import json
file1= open('blogmatrix.txt','r')
file2 = open('bloglist','w')
output = []
count = 0
for line in file1:
	count=count+ 1
	if count >1:  
		mydict = {}
		line = line.strip()
		input = line.split('\t')
		# print input
		name= input[0]
		input.pop(0)
		generated = input
		# print name
		# print generated
		mydict[name] = generated
		output.append(mydict)
file2.write(json.dumps(output))
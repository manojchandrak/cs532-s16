from datetime import datetime

now=datetime.now()
file1=open('created_dates.txt', 'r')
file2= open('numberdays.txt','w')

for line in file1.readlines() :
	print line
	dateUrl=line.strip().split()
	date = dateUrl[0]
	date_object = datetime.strptime(date,"%Y-%m-%dT%H:%M:%S")
	print date_object	
	days = (now - date_object).total_seconds() / ( 3600.0 * 24 )
	number_days = int(days)		
	file2.write("%s\n"% number_days)
	file2.write("\r\n")
# except:
	# date_object = datetime.strptime(line,"%Y-%m-%dT%H:%M:%S")   
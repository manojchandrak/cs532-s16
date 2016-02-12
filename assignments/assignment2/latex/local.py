from checkForModules import checkForModules
import json
from ordereddict import OrderedDict
#import simplejson
import urlparse
import re

from getBitly import getBitlyCreationDate
from getArchives import getArchivesCreationDate
from getGoogle import getGoogleCreationDate
from getBacklinks import *
from getLowest import getLowest

from getLastModified import getLastModifiedDate
#Topsy service is no longer available
#from getTopsyScrapper import getTopsyCreationDate
from htmlMessages import *
from pprint import pprint

from threading import Thread
import Queue
import datetime

import os,sys, traceback




def cd(url, backlinksFlag = False):

    #print 'Getting Creation dates for: ' + url


    #scheme missing?
    parsedUrl = urlparse.urlparse(url)
    if( len(parsedUrl.scheme)<1 ):
        url = 'http://'+url
    
    
    threads = []
    outputArray =['','','','','','']
    now0 = datetime.datetime.now()
    
   
    lastmodifiedThread = Thread(target=getLastModifiedDate, args=(url, outputArray, 0))
    bitlyThread = Thread(target=getBitlyCreationDate, args=(url, outputArray, 1))
    googleThread = Thread(target=getGoogleCreationDate, args=(url, outputArray, 2))
    archivesThread = Thread(target=getArchivesCreationDate, args=(url, outputArray, 3))
    
    if( backlinksFlag ):
        backlinkThread = Thread(target=getBacklinksFirstAppearanceDates, args=(url, outputArray, 4))

    #topsyThread = Thread(target=getTopsyCreationDate, args=(url, outputArray, 5))
    

    # Add threads to thread list
    threads.append(lastmodifiedThread)
    threads.append(bitlyThread)
    threads.append(googleThread)	
    threads.append(archivesThread)

    if( backlinksFlag ):
        threads.append(backlinkThread)

    #threads.append(topsyThread)	

    
    # Start new Threads
    lastmodifiedThread.start()
    bitlyThread.start()
    googleThread.start()
    archivesThread.start()

    if( backlinksFlag ):
        backlinkThread.start()

    #topsyThread.start()

    
    # Wait for all threads to complete
    for t in threads:
        t.join()
        
    # For threads
    lastmodified = outputArray[0]
    bitly = outputArray[1] 
    google = outputArray[2] 
    archives = outputArray[3] 
    
    if( backlinksFlag ):
        backlink = outputArray[4]
    else:
        backlink = ''

   
    
  
    try:

        lowest = getLowest([lastmodified, bitly, google, archives[0][1], backlink]) #for thread
    except:
       print sys.exc_type, sys.exc_value , sys.exc_traceback

    
    
 
    
    file2=open('dates.csv','a')
    print lowest
    file2.write("%s\n"% lowest)


file1=open('abovezerourls.json','r')

for line in file1.readlines():
	
	cd(line)
	
	
	
    




  
  
  






#!/usr/bin/env python
 
# get_links.py
 
import re

import sys
import urllib
import urllib2
import urlparse
from BeautifulSoup import BeautifulSoup

class MyOpener(urllib.FancyURLopener):

	

 
def parse(url):#user defined function to parse the url.
    mo = MyOpener()
    
    page = mo.open(url)
	
 
    text = page.read()
    page.close()
 
    soup = BeautifulSoup(text)#convert the page content into soup object
 
    for link in soup.findAll('a', href=True):#finds all links in the url
        link['href'] = urlparse.urljoin(url,link['href'])#parses the url and extracts a link into link['href']
        response=urllib2.urlopen(link['href'])#generates a response from each individual url
	
		
        message=response.info()#contains the response information i.e response header
        format=message.type#gives the format if it is plain text or pdf etc
        size=response.info().get("Content-length")#gets the size of the content in bytes.
		

		
        if format =="application/pdf"  :#verifies if the url is of pdf format
            print link['href']#prints the matching url i.e a pdf
            print "size is",size, "bytes and response code is ",response.getcode()# prints the size and status code
			
		

 
def main():
  
    for url in sys.argv[1:]:
        parse(url)#calls the parse method
# main()
 
if __name__ == "__main__":
    main()
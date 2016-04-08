#!/usr/bin/env python

import re
import sys
import feedparser
if __name__ == "__main__":

      matrixCreation()
def matrixCreation():
  nowords={}
  cap={}
  
  feedlist=[line for line in file('urlsappended')]
  for feedurl in feedlist:
    try:
      title,wc=getnowords(feedurl)
      nowords[title]=wc
      for word,count in wc.items():
        cap.setdefault(word,0)
        if count>1:
          cap[word]+=1
    except:
      print 'Parsing failed %s' % feedurl

  wordlist=[]
  repeatingWords = []
  for w,bc in cap.items():
    frac=float(bc)/len(feedlist)
    if frac>0.1 and frac<0.5:
      repeatingWords.append((w,bc))

  repeatingWords=sorted(repeatingWords,key=lambda x:x[1], reverse = True)

  for value in repeatingWords:

    value1 = value[0]
 
    value2 = value[1]
    length = len(wordlist)
    if(length < 500):   
      wordlist.append(value1)
    else:
      break

  out=file('blogdata.txt','w')
  out.write('Blog')

  for word in wordlist: 
    word1 = word.encode('UTF-8')
    out.write('\t%s' % word1)
  out.write('\n')

  for blog,wc in nowords.items():
    blogName = blog.encode('UTF-8')
    print blog
    out.write(blogName)
    for word in wordlist:
      if word in wc: out.write('\t%d' % wc[word])
      else: out.write('\t0')
    out.write('\n')
def getwords(html):

  txt=re.compile(r'<[^>]+>').sub('',html)


  words=re.compile(r'[^A-Z^a-z]+').split(txt)

  return [word.lower() for word in words if word!='']
def getnowords(url):

  d=feedparser.parse(url)
  wc={}


  for e in d.entries:
    if 'summary' in e: summary=e.summary
    else: summary=e.description


    words=getwords(e.title+' '+summary)
    for word in words:
      wc.setdefault(word,0)
      wc[word]+=1
  return d.feed.title,wc







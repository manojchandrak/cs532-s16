#!/usr/local/bin/python
import sys
import recommendationsedited

if __name__ == '__main__':
    
    outlier   = sys.argv[1]
    movie   = 'Shawshank Redemption, The (1994)'
    movie2='Smile Like Yours, A (1997)'
    
    count       = 5
    
    if outlier not in [ "top5", "bottom5"]:
        print "argument  1 must be either top5 or bottom5"
        sys.exit(1)
   
   
    prefs = recommendationsedited.loadMovieLens('../data')
    itemPrefs = recommendationsedited.transformPrefs(prefs)
    results   = recommendationsedited.topMatches(itemPrefs,movie,2000)
    results2= recommendationsedited.topMatches(itemPrefs,movie2,2000)
    
    if outlier == "top5":
		print 'for favourite movie Shawshank Redemption most correlated movies are'
		for i in results[0:count]:
          
			print i[0],i[1]
		print 'for least favourite movie A Smile like yours most correlated movies are'	
		for i in results2[0:count]:
          
			print i[0],i[1]
        
    
    if outlier == "bottom5":
		
    
        results.reverse()
        results2.reverse()
        print 'for favourite movie Shawshank Redemption least correlated movies are'
        for i in results[0:count]:
            #print i[0],i[1]
			print i	
        print 'for least favourite movie A Smile like yours bottom5 least correlated movies are'
        for i in results2[0:count]:
            #print i[0],i[1]
			print i
        


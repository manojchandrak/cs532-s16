#!/usr/local/bin/python

import sys
import recommendations 
import operator 
def getRatings(ratingsfile):
    
    itemsdict = {}

    for line in ratingsfile:
        (user_id, item_id, rating, timestamp) = line.split('\t')
    
        itemsdict.setdefault(user_id,{})
        itemsdict[user_id][item_id] = float(rating)
        
    #print itemsdict
    return itemsdict
    
if __name__ == '__main__':
    
    count       = int(sys.argv[1])
    ratingsfile = open ("../ml-100k/u.data", "r")
    ratings     = getRatings(ratingsfile)
    raters      = ratings.keys()
    ratecompare = {}
    
    for i in range(0,len(raters)):
        bestmatch = recommendations.topMatchesnegative(ratings,raters[i],n=len(raters))
                
        if bestmatch[0][1] == 33:
           
            pass
            
        if (bestmatch[0][1],33) not in ratecompare:
            ratecompare[(33, bestmatch[0][1])] = bestmatch[0][0]
            
    for item in sorted(
            ratecompare, key=ratecompare.get, reverse=False
    )[0:count]:
                
        print "{:>4} {:>4} {}".format(
            item[0],
            item[1],
            ratecompare[item]
        )
    
    
    
        
    

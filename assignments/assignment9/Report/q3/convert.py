#!/usr/bin/env python

import sys
from bs4 import BeautifulSoup
counter =33
file1 = open('karate.GraphML', 'r')
file2 = open('output1.json', 'w')
soup     = BeautifulSoup(file1, "html5lib")
file2.write('"nodes": [\n' )
for node in soup.find_all('node'):
        nodekeys = dict(node.attrs)
        id  = nodekeys[u'id']
        data_faction, data_name   = node.find_all('data')
        
        faction = data_faction.contents
        name    = data_name.contents

        id_split = id.split('n');       
        counternt           = id_split[1]
     
        file2.write('  {\n')
        file2.write('   "id": ')      
        file2.write( id_split[1])
        file2.write(',\n')

        file2.write('   "faction": ')      
        file2.write(faction[0])
        file2.write(',\n')

        file2.write('   "name": "')      
        file2.write(name[0])
        file2.write('"\n ')
         
        if counternt != 33:
            file2.write(' },\n')             
        else :
            file2.write(' }\n ],')            
        
 
file2.write('\n "links": [\n' )
for edge in soup.find_all('edge'):
        edgekeys  = dict(edge.attrs)        
        source = edgekeys[u'source']
        target = edgekeys[u'target']

        source_split = source.split('n')
        target_split = target.split('n')

        file2.write('  {\n')
        file2.write('   "source": ')      
        file2.write(source_split[1])
        file2.write(',\n')

        file2.write('   "target": ')      
        file2.write(target_split[1])
        file2.write('},\n')



file2.write(']} ')
    


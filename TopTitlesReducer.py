#!/usr/bin/env python3
import sys
import re
import operator


# input comes from STDIN
wordcount = dict()
for line in sys.stdin:
    key,mapdata = line.split('\t', 1)
    mapoutputkey,mapoutputcount = mapdata.split('-',1)
    wordcount[mapoutputkey]=int(mapoutputcount)

    # TODO



ret = sorted(wordcount.items(), key=lambda kv: kv[1] )
       
    
size = len(ret)
i=0
ans = list()
while(i<5 and i<size):
    ans.append(ret[size-i-1])
    #print ret[size-i-1]
    i+=1
    
ans.sort(key=lambda x: (-x[1], x[0]))
i=0
while(i<5):
    print(ans[i][0])
    print('%s\t%s' % (ans[i][0],ans[i][1]))
    i+=1   
    # print('%s\t%s' % (  ,  )) print as final output
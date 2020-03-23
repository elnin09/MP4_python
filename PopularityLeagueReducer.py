#!/usr/bin/env python3
import sys
#TODO


keydata = dict()
# input comes from STDIN
for line in sys.stdin:
    mapdata = (line.rstrip('\n')).split('\t',2)
    key,value = int(mapdata[1]),int(mapdata[2])


    if key in keydata.keys():
        keydata[key]=keydata[key]+1
        #if value not in keydata.keys():
            #keydata[value]=0
    else:
        keydata[key]=1
        if value not in keydata.keys():
            keydata[value]=0
        

ret = sorted(keydata.items(), key=lambda kv: kv[1] )

print(ret)

 


#TODO
# print('%s\t%s' % (  ,  )) print as final output
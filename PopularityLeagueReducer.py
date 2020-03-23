#!/usr/bin/env python3
import sys
#TODO


keydata = dict()
# input comes from STDIN
for line in sys.stdin:
    mapdata = (line.rstrip('\n')).split('\t',2)
    key,value = int(mapdata[1]),int(mapdata[2])
    keydata[key]=value


 
        

ret = sorted(keydata.items(), key=lambda kv: kv[1] )

print(ret)

 


#TODO
# print('%s\t%s' % (  ,  )) print as final output
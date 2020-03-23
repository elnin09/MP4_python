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


size = len(ret)
i=0
ans = list()
while(i<size):
    ans.append(ret[size-i-1])
    #print ret[size-i-1]
    i+=1


counter=0
for counter in range(1,len(ans)):
     ans[counter-1][1] = counter-1
     counter=counter+1


print(ans)

 


#TODO
# print('%s\t%s' % (  ,  )) print as final output
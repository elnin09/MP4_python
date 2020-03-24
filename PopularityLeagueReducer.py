#!/usr/bin/env python3
import sys
#TODO


keydata = dict()
# input comes from STDIN
for line in sys.stdin:
    mapdata = (line.rstrip('\n')).split('\t',2)
    key,value = mapdata[1],int(mapdata[2])
    keydata[key]=value


 
        

ret = sorted(keydata.items(), key=lambda kv: kv[1] )


size = len(ret)
i=0
ans = list()
while(i<size):
    ans.append(ret[size-i-1])
    #print ret[size-i-1]
    i+=1

retlist = [list(elem) for elem in ans]
retlist = retlist.reverse()
counter=0

retlistcopy = retlist


for counter in range(1,len(retlist)):
     retlist[counter-1][1] = counter-1
     if counter >  1 and (retlistcopy[counter-1]==retlistcopy[counter-2]):
         retlist[counter-1] = retlist[counter-2]
     counter=counter+1

retlist.sort(key=lambda x: (x[0],x[1]))

print(retlist)

 


#TODO
# print('%s\t%s' % (  ,  )) print as final output
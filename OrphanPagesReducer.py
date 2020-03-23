#!/usr/bin/env python3
import sys


#TODO
keydata = dict()

for line in sys.stdin:
  mapdata = (line.rstrip('\n')).split('\t',2)
  key,value = mapdata[1],mapdata[2]

  
  if key in keydata.keys():
    keydata[key]=keydata[key]+1
  else:
    if(key == value): 
      keydata[key] = 0
    else:
      keydata[key] = 1

ids = []

for key in keydata.keys():
  if keydata[key] == 0:
    ids.append(int(key))
ids.sort()

for id in ids:
  print(int(id))

#TODO
# print(xx) print as final output
#!/usr/bin/env python3
import sys


#TODO
keydata = dict()

for line in sys.stdin:
  key,value = (line.rstrip('\n')).split('\t',1)
  if key in keydata.keys():
    keydata[key]=keydata[key]+1
  else:
    keydata[key] = 1

for key in keydata.keys():
  if keydata[key] == 1:
     {
      print(key)
     }

#TODO
# print(xx) print as final output
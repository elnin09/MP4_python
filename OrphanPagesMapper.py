#!/usr/bin/env python3
import sys
import re


for line in sys.stdin:
  key,value = (line.rstrip('\n')).split(':',1);
  values = re.split(" ",value.lstrip(' '));

  print('%s\t%s' % (key,key))
  for i in values:
    print('%s\t%s' % (i,key))

  # TODO
  
  # print('%s\t%s' % (  ,  )) pass this output to reducer

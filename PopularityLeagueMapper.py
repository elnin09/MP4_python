#!/usr/bin/env python3
import sys


leaguePath = sys.argv[1]
#TODO

with open(leaguePath) as f:
       data = f.read()
       words = re.split("\\n|\\s",data)
	





for line in sys.stdin:
       key,value = (line.rstrip('\n')).split(':',1);
       values = re.split(" ",value.lstrip(' '));

       for i in values:
              if i in words:
                     print('%s\t%s\t%s' % (1,i,key.rstrip('\n')))

       #TODO

       # print('%s\t%s' % (  ,  )) pass this output to reducer

#!/usr/bin/env python3
from operator import itemgetter
import sys
import re

#TODO

wordcount = dict()

# input comes from STDIN
for line in sys.stdin:
    print(line)
    linesplit=re.split(" ",line)
    getter = itemgetter(0)
    getterval = getter(linesplit)
    if getterval[0] in wordcount:
        wordcount[getterval[0]] = wordcount[getterval[0]] +11
    else:
        wordcount[getterval[0]] = 1


# TODO
for  k in wordcount.keys():
    print('%s\t%s' % (k,wordcount[k])) 

# print('%s\t%s' % (  ,  )) print as final output
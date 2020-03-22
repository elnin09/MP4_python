#!/usr/bin/env python3
from operator import itemgetter
import sys

#TODO

wordcount = dict()

# input comes from STDIN
for line in sys.stdin:
    getter = itemgetter(0,1)
    getterval = getter(line)
    if getterval[0] in wordcount:
        wordcount[getterval[0]] = wordcount[getterval[0]] +11
    else:
        wordcount[getterval[0]] = 1


# TODO
for  k in wordcount.keys():
    print('%s\t%s' % (k,wordcount[k])) 

# print('%s\t%s' % (  ,  )) print as final output
#!/usr/bin/env python3
import sys




for line in sys.stdin:
       mapoutput = line.split('\t', 1)
       print('%s\t%s\t%s' % (1,mapoutput[0],mapoutput[1]))

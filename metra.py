#!/usr/bin/python

import re
import sys

# Collect the two rows of data.
start = sys.stdin.readline().split()
stop = sys.stdin.readline().split()

# Change leading zeros to two spaces.
start = [re.sub(r'^0', '  ', s) for s in start]
stop = [re.sub(r'^0', '  ', s) for s in stop]

# Print the data as two columns, using a simple heuristic for am/pm.
ap = 'a'
for i in range(0, len(start)):
  if start[i][0:2] == '12':
    if ap == 'a':
      ap = 'p'
    else:
      ap = 'a'
  
  print ' %s%s          %s%s' % (start[i], ap, stop[i], ap)

  
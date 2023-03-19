#!/usr/bin/python3
import sys

numArgvs = len(sys.argv)
if numArgvs != 2:
    sys.stderr.write('Usage: %s inputFiles\n' % sys.argv[0])
    sys.exit(1)

try:
    fh = open(sys.argv[1], 'r')
except:
    sys.stderr.write('cannot open input file %s\n' % sys.argv[1])
    sys.exit(2)

prevLine = ''
for line in fh.readlines():
    if line != prevLine:
        print(line, end='')
        prevLine = line
fh.close()
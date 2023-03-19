#!/usr/bin/python3
import sys

numArgvs = len(sys.argv)
if numArgvs != 3:    # [1] pattern; [2] input file
    sys.stderr.write('Usage: %s inputFiles\n' % sys.argv[0])
    sys.exit(1)

try:
    fh = open(sys.argv[2], 'r')
except:
    sys.stderr.write('cannot open input file %s\n' % sys.argv[1])
    sys.exit(2)

for line in fh.readlines():
    if line.find(sys.argv[1]) != -1:    # matched
        print(line, end='')

fh.close()
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

lines = words = chars = 0
for line in fh.readlines():
    lines += 1
    words += len(line.split())
    chars += len(line)
fh.close()
print(f'{lines:8d}{words:8d}{chars:8d} {sys.argv[1]}')
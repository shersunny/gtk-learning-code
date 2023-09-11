#!/usr/bin/env python
import sys

# Input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    count, match = line.split('\t', 1)
    print(f'{match}\t{count}')

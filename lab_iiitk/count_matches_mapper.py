#!/usr/bin/env python
import sys
import re

# Input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    # Your regex pattern for matching goes here
    pattern = r'your_regex_pattern_here'
    matches = re.findall(pattern, line)
    for match in matches:
        # Emit the match as the key and '1' as the value
        print(f'{match}\t1')

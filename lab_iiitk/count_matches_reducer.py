#!/usr/bin/env python
import sys

current_match = None
match_count = 0

# Input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    match, count = line.split('\t', 1)
    
    # Convert count to an integer
    try:
        count = int(count)
    except ValueError:
        continue

    # If the current match is the same as the previous one, increment the count
    if current_match == match:
        match_count += count
    else:
        # Print the previous match and its count
        if current_match:
            print(f'{current_match}\t{match_count}')
        current_match = match
        match_count = count

# Don't forget to print the last match
if current_match:
    print(f'{current_match}\t{match_count}')

#!/usr/bin/env python

import sys

sys.stdin = open("smapout.txt", "r")
sys.stdout = open("redout.txt", "w")

current_key = None
current_weight_sum = 0
current_parcel_sum = 0
key = None

for line in sys.stdin:
    line = line.strip()

    # Parse the input we got from mapper
    key, val_1, val_2 = line.split('\t', 2)

    # convert count (currently a string) to int
    try:
        val_1 = float(val_1)
        val_2 = int(val_2)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_key == key:
        current_weight_sum += val_1
        current_parcel_sum += val_2
    else:
        if current_key != None:
            # write result to STDOUT
            print(f'{current_key}\t{current_weight_sum}\t{current_parcel_sum}')

        current_weight_sum = val_1
        current_parcel_sum = val_2
        current_key = key

# do not forget to output the last word if needed!
if current_key == key:
    print(f'{current_key}\t{current_weight_sum}\t{current_parcel_sum}')

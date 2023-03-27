#!/usr/bin/env python

import sys

sys.stdin = open("smapout.txt", "r")
sys.stdout = open("redout.txt", "w")

current_key = None
current_weight_sum = 0
current_parcel_sum = 0

current_zone = None
current_zone_count = 0
zone_dict = {}

key = None

for line in sys.stdin:
    line = line.strip()

    # Parse the input we got from mapper
    key, val_1, val_2, zone = line.split('\t', 3)

    # convert count (currently a string) to int
    try:
        val_1 = float(val_1)
        val_2 = int(val_2)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # For this key, put the zone count into the dictionary
    if zone != None and zone in zone_dict:
        zone_dict[zone] += 1
    else:
        zone_dict.setdefault(zone, 1)

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_key == key:
        current_weight_sum += val_1
        current_parcel_sum += val_2
    else:
        if current_key != None:
            # write result to STDOUT
            print(
                f'{current_key}\t{current_weight_sum}\t{current_parcel_sum}', end='')

            # Write zones for this key
            [print(f'\t{zone}\t{zone_count}', end='')
             for [zone, zone_count] in zone_dict.items()]
            print()

        current_weight_sum = val_1
        current_parcel_sum = val_2
        current_key = key
        zone_dict = {}

# do not forget to output the last word if needed!
if current_key == key:
    if zone in zone_dict:
        zone_dict[zone] += 1
    else:
        zone_dict.setdefault(zone, 1)
    print(f'{current_key}\t{current_weight_sum}\t{current_parcel_sum}', end='')
    # Write zones for this key
    [print(f'\t{zone}\t{zone_count}', end='')
        for [zone, zone_count] in zone_dict.items()]

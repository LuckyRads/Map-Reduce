#!/usr/bin/env python
import sys

sys.stdin = open("mapout.txt", "r")
sys.stdout = open("smapout.txt", "w")

sorted_list = []

for line in sys.stdin:
    key, val_1, val_2, val_3 = line.strip().split('\t', 3)
    sorted_list.append([key, val_1, val_2, val_3])

# Sort the list by keys and geographic zones
sorted_list.sort(key=lambda tup: (tup[0], tup[3]))

for el in sorted_list:
    print(f'{el[0]}\t{el[1]}\t{el[2]}\t{el[3]}')

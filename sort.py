#!/usr/bin/env python
import sys

sys.stdin = open("mapout.txt", "r")
sys.stdout = open("smapout.txt", "w")

sorted_list = []

for line in sys.stdin:
    key, val_1, val_2 = line.strip().split('\t', 2)
    sorted_list.append([key, val_1, val_2])

sorted_list.sort(key=lambda tup: tup[0])

for el in sorted_list:
    print(f'{el[0]}\t{el[1]}\t{el[2]}')

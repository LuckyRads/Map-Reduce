#!/usr/bin/env python
import sys

sys.stdin = open("duom_full.txt", "r")
# sys.stdin = open("duom_cut.txt", "r")
sys.stdout = open("mapout.txt", "w")

main_field = 'marsrutas'
second_field = 'svoris'
third_field = 'siuntu skaicius'
fourth_field = 'geografine zona'

for line in sys.stdin:
    line = line.strip()
    line = line[2:len(line)-2]
    stripped_string = line.split('}}{{')

    for data_entry in stripped_string:
        parsed_strings = data_entry.split('}{')

        map_key = None
        map_value_1 = None
        map_value_2 = None
        map_value_3 = None

        for parsed_string in parsed_strings:
            (key, value) = parsed_string.split('=')

            # Skip iteration if value is empty
            if value == '':
                continue

            if key == main_field:
                map_key = int(value)
            if key == second_field:
                map_value_1 = float(value)
            if key == third_field:
                map_value_2 = int(value)
            if key == fourth_field:
                map_value_3 = value

        if(map_key != None and map_value_1 != None and map_value_2 != None and map_value_3 != None):
            print(f'{map_key}\t{map_value_1}\t{map_value_2}\t{map_value_3}')

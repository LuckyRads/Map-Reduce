#!/usr/bin/env python
import sys

sys.stdin = open("duom_cut.txt", "r")
sys.stdout = open("map_parcel_out.txt", "w")

main_field = 'marsrutas'
secondary_field = 'siuntu skaicius'

for line in sys.stdin:
    line = line.strip()
    line = line[2:len(line)-2]
    stripped_string = line.split('}}{{')

    for data_entry in stripped_string:
        parsed_strings = data_entry.split('}{')

        map_key = None
        map_value = None

        for parsed_string in parsed_strings:
            (key, value) = parsed_string.split('=')

            # Skip iteration if value is empty
            if value == '':
                continue

            if key == main_field:
                map_key = int(value)
            elif key == secondary_field:
                map_value = int(value)

        if(map_key != None and map_value != None):
            print('%s\t%s' % (map_key, map_value))

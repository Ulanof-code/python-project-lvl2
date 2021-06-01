#!/usr/bin/env python3

import json
import argparse

parser = argparse.ArgumentParser(description="Generate diff")

# Positional args:
parser.add_argument('first_file')
parser.add_argument('second_file')

# Optional args:
parser.add_argument('-f', '--format', type=str, help='set format of output', default='JSON')

args = parser.parse_args()


def generate_diff(file1, file2):
    data1 = json.load(open(file1))
    data2 = json.load(open(file2))
    result = '{\n'
    sorted_keys = sorted(set(sorted(data1) + sorted(data2)))

    for key in sorted_keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                result += '  {} {}: {} \n'.format(' ', key, data1[key])
            else:
                result += '  {} {}: {} \n'.format('-', key, data1[key])
                result += '  {} {}: {} \n'.format('+', key, data2[key])
        if key in data1 and key not in data2:
            result += '  {} {}: {} \n'.format('-', key, data1[key])
        if key in data2 and key not in data1:
            result += '  {} {}: {} \n'.format('+', key, data2[key])
    return result + '}'

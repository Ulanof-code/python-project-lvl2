#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="Generate diff")

# Positional args:
parser.add_argument('first_file')
parser.add_argument('second_file')

# Optional args:
parser.add_argument('-f', '--format', type=str, help='set format of output', default='JSON')

args = parser.parse_args()


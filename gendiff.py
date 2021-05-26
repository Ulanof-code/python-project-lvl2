#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="Generate diff")
parser.add_argument('first_file')
parser.add_argument('second_file')
args = parser.parse_args()
print(args.first_file, args.second_file)

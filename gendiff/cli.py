#!/usr/bin/env python3
from gendiff import gendiff
import argparse


def get_args():
    parser = argparse.ArgumentParser(description="Generate diff")
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        type=str,
                        help='set format of output',
                        default='JSON'
                        )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    print(gendiff.generate_diff(get_args().first_file, get_args().second_file))

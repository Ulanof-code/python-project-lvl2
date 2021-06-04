#!/usr/bin/env python3
from gendiff.gendiff import generate_diff
from gendiff.parser import parse
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
    print(
        generate_diff(
            parse(get_args().first_file),
            parse(get_args().second_file)
        )
    )

#!/usr/bin/env python3
from gendiff.gendiff import generate_output
from gendiff.parser import parse
import argparse


def get_args():
    parser = argparse.ArgumentParser(description="Generate diff")
    parser.add_argument('first_file', help='First argument')
    parser.add_argument('second_file', help='Second argument')
    parser.add_argument('-f', '--format',
                        type=str,
                        help='What is the output format?',
                        default='stylish'
                        )
    args = parser.parse_args()
    return args


def main():
    print(
        generate_output(
            parse(get_args().first_file),
            parse(get_args().second_file),
            format_output=get_args().format
        )
    )


if __name__ == "__main__":
    main()
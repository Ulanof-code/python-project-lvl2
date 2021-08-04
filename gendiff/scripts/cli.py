#!/usr/bin/env python3
from gendiff.gendiff import generate_diff
import argparse
from gendiff.formatters.formats import FORMATS


def get_args():
    parser = argparse.ArgumentParser(description="Generate diff")
    parser.add_argument('first_file', help='First argument')
    parser.add_argument('second_file', help='Second argument')
    parser.add_argument('-f', '--format',
                        type=str,
                        help='What is the output format?',
                        default='stylish',
                        choices=FORMATS
                        )
    return parser


def main():
    args = get_args().parse_args()
    print(
        generate_diff(args.first_file, args.second_file, format_output=args.format)
    )


if __name__ == "__main__":
    main()

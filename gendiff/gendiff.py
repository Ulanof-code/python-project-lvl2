from gendiff.make_diff import make_diffs_representation
from gendiff.formatters.plain import make_plain
from gendiff.formatters.stylish import make_stylish
from gendiff.formatters.json import make_json
from typing import Dict


def generate_diff(data1: Dict,
                  data2: Dict,
                  format_output='stylish') -> str:
    diffs = make_diffs_representation(data1, data2)
    if format_output == 'plain':
        return make_plain(diffs)
    elif format_output == 'json':
        return make_json(diffs)
    return make_stylish(diffs)

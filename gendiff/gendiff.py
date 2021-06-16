from gendiff.make_diff import get_diff
from gendiff.formatters.plain import make_plain
from gendiff.formatters.stylish import make_stylish


def generate_output(data1, data2, format_output='stylish'):
    diffs = get_diff(data1, data2)
    if format_output == 'plain':
        return make_plain(diffs)
    return make_stylish(diffs)

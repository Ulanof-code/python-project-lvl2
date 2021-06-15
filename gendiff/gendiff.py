from gendiff.make_diff import get_diff
from gendiff.formatters.stylish import make_stylish


def generate_diff(data1, data2):
    inside_view = get_diff(data1, data2)
    return make_stylish(inside_view)
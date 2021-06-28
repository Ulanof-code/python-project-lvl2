from gendiff.make_diff import make_diffs_representation
from gendiff.formatters.plain import make_plain
from gendiff.formatters.stylish import make_stylish
from gendiff.formatters.json import make_json
from gendiff.parser import get_dict_from_file
from gendiff.formatters.formats import STYLISH, PLAIN, JSON


def generate_diff(first_file: str,
                  second_file: str,
                  format_output=STYLISH) -> str:
    dict1 = get_dict_from_file(first_file)
    dict2 = get_dict_from_file(second_file)
    diffs = make_diffs_representation(dict1, dict2)
    if format_output == PLAIN:
        return make_plain(diffs)
    elif format_output == JSON:
        return make_json(diffs)
    return make_stylish(diffs)

from gendiff.make_diff import make_diffs
from gendiff.formatters.plain import make_plain
from gendiff.formatters.stylish import make_stylish
from gendiff.formatters.json import make_json
from gendiff.parser import get_dict_from_file
from gendiff.formatters.formats import FORMATS


def generate_diff(first_path: str,
                  second_path: str,
                  format_output='stylish') -> str:
    """
    The formatter is selected in FORMATS: tuple, where [0] == 'stylish', [1] == 'plain', [2] == 'json'

    Args:
        first_path:
        second_path:
        format_output:

    Returns:
        Formatted output.
    """
    dict1 = get_dict_from_file(first_path)
    dict2 = get_dict_from_file(second_path)
    diffs = make_diffs(dict1, dict2)
    if format_output not in FORMATS:
        raise NotImplementedError(f"The format {format_output} is not supported")
    elif format_output == FORMATS[1]:  # plain
        return make_plain(diffs)
    elif format_output == FORMATS[2]:  # json
        return make_json(diffs)
    return make_stylish(diffs)  # stylish

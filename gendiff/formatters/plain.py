from gendiff.make_diff import get_value, get_changed_value, get_condition
from typing import Dict, Any
from gendiff.make_diff import REMOVED, ADDED, CHANGED, IS_DICT

PROPERTY = 'Property'


def make_plain(diffs: Dict) -> str:
    plain_output = format_diffs_to_plain(diffs)
    if plain_output:
        return plain_output
    else:
        return '{}'


def format_diffs_to_plain(diffs: Dict,
                          parent_name='') -> str:  # noqa: C901
    """
    Formatting the difference representation to plain output
    parameters:
        2. diffs: list[dict{}], inside differences representation
        1. parent_name: str,  parent node name.
    return:
        str
    """
    sorted_keys = sorted(diffs.keys())
    line_buffer = []
    for key in sorted_keys:
        condition = get_condition(diffs[key])
        value = get_value(diffs[key])
        changed_value = get_changed_value(diffs[key])
        if parent_name == '':
            key_full_path = key
        else:
            key_full_path = f'{parent_name}.{key}'
        new_path = f"'{key_full_path}'"
        if condition == CHANGED:
            line_buffer.append(
                f'{PROPERTY} {new_path} was updated. From {value_to_string(value)} to {value_to_string(changed_value)}'
            )
        elif condition == ADDED:
            line_buffer.append(
                f'{PROPERTY} {new_path} was added with value: {value_to_string(value)}'
            )
        elif condition == REMOVED:
            line_buffer.append(
                f'{PROPERTY} {new_path} was removed'
            )
        elif condition == IS_DICT:
            line_buffer.append(format_diffs_to_plain(diffs[key]['value'], parent_name=key_full_path))
    return '\n'.join(line_buffer)


def value_to_string(value: Any) -> str:
    """
    Convert value to string.
    Convert Python "False" and "True" to lowercase.
    Convert Python "None" to "null".
    Adds '' around String.
    Convert other types to "[complex value]".
    :param value: in any format.
    :return: str.
    """
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, str):
        return f"'{value}'"
    if isinstance(value, (int, float, complex)):
        return str(value)
    return "[complex value]"

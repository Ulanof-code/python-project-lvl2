from gendiff.make_diff import (get_value, get_condition, get_name, CONDITIONS)
from typing import List, Any


def make_plain(diffs: List[dict]) -> str:
    plain_output = generate_plain_string(diffs)
    if plain_output:
        return plain_output[:-1]
    else:
        return '{\n}'


def generate_plain_string(diffs: List[dict],
                          parent_name='') -> str:  # noqa: C901
    """
    Formatting the difference representation to plain output
    parameters:
        2. diffs: list[dict{}], inside differences representation
        1. parent_name: str,  parent node name.
    return:
        str
    """
    result_string: str = ""
    for diff in diffs:
        name: str = get_name(diff)
        condition: str = get_condition(diff)
        value: Any = get_value(diff)
        if parent_name:
            key_full_path: str = f"{parent_name}.{name}"
        else:
            key_full_path = name
        base_string = f"Property '{key_full_path}' was"
        value_string = formatting_value_to_string(value)
        if condition == CONDITIONS['IS_DICT']:
            result_string += generate_plain_string(value, parent_name=key_full_path)  # noqa: E501
        elif condition == CONDITIONS['CHANGED_OLD']:
            result_string += f"{base_string} updated. From {value_string} to "
        elif condition == CONDITIONS['CHANGED_NEW']:
            result_string += f"{value_string}\n"
        elif condition == CONDITIONS['ADDED']:
            result_string += f"{base_string} added with value: {value_string}\n"  # noqa: E501
        elif condition == CONDITIONS['REMOVED']:
            result_string += f"{base_string} removed\n"
        else:  # same
            pass
    return result_string


def formatting_value_to_string(value: Any) -> str:
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

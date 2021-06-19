from gendiff.make_diff import (get_value, get_condition, get_name, CONDITIONS)
import numbers


def make_plain(diffs):
    plain_output = generate_plain_string(diffs)
    if plain_output:
        return plain_output[:-1]
    else:
        return '{\n}'


def generate_plain_string(diffs, parent_name=''):  # noqa: C901
    """
    Formatting the difference representation to plain output
    parameters:
        2. diffs: list[dict{}], inside differences representation
        1. parent_name: str,  parent node name.
    return:
        str
    """
    result_string = ""
    for diff in diffs:
        name = get_name(diff)
        condition = get_condition(diff)
        value = get_value(diff)
        if parent_name:
            key_full_path = f"{parent_name}.{name}"
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


def formatting_value_to_string(value):
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
    if isinstance(value, numbers.Number):
        return str(value)
    return "[complex value]"

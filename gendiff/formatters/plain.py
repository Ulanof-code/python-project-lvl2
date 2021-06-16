from gendiff.make_diff import (get_value, get_condition, get_name, CONDITIONS)
import numbers


def make_plain(diffs):
    long_string = generate_comparison_output_long_string(diffs)
    if long_string:
        short_string = long_string[:-1]  # removing last \n
        return short_string
    return long_string


def generate_comparison_output_long_string(diffs, parent_key=''):  # noqa: C901
    """
    Generate plain formatted string from comparison list.
    :param parent_key: name of parent key,  str.
    :param diffs: comparisons, List[Dict[str, Any]].
    :return: str.
    """
    result_string = ""
    for diff in diffs:
        name = get_name(diff)
        condition = get_condition(diff)
        value = get_value(diff)
        key_full_path = f"{parent_key}.{name}" if parent_key else name
        property_was = f"Property '{key_full_path}' was"
        value_string = convert_value_to_string(value)
        if condition == CONDITIONS['IS_DICT']:
            result_string += generate_comparison_output_long_string(value, parent_key=key_full_path)  # noqa: E501
        elif condition == CONDITIONS['CHANGED_OLD']:
            result_string += f"{property_was} updated. From {value_string} to "
        elif condition == CONDITIONS['CHANGED_NEW']:
            result_string += f"{value_string}\n"
        elif condition == CONDITIONS['ADDED']:
            result_string += f"{property_was} added with value: {value_string}\n"  # noqa: E501
        elif condition == CONDITIONS['REMOVED']:
            result_string += f"{property_was} removed\n"
        else:  # same
            pass
    return result_string


def convert_value_to_string(value):
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

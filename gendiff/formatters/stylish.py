from gendiff.make_diff import (get_value, get_condition, get_name, CONDITIONS)
from typing import Dict, List, Any


FLAGS: Dict = {
    'is_dict': '',
    'changed_new': '+',
    'changed_old': '-',
    'related': ' ',
    'added': '+',
    'removed': '-',
}

INDENT = '    '


def make_stylish(
        diff: List[dict],
        level=0):
    result: str = '{'
    indent: str = INDENT * level
    for node in diff:
        result += '\n'
        name: str = get_name(node)
        condition: str = get_condition(node)
        value: Any = get_value(node)
        flag: str = FLAGS[condition]
        if condition == CONDITIONS['IS_DICT']:
            result += f'{indent}  {flag}  {name}: '
            result += make_stylish(value, level + 1)
        else:
            value = formatting_value_to_string(value, indent + INDENT)
            result += f'{indent}  {flag} {name}: {value}'
    result += f'\n{indent}}}'
    return result


def formatting_value_to_string(value: Any,
                               indent: str) -> str:
    """
    Convert value to string.
    Convert Python "False" and "True" to lowercase.
    Convert Python "None" to "null".
    :param indent: indent via spaces, str.
    :param value: in any format.
    :return: str.
    """
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, dict):
        string = "{\n"
        for key, value in value.items():
            string += f"{INDENT}{indent}{key}: "
            string += formatting_value_to_string(value, indent=indent + INDENT)
            string += "\n"
        string += f"{indent}}}"
        return string
    return str(value)

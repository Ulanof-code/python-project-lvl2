from gendiff.make_diff import (get_value, get_changed_value, get_condition, get_name, CONDITIONS)
from typing import Dict, Any


FLAGS: Dict = {
    'changed': '',
    'is_dict': '',
    'changed_old': '-',
    'changed_new': '+',
    'related': ' ',
    'added': '+',
    'removed': '-',
}

INDENT = '    '


def make_stylish(
        diff,
        level=0):
    sorted_keys = sorted(diff.keys())
    result: str = '{'
    indent: str = INDENT * level
    for key in sorted_keys:
        result += '\n'
        name: str = get_name(diff[key])
        condition: str = get_condition(diff[key])
        value: Any = get_value(diff[key])
        changed_value = get_changed_value(diff[key])
        flag: str = FLAGS[condition]
        if condition == CONDITIONS['IS_DICT']:
            result += f'{indent}  {flag}  {name}: '
            result += make_stylish(value, level + 1)
        else:
            if condition == 'changed':
                flag = FLAGS['changed_old']
                value = formatting_value_to_string(value, indent + INDENT)
                result += f'{indent}  {flag} {name}: {value}\n'
                flag = FLAGS['changed_new']
                changed_value = formatting_value_to_string(changed_value, indent + INDENT)
                result += f'{indent}  {flag} {name}: {changed_value}'
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

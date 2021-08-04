from gendiff.make_diff import get_value, get_changed_value, get_condition, get_name
from typing import Dict, Any
from gendiff.make_diff import CHANGED, NESTED


FLAGS: Dict = {
    'changed': '',
    'nested': '',
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
        name = get_name(diff[key])
        condition = get_condition(diff[key])
        value = get_value(diff[key])
        changed_value = get_changed_value(diff[key])
        flag = FLAGS[condition]
        if condition == NESTED:
            result += f'{indent}  {flag}  {name}: '
            result += make_stylish(value, level + 1)
        elif condition == CHANGED:
            flag = FLAGS['changed_old']
            value = format_value_to_string(value, indent + INDENT)
            result += f'{indent}  {flag} {name}: {value}\n'
            flag = FLAGS['changed_new']
            changed_value = format_value_to_string(changed_value, indent + INDENT)
            result += f'{indent}  {flag} {name}: {changed_value}'
        else:
            value = format_value_to_string(value, indent + INDENT)
            result += f'{indent}  {flag} {name}: {value}'
    result += f'\n{indent}}}'
    return result


def format_value_to_string(value: Any,
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
        return dict_to_string(value, indent)
    return str(value)


def dict_to_string(value: Any, indent: str) -> str:
    string = "{\n"
    for key, value in value.items():
        string += f"{INDENT}{indent}{key}: "
        string += format_value_to_string(value, indent=indent + INDENT)
        string += "\n"
    string += f"{indent}}}"
    return string

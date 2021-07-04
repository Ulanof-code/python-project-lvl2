from gendiff.make_diff import get_condition, get_name, get_changed_value, get_value
import json
from typing import Dict
from gendiff.make_diff import CHANGED, IS_DICT


def make_json(diffs: Dict) -> str:
    """
    Formatting the difference representation to json
    The formatter is selected in FORMATS: tuple, where [0] == 'stylish', [1] == 'plain', [2] == 'json'
    :param:
        diffs: dict.
    :return:
        str.
    """
    formatted_dict = dict_formatting(diffs)
    json_output = json.dumps(formatted_dict, sort_keys=True, indent=4)
    if not formatted_dict:
        return '{}'
    return json_output


def dict_formatting(diffs: Dict) -> Dict:
    result = {}
    for diff in diffs:
        name = get_name(diffs[diff])
        condition = get_condition(diffs[diff])
        value = get_value(diffs[diff])
        changed_value = get_changed_value(diffs[diff])
        current_key = str(name)
        if condition == IS_DICT:
            value = dict_formatting(value)
            result[current_key] = {
                'condition': condition,
                'value': value,
            }
        elif condition == CHANGED:
            result[current_key] = {
                'condition': condition,
                'old_value': value,
                'new_value': changed_value
            }
        else:
            result[current_key] = {
                'condition': condition,
                'value': value,
            }
    return result

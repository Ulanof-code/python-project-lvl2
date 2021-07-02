from gendiff.make_diff import CONDITIONS, get_condition, get_name, get_changed_value, get_value
import json
from typing import Dict


def make_json(diffs: Dict) -> str:
    """
    Formatting the difference representation to json
    :param:
        diffs: dict.
    :return:
        str.
    """
    formatted_dict: Dict = dict_formatting(diffs)
    json_output: str = json.dumps(formatted_dict, sort_keys=True, indent=4)
    if not formatted_dict:
        return '{\n}'
    return json_output


def dict_formatting(diffs: Dict) -> Dict:
    result = {}
    for diff in diffs:
        name = get_name(diffs[diff])
        condition = get_condition(diffs[diff])
        value = get_value(diffs[diff])
        changed_value = get_changed_value(diffs[diff])
        current_key = f"{name}"
        if condition == CONDITIONS['IS_DICT']:
            value = dict_formatting(value)
            result[current_key] = {
                'condition': condition,
                'value': value,
            }
        else:
            if condition == CONDITIONS['CHANGED']:
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

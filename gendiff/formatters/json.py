from gendiff.make_diff import (get_name, get_value, get_condition, CONDITIONS)
import json
from typing import List, Dict


def make_json(diffs: List[dict]) -> str:
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


def dict_formatting(diffs: List[dict],
                    parent_name=None) -> Dict:
    result = {}
    for diff in diffs:
        name = get_name(diff)
        condition = get_condition(diff)
        value = get_value(diff)
        if parent_name is None:
            current_key = str(name)
        else:
            current_key = f"{parent_name}.{name}"
        if condition == CONDITIONS['IS_DICT']:
            value = dict_formatting(value, parent_name=current_key)
            result[current_key] = {
                'condition': condition,
                'value': value,
            }
        else:
            result[current_key] = {
                'condition': condition,
                'value': value,
            }
    return result
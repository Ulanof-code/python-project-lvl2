from typing import Dict, Any

REMOVED = 'removed'
CHANGED = 'changed'
ADDED = 'added'
RELATED = 'related'
NESTED = 'nested'


def make_diffs(data1: Dict,
               data2: Dict) -> Dict:
    """
    This function generates the internal representation
    of the difference program in the source files
    Parameters:
        1. data1: dict
        2. data2 : dict
    Returns: [{...}, {...}, {...}]
        - The function will return the list of nested dictionaries.
        - Each dictionary is one difference in the source files.
        - Each dictionary has keys 'name', 'condition', 'value'.
    """
    all_keys = data1.keys() | data2.keys()
    representation = dict()
    for key in all_keys:
        node: Dict = {}
        value1 = data1.get(key)
        value2 = data2.get(key)
        if key not in data2:
            node['condition'] = REMOVED
            node['name'] = key
            node['value'] = value1
            node['changed_value'] = None
        elif key not in data1:
            node['condition'] = ADDED
            node['name'] = key
            node['value'] = value2
            node['changed_value'] = None
        elif value1 == value2:
            node['condition'] = RELATED
            node['name'] = key
            node['value'] = value1
            node['changed_value'] = None
        elif isinstance(value1, dict) and isinstance(value2, dict):
            sub_comprehension = make_diffs(value1, value2)
            node['condition'] = NESTED
            node['name'] = key
            node['value'] = sub_comprehension
            node['changed_value'] = None
        else:
            node['condition'] = CHANGED
            node['name'] = key
            node['value'] = value1
            node['changed_value'] = value2
        representation[key] = node
    return representation


def get_condition(node: Dict) -> str:
    return node['condition']


def get_value(node: Dict) -> Any:
    return node['value']


def get_changed_value(node: Dict) -> Any:
    return node['changed_value']


def get_name(node: Dict) -> str:
    return node['name']

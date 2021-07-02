from typing import Dict, Any

CONDITIONS = {
    'REMOVED': 'removed',
    'CHANGED': 'changed',
    'ADDED': 'added',
    'RELATED': 'related',
    'IS_DICT': 'is_dict'
}


def make_diffs_representation(data1: Dict,
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
    def add_item(condition: str, value: Any, changed_value: Any=None):
        """
        Add a key dictionary to "representation":
            1. 'condition': str;
            2. 'name': str
            3. 'value': any
        """
        node['condition'] = condition
        node['name'] = key
        node['value'] = value
        node['changed_value'] = changed_value

    all_keys = data1.keys() | data2.keys()
    representation: Dict = dict()
    for key in all_keys:
        node = {}
        value1 = data1.get(key)
        value2 = data2.get(key)
        if key not in data2:
            add_item(CONDITIONS['REMOVED'], value1)
        elif key not in data1:
            add_item(CONDITIONS['ADDED'], value2)
        elif value1 == value2:
            add_item(CONDITIONS['RELATED'], value1)
        elif all([
            value1 != value2,
            isinstance(value1, dict),
            isinstance(value2, dict)
        ]):

            sub_comprehension = make_diffs_representation(value1, value2)
            add_item(CONDITIONS['IS_DICT'], sub_comprehension)
        else:
            add_item(CONDITIONS['CHANGED'], value1, changed_value=value2)
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

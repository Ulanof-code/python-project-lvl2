from typing import Dict, List, Any

CONDITIONS = {
    'REMOVED': 'removed',
    'CHANGED_OLD': 'changed_old',
    'CHANGED_NEW': 'changed_new',
    'ADDED': 'added',
    'RELATED': 'related',
    'IS_DICT': 'is_dict'
}


def make_diffs_representation(data1: Dict,
                              data2: Dict) -> List[dict]:  # noqa: C901
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
    def add_item(condition: str, value: Any):
        """
        Add a key dictionary to "representation":
            1. 'condition': str;
            2. 'name': str
            3. 'value': any
        """
        representation.append({
            'condition': condition,
            'name': key,
            'value': value
        })

    all_keys: List[str] = sorted(data1.keys() | data2.keys())
    representation: List = list()
    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        if key not in data2:
            add_item(CONDITIONS['REMOVED'], value1)
        elif key not in data1:
            add_item(CONDITIONS['ADDED'], value2)
        elif value1 == value2:
            add_item(CONDITIONS['RELATED'], value1)
        elif isinstance(value1, dict) and isinstance(value2, dict):
            sub_comprehension = make_diffs_representation(value1, value2)
            add_item(CONDITIONS['IS_DICT'], sub_comprehension)
        else:
            add_item(CONDITIONS['CHANGED_OLD'], value1)
            add_item(CONDITIONS['CHANGED_NEW'], value2)
    return representation


def get_condition(node: Dict) -> str:
    return node['condition']


def get_value(node: Dict) -> Any:
    return node['value']


def get_name(node: Dict) -> str:
    return node['name']

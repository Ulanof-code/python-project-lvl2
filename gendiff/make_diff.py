CONDITIONS = {
    'REMOVED': 'removed',
    'CHANGED_OLD': 'changed_old',
    'CHANGED_NEW': 'changed_new',
    'ADDED': 'added',
    'RELATED': 'related',
    'IS_DICT': 'is_dict'
}


def get_diff(data1, data2):
    """
    Write the differences of the two dictionaries to a list with special parameters:
    1. REMOVED: str - if the key was in the first dict, but was deleted in the second one;
    2. RELATED: str - if the key remains the same;
    3. ADDED: str - the key was not in the first dict, but was added to the second one;
    4. CHANGED_OLD: str - the condition of the key in the source dictionary. If the key in both dictionaries;
    5. CHANGED_NEW: str - the state of the key in the modified dictionary. If the key in both dictionaries;
    6. IS_DICT: str - A value that is different in the source and modified dictionary, if it is a dictionary

    positional arguments:
    1. data1: dict;
    2. data2: dict.

    return: [{name: str, value: any, parameter: str}...]
    """

    def add_item(condition, value):
        """Creating an object to add to the list of differences"""
        item = dict(condition=condition, name=key, value=value)
        return item

    all_keys = sorted(data1.keys() | data2.keys())
    comprehension = []
    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        if key not in data2:  # если ключ только в первых данных
            comprehension.append(add_item(CONDITIONS['REMOVED'], value1))
        elif key not in data1:
            comprehension.append(add_item(CONDITIONS['ADDED'], value2))
        elif value1 == value2:
            comprehension.append(add_item(CONDITIONS['RELATED'], value1))
        elif isinstance(value1, dict) and isinstance(value2, dict):
            sub_comprehension = get_diff(value1, value2)
            comprehension.append(add_item(CONDITIONS['IS_DICT'], sub_comprehension))
        else:
            comprehension.append(add_item(CONDITIONS['CHANGED_OLD'], value1))
            comprehension.append(add_item(CONDITIONS['CHANGED_NEW'], value2))
    return comprehension


def get_condition(node):
    return node['condition']


def get_value(node):
    return node['value']


def get_name(node):
    return node['name']

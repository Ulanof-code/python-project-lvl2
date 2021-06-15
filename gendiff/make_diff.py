CONDITIONS = {
    'REMOVED': 'removed',
    'CHANGED_OLD': 'changed_old',
    'CHANGED_NEW': 'changed_new',
    'ADDED': 'added',
    'RELATED': 'related',
    'IS_DICT': 'is_dict'
}


def get_diff(data1, data2):  # noqa: C901
    def add_item(condition, value):
        """Creating an object to add to the list of differences"""
        diffs.append({'condition': condition, 'name': key, 'value': value})

    all_keys = sorted(data1.keys() | data2.keys())
    diffs = []
    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        if key not in data2:  # если ключ только в первых данных
            add_item(CONDITIONS['REMOVED'], value1)
        elif key not in data1:
            add_item(CONDITIONS['ADDED'], value2)
        elif value1 == value2:
            add_item(CONDITIONS['RELATED'], value1)
        elif isinstance(value1, dict) and isinstance(value2, dict):
            sub_comprehension = get_diff(value1, value2)
            add_item(CONDITIONS['IS_DICT'], sub_comprehension)
        else:
            add_item(CONDITIONS['CHANGED_OLD'], value1)
            add_item(CONDITIONS['CHANGED_NEW'], value2)
    return diffs


def get_condition(node):
    return node['condition']


def get_value(node):
    return node['value']


def get_name(node):
    return node['name']

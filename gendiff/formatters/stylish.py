TAB = '    '
PLUS = '  + '
MINUS = '  - '


def make_stylish(diff, depth=0):
    """Format dict with difference.
    Args:
        diff: dict
        depth: int
    Returns:
        Return formatting difference.
    """
    keys = sorted(diff.keys())
    format_diff = []
    for key in keys:
        if diff[key]['condition'] == 'removed':
            format_diff.append(
                f"{TAB * depth}"
                f"{MINUS}{key}: "
                f"{format_value(diff[key]['value'], depth + 1)}")
        if diff[key]['condition'] == 'added':
            format_diff.append(
                f"{TAB * depth}"
                f"{PLUS}{key}: "
                f"{format_value(diff[key]['value'], depth + 1)}")
        elif diff[key]['condition'] == 'related':
            format_diff.append(
                f"{TAB * depth}"
                f"{TAB}"
                f"{key}: {format_value(diff[key]['value'], depth + 1)}")
        elif diff[key]['condition'] == 'changed':
            format_diff.append(
                f"{TAB * depth}"
                f"{MINUS}"
                f"{key}: "
                f"{format_value(diff[key]['value'], depth + 1)}")
            format_diff.append(
                f"{TAB * depth}"
                f"{PLUS}"
                f"{key}: "
                f"{format_value(diff[key]['changed_value'], depth + 1)}")
        elif diff[key]['condition'] == 'nested':
            format_diff.append(
                f"{TAB * depth}"
                f"{TAB}"
                f"{key}: "
                f"{make_stylish(diff[key]['value'], depth + 1)}")
    return '\n'.join([
        '{',
        *format_diff,
        '{a}{b}'.format(a=TAB * depth, b='}'),
    ])


def format_value(dict_unchanged, depth):
    """Format dict without changing.
    Args:
        dict_unchanged: dict
        depth: int
    Returns:
        Return formatting dict.
    """
    objects_to_json = {'True': 'true', 'False': 'false', 'None': 'null'}
    if not isinstance(dict_unchanged, dict):
        if str(dict_unchanged) in objects_to_json.keys():
            return objects_to_json[str(dict_unchanged)]
        return str(dict_unchanged)
    list_values = []
    for key in dict_unchanged.keys():
        list_values.append(''.join([
            TAB * (depth + 1),
            str(key),
            ': ',
            str(format_value(
                dict_unchanged[key],
                depth=depth + 1,
            )),
            ]))
    return '\n'.join([
        '{',
        *list_values,
        '{a}{b}'.format(a=(TAB * depth), b='}'),
    ])

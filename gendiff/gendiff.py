from gendiff.parser import (is_json, is_yaml, json_parse, yaml_parse)


def generate_diff(file1, file2):
    if is_json(file1) and is_json(file2):
        data1 = json_parse(file1)
        data2 = json_parse(file2)
    elif is_yaml(file1) and is_yaml(file2):
        data1 = yaml_parse(file1)
        data2 = yaml_parse(file2)
    else:
        return "Error"
    result = '{\n'
    sorted_keys = sorted(set(sorted(data1) + sorted(data2)))

    for key in sorted_keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                result += '  {} {}: {} \n'.format(' ', key, data1[key])
            else:
                result += '  {} {}: {} \n'.format('-', key, data1[key])
                result += '  {} {}: {} \n'.format('+', key, data2[key])
        if key in data1 and key not in data2:
            result += '  {} {}: {} \n'.format('-', key, data1[key])
        if key in data2 and key not in data1:
            result += '  {} {}: {} \n'.format('+', key, data2[key])
    return result + '}'

import yaml
import json


def is_json(path_to_file):
    if path_to_file.endswith('.json'):
        return True
    return False


def json_parse(file):
    data = json.load(open(file))
    return data


def is_yaml(path_to_file):
    if path_to_file.endswith('.yml') or path_to_file.endswith('.yaml'):
        return True
    return False


def yaml_parse(file):
    data = yaml.safe_load(open(file))
    return data


def parse(file):
    if is_json(file):
        data = json_parse(file)
    elif is_yaml(file):
        data = yaml_parse(file)
    else:
        return "{}"
    return data

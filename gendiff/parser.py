import yaml
import json
import os


def json_parse(file):
    data = json.loads(open(file, 'r').read())
    return data


def yaml_parse(file):
    data = yaml.safe_load(open(file, 'r').read())
    return data


def get_dict_from_file(file_path):
    _, file_type = os.path.splitext(file_path)
    if file_type.lower() in ".json":
        return json_parse(file_path)
    elif file_type.lower() in (".yml", ".yaml"):
        return yaml_parse(file_path)
    raise NotImplementedError(f"The file type {file_type} is not supported")

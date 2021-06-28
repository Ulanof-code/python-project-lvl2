from gendiff.common_components import read_file
import yaml
import json
import os


def json_parse(path_to_file):
    data = json.loads(read_file(path_to_file))
    return data


def yaml_parse(path_to_file):
    data = yaml.safe_load(read_file(path_to_file))
    return data


def get_dict_from_file(path_to_file):
    _, file_type = os.path.splitext(path_to_file)
    if file_type.lower() in ".json":
        return json_parse(path_to_file)
    elif file_type.lower() in (".yml", ".yaml"):
        return yaml_parse(path_to_file)
    raise NotImplementedError(f"The file type {file_type} is not supported")

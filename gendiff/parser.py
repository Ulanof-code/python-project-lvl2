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
    extension = os.path.splitext(file_path)[-1]
    if extension == ".json":
        return json_parse(file_path)
    elif extension in (".yml", ".yaml"):
        return yaml_parse(file_path)
    raise NotImplementedError(f"Unsupported file type {extension}")

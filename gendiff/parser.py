from gendiff.common_components import read_file
import yaml
import json
import os


def get_dict_from_file(file_path):
    file = read_file(file_path)
    _, file_type = os.path.splitext(file_path)
    if file_type.lower() in ".json":
        return json.loads(file)
    elif file_type in (".yml", ".yaml"):
        return yaml.safe_load(file)
    raise NotImplementedError(f"The file type {file_type} is not supported")

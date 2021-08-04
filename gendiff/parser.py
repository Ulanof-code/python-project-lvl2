from gendiff.common_components import read_file
import yaml
import json
import os


def get_dict_from_file(file_path):
    file = read_file(file_path)
    _, file_extension = os.path.splitext(file_path)
    if file_extension.lower() in ".json":
        return json.loads(file)
    elif file_extension in (".yml", ".yaml"):
        return yaml.safe_load(file)
    raise NotImplementedError(f"The file type {file_extension} is not supported")

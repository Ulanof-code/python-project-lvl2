import json
from typing import Dict


def make_json(diffs: Dict) -> str:
    """
    Formatting the difference representation to json
    The formatter is selected in FORMATS: tuple, where [0] == 'stylish', [1] == 'plain', [2] == 'json'
    :param:
        diffs: dict.
    :return:
        str.
    """
    return json.dumps(diffs, sort_keys=True, indent=4)

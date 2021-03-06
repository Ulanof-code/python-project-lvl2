from gendiff.gendiff import generate_diff
from gendiff.read_file import read_file
import os
import pytest

path = 'tests'
file1_json = os.path.join(path, 'fixtures', 'file1.json')  # 'tests/fixtures/file1.json'
file2_json = os.path.join(path, 'fixtures', 'file2.json')  # 'tests/fixtures/file2.json'
file1_yaml = os.path.join(path, 'fixtures', 'file1.yaml')  # 'tests/fixtures/file1.yaml'
file2_yml = os.path.join(path, 'fixtures', 'file2.yml')  # 'tests/fixtures/file2.yml'

stylish_expected = read_file(os.path.join(path, 'fixtures', 'correct_stylish_output.txt'))
plain_expected = read_file(os.path.join(path, 'fixtures', 'correct_plain_output.txt'))
json_expected = read_file(os.path.join(path, 'fixtures', 'correct_json_output.txt'))

FORMATTERS = [
    'stylish',
    'plain',
    'json'
]


@pytest.mark.parametrize('fixture1, fixture2, formatter, result', [
    (file1_json, file2_json, FORMATTERS[0], stylish_expected),
    (file1_json, file2_json, FORMATTERS[1], plain_expected),
    (file1_json, file2_json, FORMATTERS[2], json_expected),
    (file1_yaml, file2_yml, FORMATTERS[0], stylish_expected),
    (file1_yaml, file2_yml, FORMATTERS[1], plain_expected),
    (file1_yaml, file2_yml, FORMATTERS[2], json_expected)
])
def test_all_cases(fixture1, fixture2, formatter, result):
    tmp = generate_diff(fixture1, fixture2, formatter)
    assert tmp == result

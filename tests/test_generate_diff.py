from gendiff.gendiff import generate_diff
from gendiff.common_components import read_file
import pytest

file1_json = 'tests/fixtures/file1.json'
file2_json = 'tests/fixtures/file2.json'
file1_yaml = 'tests/fixtures/file1.yaml'
file2_yml = 'tests/fixtures/file2.yml'


stylish_expected = read_file('tests/fixtures/correct_stylish_output.txt')
plain_expected = read_file('tests/fixtures/correct_plain_output.txt')
json_expected = read_file('tests/fixtures/correct_json_output.txt')

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
    tmp = generate_diff(fixture1,
                        fixture2,
                        formatter)
    assert tmp == result

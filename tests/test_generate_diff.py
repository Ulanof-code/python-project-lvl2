from gendiff.gendiff import generate_diff
from gendiff.parser import parse

correct = ''
with open('tests/fixtures/correct_output.txt', 'r') as file:
    correct = file.read()


def test_correct_output_json():
    tmp = generate_diff(
        parse('tests/fixtures/file1.json'),
        parse('tests/fixtures/file2.json')
    )
    assert tmp == correct


def test_correct_output_yaml():
    tmp = generate_diff(
        parse('tests/fixtures/file1.yaml'),
        parse('tests/fixtures/file2.yml')
    )
    assert tmp == correct

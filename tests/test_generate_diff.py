from gendiff.gendiff import generate_output
from gendiff.parser import parse

with open('tests/fixtures/correct_stylish_output.txt', 'r') as file:
    stylish_expected = file.read()

with open('tests/fixtures/correct_plain_output.txt', 'r') as file:
    plain_expected = file.read()


def test_empty():
    tmp = generate_output({}, {})
    assert tmp == '{\n}'


def test_stylish_json():
    tmp = generate_output(
        parse('tests/fixtures/file1.json'),
        parse('tests/fixtures/file2.json'),
        'stylish'
    )
    assert tmp == stylish_expected


def test_stylish_yaml():
    tmp = generate_output(
        parse('tests/fixtures/file1.yaml'),
        parse('tests/fixtures/file2.yml'),
        'stylish'
    )
    assert tmp == stylish_expected


def test_plain_json():
    tmp = generate_output(
        parse('tests/fixtures/file1.yaml'),
        parse('tests/fixtures/file2.yml'),
        'plain'
    )
    assert tmp == plain_expected


def test_plain_yaml():
    tmp = generate_output(
        parse('tests/fixtures/file1.yaml'),
        parse('tests/fixtures/file2.yml'),
        'plain'
    )
    assert tmp == plain_expected

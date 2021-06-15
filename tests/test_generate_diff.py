from gendiff.gendiff import generate_diff
from gendiff.parser import parse


with open('tests/fixtures/correct_output.txt', 'r') as file:
    expected = file.read()

with open('tests/fixtures/correct_complex_output.txt', 'r') as file:
    complex_expected = file.read()


def test_correct_output_json():
    tmp = generate_diff(
        parse('tests/fixtures/file1.json'),
        parse('tests/fixtures/file2.json')
    )
    assert tmp == expected


def test_correct_output_yaml():
    tmp = generate_diff(
        parse('tests/fixtures/file1.yaml'),
        parse('tests/fixtures/file2.yml')
    )
    assert tmp == expected


def test_complex_json():
    tmp = generate_diff(
        parse('tests/fixtures/complex_file1.json'),
        parse('tests/fixtures/complex_file2.json')
    )
    assert tmp == complex_expected


def test_complex_yaml():
    tmp = generate_diff(
        parse('tests/fixtures/complex_file1.yaml'),
        parse('tests/fixtures/complex_file2.yml')
    )
    assert tmp == complex_expected

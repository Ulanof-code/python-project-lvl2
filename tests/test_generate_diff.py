from gendiff.gendiff import generate_diff

with open('tests/fixtures/correct_stylish_output.txt', 'r') as file:
    stylish_expected = file.read()

with open('tests/fixtures/correct_plain_output.txt', 'r') as file:
    plain_expected = file.read()

with open('tests/fixtures/correct_json_output.txt', 'r') as file:
    json_expected = file.read()

FORMATTERS = [
    'stylish',
    'plain',
    'json'
]


def test_stylish_json():
    tmp = generate_diff('tests/fixtures/file1.json',
                        'tests/fixtures/file2.json',
                        'stylish')
    assert tmp == stylish_expected


def test_stylish_yaml():
    tmp = generate_diff('tests/fixtures/file1.yaml',
                        'tests/fixtures/file2.yml',
                        'stylish')
    assert tmp == stylish_expected


def test_plain_json():
    tmp = generate_diff('tests/fixtures/file1.yaml',
                        'tests/fixtures/file2.yml',
                        'plain')
    assert tmp == plain_expected


def test_plain_yaml():
    tmp = generate_diff('tests/fixtures/file1.yaml',
                        'tests/fixtures/file2.yml',
                        'plain')
    assert tmp == plain_expected


def test_yaml_to_json():
    tmp = generate_diff('tests/fixtures/file1.yaml',
                        'tests/fixtures/file2.yml',
                        'json')
    assert tmp == json_expected


def test_formatter_json():
    tmp = generate_diff('tests/fixtures/file1.json',
                        'tests/fixtures/file2.json',
                        'json')
    assert tmp == json_expected

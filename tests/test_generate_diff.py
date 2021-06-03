from gendiff.gendiff import generate_diff

correct = ''
with open('tests/fixtures/correct_output.txt', 'r') as file:
    correct = file.read()


def test_correct_output_json():
    tmp = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert str(tmp) == correct

def test_correct_output_yaml():
    tmp = generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yml')
    assert tmp == correct
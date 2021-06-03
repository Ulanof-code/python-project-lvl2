from gendiff.gendiff import generate_diff

correct = ''
with open('tests/fixtures/correct_output.txt', 'r') as file:
    correct = file.read()


def test_correct():
    tmp = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert str(tmp) == correct

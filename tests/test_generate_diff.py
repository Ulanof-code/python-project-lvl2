from gendiff.gendiff import generate_diff

correct = """{
  - follow: False 
    host: hexlet.io 
  - proxy: 123.234.53.22 
  - timeout: 50 
  + timeout: 20 
  + verbose: True 
}"""


def test_correct():
    tmp = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert str(tmp) == correct

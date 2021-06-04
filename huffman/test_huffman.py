from collections import Counter

from huffman import make_codes, code, decode


def test_codes():
    counter = Counter(bytearray('aabc', encoding='utf-8'))

    assert make_codes(counter) == {ord('a'): '0', ord('b'): '11', ord('c'): '10'}


def test_code_decode():
    string = bytearray('aabc', encoding='utf-8')
    codes = make_codes(Counter(string))

    length, coded = code(string, codes)

    assert length == 6

    assert decode(coded, codes, length) == string

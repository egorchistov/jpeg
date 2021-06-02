from collections import Counter

from . import codes, code, decode


def test_codes():
    c = Counter(bytearray('aabc', encoding='utf-8'))

    assert codes(c) == {ord('a'): '0', ord('b'): '11', ord('c'): '10'}


def test_code_decode():
    s = bytearray('aabc', encoding='utf-8')
    c = codes(Counter(s))

    length, coded_s = code(s, c)

    assert length == 6

    assert decode(coded_s, c, length) == s


from . import rle_code, rle_decode


def test_code_decode():
    s = bytearray('aaaabccc', encoding='utf-8')
    coded = rle_code(s)
    
    assert bytearray(rle_decode(coded)) == s


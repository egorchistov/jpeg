from . import rle_code, rle_decode, int2bytes, bytes2int


def test_code_decode():
    s = bytearray('aaaaabccc', encoding='utf-8')
    coded = rle_code(s)
    
    assert bytearray(rle_decode(coded)) == s


def test_int2bytes():
    assert int2bytes(256) == bytearray([0, 0, 1, 0])


def test_bytes2int():
    assert bytes2int([0, 0, 1, 0]) == 256


from rle import code, decode


def test_code_decode():
    bad = bytearray("abcdef", encoding="utf-8")

    assert code(bad) == bytearray(b"\x05abcdef")
    assert decode(code(bad)) == bad

    good = bytearray("aabcdef", encoding="utf-8")

    assert code(good) == bytearray(b"\x81a\x04bcdef")
    assert decode(code(good)) == good

    many = bytearray("a" * 128, encoding="utf-8")

    assert code(many) == bytearray(b"\xffa")
    assert decode(code(many)) == many

    over9999 = bytearray("a" * 256, encoding="utf-8")

    assert code(over9999) == bytearray(b"\xffa\xffa")
    assert decode(code(over9999)) == over9999

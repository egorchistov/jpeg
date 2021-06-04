import pytest

from huffman.bitbuffer import bits2byte, byte2bits, BitBuffer


def test_bits2byte():
    assert bits2byte([1, 0, 0, 0, 0, 1, 0, 0]) == 132


def test_bits2byte_incorrect_bits():
    with pytest.raises(ValueError):
        bits2byte([])

    with pytest.raises(ValueError):
        bits2byte([2, 0, 0, 0, 0, 0, 0, 0])


def test_byte2bits():
    assert byte2bits(68) == [0, 1, 0, 0, 0, 1, 0, 0]


def test_byte2bits_incorrect_byte():
    with pytest.raises(ValueError):
        byte2bits(256)

    with pytest.raises(ValueError):
        byte2bits(-1)


def test_bitbuffer():
    bbuf = BitBuffer()

    bbuf.push(1)
    assert bbuf.to_bytearray() == bytearray([128])

    bbuf.push(0)
    assert len(bbuf) == 2
    assert bbuf.pop() == 1
    assert bbuf.pop() == 0


def test_bitbuffer_incorrect():
    bbuf = BitBuffer()

    with pytest.raises(ValueError):
        bbuf.push(2)

    with pytest.raises(IndexError):
        bbuf.pop()

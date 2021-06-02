import pytest

from . import bits2byte, byte2bits, BitBuffer


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
    b = BitBuffer()

    b.push(1)
    assert b.to_bytearray() == bytearray([128])

    b.push(0)
    assert len(b) == 2
    assert b.pop() == 1
    assert b.pop() == 0


def test_bitbuffer_incorrect():
    b = BitBuffer()

    with pytest.raises(ValueError):
        b.push(2)

    with pytest.raises(IndexError):
        b.pop()


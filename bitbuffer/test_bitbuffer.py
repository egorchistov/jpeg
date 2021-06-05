import pytest

from bitbuffer import BitBuffer


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

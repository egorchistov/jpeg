import numpy as np

from zigzag import scan64, inverse64, scan, inverse


def test_zigzag64():
    block = np.arange(64).reshape(8, 8)
    assert (inverse64(scan64(block)) == block).all()


def test_zigzag():
    block = np.arange(64 * 100).reshape(100, 8, 8)
    assert (inverse(scan(block)) == block).all()

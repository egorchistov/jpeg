import numpy as np

from . import scan64, inverse64, scan, inverse

def test_zigzag64():
    x = np.arange(64).reshape(8, 8)
    assert (inverse64(scan64(x)) == x).all()


def test_zigzag():
    x = np.arange(64 * 100).reshape(100, 8, 8)
    assert (inverse(scan(x)) == x).all()


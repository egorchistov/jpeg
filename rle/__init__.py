from itertools import groupby

import numpy as np


def rle_code(istream):
    ostream = bytearray()
    for char, same in groupby(istream):
        count = sum(1 for _ in same)
        ostream.extend((count, char))

    return ostream


def rle_decode(istream):
    ostream = []
    for count, char in np.array(istream).reshape(-1, 2):
        ostream.extend([char] * count)

    return np.array(ostream)


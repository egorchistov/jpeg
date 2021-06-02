from itertools import groupby

import numpy as np


def rle_code(istream):
    ostream = bytearray()
    for char, same in groupby(istream):
        count = sum(1 for _ in same)
        ostream.extend(int2bytes(count))
        ostream.append(char)

    return ostream


def rle_decode(istream):
    ostream = []
    for count_char in np.array(istream).reshape(-1, 5):
        count = bytes2int(count_char[:4])
        char = count_char[4]
        ostream.extend([char] * count)

    return np.array(ostream)


def int2bytes(u32):
    return bytearray([
            (u32 >> 24) & 0xFF,
            (u32 >> 16) & 0xFF,
            (u32 >> 8 ) & 0xFF,
            (u32 >> 0 ) & 0xFF])


def bytes2int(b):
    return (b[0] << 24) + (b[1] << 16) + (b[2] << 8) + b[3]


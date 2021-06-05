"""This module implement zigzag scan for 8x8 blocks.

This is useful in JPEG algorithm for reordering DCT coefficients.

Examples
--------
>>> import numpy as np
>>> import zigzag
>>> coefs = np.array(128).reshape(-1, 8, 8)
>>> zigzaged = zigzag.scan(coefs)
>>> zigzag.inverse(zigzaged)
"""

import numpy as np


def scan64(block):
    """Apply zigzag scan for one 8x8 block."""

    indexes = [
            0,   1,  8, 16,  9,  2,  3, 10,
            17, 24, 32, 25, 18, 11,  4,  5,
            12, 19, 26, 33, 40, 48, 41, 34,
            27, 20, 13,  6,  7, 14, 21, 28,
            35, 42, 49, 56, 57, 50, 43, 36,
            29, 22, 15, 23, 30, 37, 44, 51,
            58, 59, 52, 45, 38, 31, 39, 46,
            53, 60, 61, 54, 47, 55, 62, 63]

    return block.flatten()[indexes]


def inverse64(block):
    """Restore one 8x8 block from zigzaged input."""

    indexes = [
             0,  1,  5,  6, 14, 15, 27, 28,
             2,  4,  7, 13, 16, 26, 29, 42,
             3,  8, 12, 17, 25, 30, 41, 43,
             9, 11, 18, 24, 31, 40, 44, 53,
            10, 19, 23, 32, 39, 45, 52, 54,
            20, 22, 33, 38, 46, 51, 55, 60,
            21, 34, 37, 47, 50, 56, 59, 61,
            35, 36, 48, 49, 57, 58, 62, 63]

    return block[indexes].reshape(8, 8)


def scan(blocks):
    """Apply zigzag scan for all blocks.

    Parameters
    ----------
    blocks : np.ndarray of shape (n, 8, 8)

    Returns
    -------
    zigzaged : np.ndarray of shape n * 8 * 8
    """

    return np.array([scan64(block) for block in blocks]).flatten()


def inverse(blocks):
    """Restore all blocks from zigzaged input.

    Parameters
    ----------
    blocks : np.ndarray of shape n * 8 * 8

    Returns
    -------
    blocks : np.ndarray of shape (n, 8, 8)
    """

    return np.array([inverse64(block) for block in blocks.reshape(-1, 64)])

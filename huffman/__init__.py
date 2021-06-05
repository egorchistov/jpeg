"""Huffman coding

This module implements huffman coding.

Example
-------
>>> from collections import Counter
>>> import huffman
>>> string = b"aabc"
>>> codes = huffman.make_codes(Counter(string))
>>> length, coded = huffman.code(string, codes)
>>> decoded = huffman.decode(coded, codes, length)
"""

from heapq import heappush, heappop, heapify

from bitbuffer import BitBuffer


class Node:
    """Non-leaf tree node."""

    def __init__(self, left, right):
        self.parent = None
        left.parent = right.parent = self

        self.left = left
        self.right = right

        self.weight = left.weight + right.weight

    def __lt__(self, other):
        return self.weight < other.weight


class Leaf:
    """Tree leaf."""

    def __init__(self, symbol, weight):
        self.parent = None
        self.symbol = symbol
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    @property
    def code(self):
        """Make huffman code for current symbol."""

        huffman_code = ""
        cur = self
        while cur.parent is not None:
            codebit = "0" if cur is cur.parent.left else "1"
            huffman_code = codebit + huffman_code
            cur = cur.parent

        return huffman_code


def preorder(root):
    """Return all leaves from tree using preorder."""

    if isinstance(root, Leaf):
        return [root]

    return preorder(root.left) + preorder(root.right)


def make_codes(symbolweights):
    """Make huffman codes.

    Parameters
    ----------
    symbolweights : collections.Counter

    Returns
    -------
    codes : dict[str, str]
    """

    leaves = [Leaf(symbol, weight) for symbol, weight in symbolweights.items()]

    heapify(leaves)

    while len(leaves) >= 2:
        heappush(leaves, Node(heappop(leaves), heappop(leaves)))

    root = heappop(leaves)
    leaves = preorder(root)

    return {l.symbol: l.code for l in leaves}


def code(string, codes):
    """Code string using huffman coding."""

    bbuf = BitBuffer()
    length = 0

    for char in string:
        for bit in codes[char]:
            bbuf.push(int(bit))
            length += 1

    return length, bbuf.to_bytearray()


def decode(ibytes, codes, length):
    """Decode string using huffman coding."""

    inverse_codes = {v: k for k, v in codes.items()}
    bbuf = BitBuffer(ibytes)

    string = bytearray()

    while length:
        char_code = str(bbuf.pop())
        while not char_code in inverse_codes.keys():
            char_code += str(bbuf.pop())
        length -= len(char_code)
        char = inverse_codes[char_code]

        string.append(char)

    return string

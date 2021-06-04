from heapq import heappush, heappop, heapify

from huffman.bitbuffer import BitBuffer


class Node:
    def __init__(self, left, right):
        self.parent = None
        left.parent = right.parent = self

        self.left = left
        self.right = right

        self.weight = left.weight + right.weight

    def __lt__(self, other):
        return self.weight < other.weight


class Leaf(Node):
    def __init__(self, symbol, weight):
        self.parent = None
        self.symbol = symbol
        self.weight = weight

    @property
    def code(self):
        code = ""
        cur = self
        while cur.parent is not None:
            codebit = "0" if cur is cur.parent.left else "1"
            code = codebit + code
            cur = cur.parent

        return code


def preorder(root):
    if isinstance(root, Leaf):
        return [root]

    return preorder(root.left) + preorder(root.right)


def make_codes(symbolweights):
    leaves = [Leaf(symbol, weight) for symbol, weight in symbolweights.items()]

    heapify(leaves)

    while len(leaves) >= 2:
        heappush(leaves, Node(heappop(leaves), heappop(leaves)))

    root = heappop(leaves)
    leaves = preorder(root)

    return {l.symbol: l.code for l in leaves}


def code(string, codes):
    bbuf = BitBuffer()
    length = 0

    for char in string:
        for bit in codes[char]:
            bbuf.push(int(bit))
            length += 1

    return length, bbuf.to_bytearray()


def decode(bytes_, codes, length):
    inverse_codes = {v: k for k, v in codes.items()}
    bbuf = BitBuffer(bytes_)

    string = bytearray()

    while length:
        code = str(bbuf.pop())
        length -= 1
        while not code in inverse_codes.keys():
            code += str(bbuf.pop())
            length -= 1
        char = inverse_codes[code]

        string.append(char)

    return string

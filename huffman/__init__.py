from heapq import heappush, heappop, heapify

from .bitbuffer import BitBuffer


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
        n = self
        while n.parent is not None:
            codebit = "0" if n is n.parent.left else "1"
            code = codebit + code
            n = n.parent

        return code


def preorder(root):
    if type(root) == Leaf:
        return [root]

    return preorder(root.left) + preorder(root.right)


def codes(symbolweights):
    leaves = [Leaf(symbol, weight) for symbol, weight in symbolweights.items()]

    heapify(leaves)

    while len(leaves) >= 2:
        heappush(leaves, Node(heappop(leaves), heappop(leaves)))

    root = heappop(leaves)
    leaves = preorder(root)

    return {l.symbol: l.code for l in leaves}


def code(s, codes):
    b = BitBuffer()
    length = 0

    for c in s:
        for bit in codes[c]:
            b.push(int(bit))
            length += 1
    
    return length, b.to_bytearray()


def decode(b, codes, length):
    inverse_codes = {v: k for k, v in codes.items()}
    b = BitBuffer(b)
    
    s = bytearray()
    
    while length:
        code = str(b.pop())
        length -= 1
        while not code in inverse_codes.keys():
            code += str(b.pop())
            length -= 1
        c = inverse_codes[code]
        
        s.append(c)
    
    return s


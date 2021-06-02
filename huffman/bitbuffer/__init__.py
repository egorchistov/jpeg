def bits2byte(bits):
    if len(bits) != 8 or any(bit not in (0, 1) for bit in bits):
        raise ValueError

    byte = 0
    for bit in bits:
        byte <<= 1
        byte |= bit

    return byte


def byte2bits(byte):
    if not 0 <= byte <= 255:
        raise ValueError

    bits = [0] * 8
    for i in range(8):
        bits[i] = (byte & (1 << (7 - i))) >> (7 - i)
    
    return bits


class BitBuffer:
    """Class that provides storing and and reading bits in continuous
    bytearray.

    Parameters
    ----------
    buffer : bytearray, optional (default=None)
        Input bytearray, for initialization.

    Examples
    --------
    >>> b = BitBuffer()
    >>> b.push(0)
    >>> b.push(1)
    >>> b.pop()
    0
    >>> b.pop()
    1

    """

    def __init__(self, bytes=bytearray()):
        self.bits = bytearray()
        while len(bytes):
            self.bits.extend(byte2bits(bytes.pop(0)))

    def __len__(self):
        return len(self.bits)

    def to_bytearray(self):
        """Convert to bytearray.

        Returns
        -------
        buffer: bytearray
            Bytearray that contains all data.

        """
        
        bytes = bytearray()
        
        full = len(self.bits) // 8 * 8
        
        for i in range(0, full, 8):
            bits = self.bits[i : i + 8]
            bytes.append(bits2byte(bits))
        
        remains = 8 - len(self.bits) % 8
        bits = list(self.bits[full :]) + [0] * remains
        bytes.append(bits2byte(bits))
        
        return bytes

    def push(self, bit):
        """Push given bit to buffer.

        Parameters
        ----------
        bit: int
            Input bit.
        """
       
        if bit not in (0, 1):
            raise ValueError

        self.bits.append(bit)

    def pop(self):
        """Pop one bit from buffer.

        Returns
        -------
        bit: int
            Popped bit.

        """

        return self.bits.pop(0)


"""BitBuffer

Provides class to work with bits.
"""

import numpy as np


class BitBuffer:
    """Class that provides storing and and reading bits in continuous
    bytearray.

    Parameters
    ----------
    bytes_ : bytearray, optional (default=bytearray())
        Input bytearray, for initialization.

    Examples
    --------
    >>> bbuf = BitBuffer()
    >>> bbuf.push(0)
    >>> bbuf.push(1)
    >>> bbuf.to_bytearray()
    b'@'
    >>> len(bbuf)
    2
    >>> bbuf.pop()
    0
    >>> bbuf.pop()
    1
    """

    def __init__(self, bytes_=bytearray()):
        self.bits = bytearray(np.unpackbits(bytes_))

    def __len__(self):
        """Get bits count in array.
        """

        return len(self.bits)

    def to_bytearray(self):
        """Convert to bytearray. The result is padded to full bytes
        by inserting zero bits at the end.

        Returns
        -------
        buffer: bytearray
            Bytearray that contains all data.

        """

        return bytearray(np.packbits(self.bits))

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

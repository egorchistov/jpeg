"""Run-length encoding

Bytes are stored like this:


   Count unique bytes

  ┌─────────────┐   ┌─────────────┐     ┌─────────────┐
  │0   count - 1│   │     'a'     │ ... │     'z'     │
  └─────────────┘   └─────────────┘     └─────────────┘


   Count identical bytes

  ┌─────────────┐   ┌─────────────┐
  │1   count - 1│   │     'a'     │
  └─────────────┘   └─────────────┘


High bit is 0 for unique byte sequence and 1 for identical byte sequence.

The lower bits store count - 1 times to do nothing or to repeat next byte.

The combination of these two options forms the encoding.

Examples
--------
>>> import rle
>>> rle.decode(rle.code(b'aaaabccc'))
"""

import itertools


def code(ibytes):
    """Apply run-length encoding to ibytes."""

    def flush_uniques():
        nonlocal uniques, obytes

        while uniques:
            count = len(uniques[:128])

            obytes.append(0x00 + count - 1)
            obytes.extend(uniques[:128])
            del uniques[:128]

    obytes = bytearray()
    uniques = bytearray()

    for byte, same in itertools.groupby(ibytes):
        count = sum(1 for _ in same)

        if count == 1:
            uniques.append(byte)
        else:
            flush_uniques()

            while count:
                portion = min(count, 128)

                obytes.append(0x80 + portion - 1)
                obytes.append(byte)
                count -= portion

    flush_uniques()

    return obytes


def decode(ibytes):
    """Decode ibytes from run-length-encoding."""

    obytes = bytearray()

    while ibytes:
        byte = ibytes.pop(0)
        count = (byte & 0x7F) + 1

        if byte & 0x80:
            byte = ibytes.pop(0)
            obytes.extend([byte] * count)
        else:
            obytes.extend(ibytes[:count])
            del ibytes[:count]

    return obytes

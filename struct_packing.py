#!/usr/bin/env python

import struct

print 'This is a demonstration of struct packing in Python'

"""
struct.pack(<format_string>, var1, var2, ...)

Format characters:
Format      C type          Size
    c       char            1
    b       signed char     1
    B       unsigned char   1
"""

s = struct.pack("bB", -1, 1)
print s
print s.encode('hex')

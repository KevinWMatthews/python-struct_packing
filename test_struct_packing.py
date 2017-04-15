import struct

def pack_one_variable():
    return struct.pack("b", -1)

def pack_two_variables():
    return struct.pack("bB", -1, 1)

def pack_ascii_variable():
    return struct.pack("bB", -1, 0x42)

def pack_two_byte_variables_big_endian():
    return struct.pack(">hH", -1, 1)

def test_pack_one_variable():
    assert pack_one_variable() == '\xff'

def test_pack_two_variables():
    assert pack_two_variables() == '\xff\x01'

def test_pack_ascii_variable():
    # Without encoding, the function returns: \xffB
    assert pack_ascii_variable().encode('hex') == 'ff42'

def test_pack_two_byte_variables_big_endian():
    # Endian-ness comes into play: 1 can be represented as 0001 or 0100.
    assert pack_two_byte_variables_big_endian().encode('hex') == 'ffff0001'

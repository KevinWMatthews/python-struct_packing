import struct

def pack_one_variable():
    return struct.pack("b", -1)

def pack_two_variables():
    return struct.pack("bB", -1, 1)

def test_pack_one_variable():
    assert pack_one_variable() == '\xff'

def test_pack_two_variables():
    assert pack_two_variables() == '\xff\x01'

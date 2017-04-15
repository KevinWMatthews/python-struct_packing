import struct

def pack_one_variable():
    return struct.pack("b", -1)

def test_pack_one_variable():
    assert pack_one_variable() == '\xff'

import math


def repeat_extend_string(byte_string, length):
    """Takes in a byte string and a length. Extends the byte string to the length by repeating the input until length
    is reached"""
    return (byte_string * math.ceil(length / len(byte_string)))[:length]



def fixed_size(byte_string_1, byte_string_2):
    """Take in two byte strings. Outputs the byte string representing the XOR of the inputs"""
    return bytes([(a ^ b) for (a, b) in zip(byte_string_1, byte_string_2)])
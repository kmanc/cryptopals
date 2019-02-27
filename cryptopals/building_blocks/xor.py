from cryptopals.building_blocks import generate


def fixed_size(byte_string_1, byte_string_2):
    """Take in two byte strings. Outputs the byte string representing the XOR of the inputs"""
    return bytes([(a ^ b) for (a, b) in zip(byte_string_1, byte_string_2)])


def repeat_key(byte_string, key):
    """Take in two byte strings; an input and a key. Outputs a byte string representing the key XORed with
    the input repeated until the input is exhausted"""
    full_key = generate.repeat_extend_string(key, len(byte_string))

    return fixed_size(byte_string, full_key)


from cryptopals import xor, convert


def hex_to_base64(input_hex):
    """https://cryptopals.com/sets/1/challenges/1"""

    input_bytes = convert.hex_to_bytes(input_hex)
    bytes_result = convert.bytes_to_base64(input_bytes)
    output = convert.bytes_to_ascii(bytes_result)

    return output


def fixed_size_hex_xor(input_string_1, input_string_2):
    """https://cryptopals.com/sets/1/challenges/2"""

    string_1_as_bytes = convert.hex_to_bytes(input_string_1)
    string_2_as_bytes = convert.hex_to_bytes(input_string_2)
    xor_result = xor.fixed_size(string_1_as_bytes, string_2_as_bytes)
    output = convert.bytes_to_hex(xor_result)

    return output


def break_repeat_hex_char_xor(input_string):
    """https://cryptopals.com/sets/1/challenges/3"""

    input_bytes = convert.hex_to_bytes(input_string)
    break_result = xor.break_single_byte(input_bytes)
    output = convert.bytes_to_ascii(break_result)

    return output

from cryptopals import xor, convert, generate


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


def find_and_break_repeat_hex_char_xor(input_lines):
    """https://cryptopals.com/sets/1/challenges/4"""

    best = tuple((0, bytes()))
    for line in input_lines:
        input_bytes = convert.hex_to_bytes(line)
        break_result = xor.break_single_byte(input_bytes)
        break_score = generate.english_score(break_result)
        if break_score > best[0]:
            best = (break_score, break_result)
    output = convert.bytes_to_ascii(best[1])

    return output


def repeat_key_xor(input_string):
    """https://cryptopals.com/sets/1/challenges/5"""

    input_bytes = convert.ascii_to_bytes(input_string)
    key = "ICE"
    key_bytes = convert.ascii_to_bytes(key)
    xor_result = xor.repeat_key(input_bytes, key_bytes)
    output = convert.bytes_to_hex(xor_result)

    return output


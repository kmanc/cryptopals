import math


def resize_bytes(input_bytes, length):
    multiplier = math.ceil(length / len(input_bytes))
    raw_output = input_bytes * multiplier

    return raw_output[:length]


def xor_keyed(input_bytes_1, input_bytes_2):
    input_length = len(input_bytes_1)
    extended_input_2 = resize_bytes(input_bytes_2, input_length)

    return xor_same_length(input_bytes_1, extended_input_2)


def xor_same_length(input_bytes_1, input_bytes_2):
    list_of_chars = [(a ^ b) for (a, b) in zip(input_bytes_1, input_bytes_2)]

    return bytes(list_of_chars)

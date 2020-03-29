import math


def hex_to_bytes(input_hex):
    return bytes.fromhex(input_hex)


def bytes_to_hex(input_bytes):
    return input_bytes.hex()


def resize_bytes(input_bytes, length):
    multiplier = math.ceil(length / len(input_bytes))
    raw_output = input_bytes * multiplier

    return raw_output[:length]



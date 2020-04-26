import math


def resize_bytes(input_bytes: bytes, length: int):
    """Takes in a byte string and an integer. Outputs the byte string repeated till it is of length integer"""
    multiplier = math.ceil(length / len(input_bytes))
    raw_output = input_bytes * multiplier

    return raw_output[:length]


def xor_keyed(plaintext_bytes: bytes, key_bytes: bytes):
    """Takes in a plaintext and a key as bytes. Encrypts the plaintext with the key using repeated-key xor"""
    input_length = len(plaintext_bytes)
    extended_key = resize_bytes(key_bytes, input_length)

    return xor_same_length(plaintext_bytes, extended_key)


def xor_same_length(input_bytes_1: bytes, input_bytes_2: bytes):
    """Takes in a two byte strings. Outputs the xor of those two strings"""
    list_of_chars = [(a ^ b) for (a, b) in zip(input_bytes_1, input_bytes_2)]

    return bytes(list_of_chars)

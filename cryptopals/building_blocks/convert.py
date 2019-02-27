import base64


def ascii_to_bytes(input_1):
    """Takes in an ascii string. Outputs a byte string"""
    return str.encode(input_1)


def ascii_to_hex(input_1):
    """Takes in an ascii string. Outputs a hex string"""
    return str.encode(input_1).hex()


def bytes_to_ascii(input_1):
    """Takes in a byte string. Outputs an ascii string"""
    return bytes.decode(input_1)


def bytes_to_base64(input_1):
    """Takes in a byte string. Outputs a base64 encoded byte string"""
    return base64.b64encode(input_1)


def bytes_to_hex(input_1):
    """Takes in a byte string. Outputs a hex string"""
    return input_1.hex()


def hex_to_ascii(input_1):
    """Takes in a hex encoded string. Outputs an ascii string"""
    return bytes.decode(bytes.fromhex(input_1))


def hex_to_bytes(input_1):
    """Takes in a hex encoded string. Outputs a byte string"""
    return bytes.fromhex(input_1)

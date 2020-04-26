def bytes_to_hex(input_bytes: bytes):
    """Takes in a byte string. Outputs that string as hex"""
    return input_bytes.hex()


def hex_to_bytes(input_hex: str):
    """Takes in a hex string. Outputs that string as bytes"""
    return bytes.fromhex(input_hex)

from cryptopals.building_blocks import convert
from cryptopals.building_blocks import encrypt
from cryptopals.building_blocks import generate
from cryptopals.building_blocks import pad
from cryptopals.building_blocks import xor


def hex_to_base64(input_hex):
    """Converts hex to base64"""

    input_bytes = convert.hex_to_bytes(input_hex)
    output = convert.bytes_to_base64(input_bytes)

    return output

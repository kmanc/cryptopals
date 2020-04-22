from cryptopals.building_blocks.input_output import bytes_to_hex, hex_to_bytes
from cryptopals.building_blocks.xor import xor_same_length


challenge_input_1 = "1c0111001f010100061a024b53535009181c"
challenge_input_2 = "686974207468652062756c6c277320657965"


def complete_challenge(challenge_input_1, challenge_input_2):
    bytes_input_1 = hex_to_bytes(challenge_input_1)
    bytes_input_2 = hex_to_bytes(challenge_input_2)
    xored_bytes = xor_same_length(bytes_input_1, bytes_input_2)

    return bytes_to_hex(xored_bytes)


print(complete_challenge(challenge_input_1, challenge_input_2))

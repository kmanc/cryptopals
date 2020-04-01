import input_output
import xor


challenge_input_1 = "1c0111001f010100061a024b53535009181c"
challenge_input_2 = "686974207468652062756c6c277320657965"


def complete_challenge(challenge_input_1, challenge_input_2):
    bytes_input_1 = input_output.hex_to_bytes(challenge_input_1)
    bytes_input_2 = input_output.hex_to_bytes(challenge_input_2)
    xored_byte_list = xor.fixed_length(bytes_input_1, bytes_input_2)
    xored_bytes = bytes(xored_byte_list)
    return input_output.bytes_to_hex(xored_bytes)


print(complete_challenge(challenge_input_1, challenge_input_2))

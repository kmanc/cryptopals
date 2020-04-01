import input_output
import xor


def complete_challenge(challenge_input_1, challenge_input_2):
    bytes_input_1 = input_output.hex_to_bytes(challenge_input_1)
    bytes_input_2 = input_output.hex_to_bytes(challenge_input_2)
    xored_byte_list = _xor.fixed_length(bytes_input_1, bytes_input_2)
    xored_bytes = bytes(xored_byte_list)
    return input_output.bytes_to_hex(xored_bytes)

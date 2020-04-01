import input_output
import base64


def complete_challenge(challenge_input):
    bytes_input = input_output.hex_to_bytes(challenge_input)
    return base64.base64_encode(bytes_input)

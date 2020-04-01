import input_output
import base64

challenge_input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"


def complete_challenge(challenge_input):
    bytes_input = input_output.hex_to_bytes(challenge_input)
    return base64.base64_encode(bytes_input)


print(complete_challenge(challenge_input))

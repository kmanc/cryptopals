import logging
from cryptopals.building_blocks import base64
from cryptopals.building_blocks.input_output import hex_to_bytes


logger = logging.getLogger(__file__)
logger.info('my logging message')

challenge_input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"


def complete_challenge(challenge_input):
    bytes_input = hex_to_bytes(challenge_input)

    return base64.base64_encode(bytes_input)


print(complete_challenge(challenge_input))

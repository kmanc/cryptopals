from cryptopals.building_blocks.input_output import bytes_to_hex
from cryptopals.building_blocks.xor import xor_keyed

challenge_input_1 = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
challenge_input_2 = b"ICE"


def complete_challenge(challenge_input_1, challenge_input_2):
	xor_result = xor_keyed(challenge_input_1, challenge_input_2)

	return bytes_to_hex(xor_result)


print(complete_challenge(challenge_input_1, challenge_input_2))

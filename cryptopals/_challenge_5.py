import input_output
import xor

challenge_input_1 = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
challenge_input_2 = b"ICE"


def complete_challenge(challenge_input_1, challenge_input_2):
	input_length = len(challenge_input_1)
	extended_input_2 = input_output.resize_bytes(challenge_input_2, input_length)
	xor_result = xor.fixed_length(challenge_input_1, extended_input_2)
	hex_output = input_output.bytes_to_hex(xor_result)
	return hex_output


print(complete_challenge(challenge_input_1, challenge_input_2))

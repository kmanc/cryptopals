from cryptopals.attacks.xor import xor_break_byte_ciphertext
from cryptopals.building_blocks.input_output import hex_to_bytes


challenge_input = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"


def complete_challenge(challenge_input):
	input_bytes = hex_to_bytes(challenge_input)

	return xor_break_byte_ciphertext(input_bytes)


print(complete_challenge(challenge_input))

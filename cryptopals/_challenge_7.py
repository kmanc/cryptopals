import os
from cryptopals.building_blocks.aes import decrypt_ecb
from cryptopals.building_blocks.base64 import base64_decode


dir_path = os.path.dirname(os.path.realpath(__file__))
challenge_input = f"{dir_path}/_challenge_7_input.txt"


def complete_challenge(challenge_input):
	with open(challenge_input) as f:
		input_base64 = f.read().replace("\n", "")
	input_base64_bytes = input_base64.encode('utf-8')
	input_bytes = base64_decode(input_base64_bytes)
	test = decrypt_ecb(input_bytes, b"YELLOW SUBMARINE")

	return test


print(complete_challenge(challenge_input))

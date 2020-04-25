import os
from cryptopals.attacks.aes import detect_ecb
from cryptopals.building_blocks.input_output import hex_to_bytes

dir_path = os.path.dirname(os.path.realpath(__file__))
challenge_input = f"{dir_path}/_challenge_8_input.txt"


def complete_challenge(challenge_input):
	with open(challenge_input) as f:
		input_hex_list = f.readlines()
	for line in input_hex_list:
		input_bytes = hex_to_bytes(line.strip())
		if detect_ecb(input_bytes):
			return line


print(complete_challenge(challenge_input))

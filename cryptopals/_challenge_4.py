import os
from cryptopals.attacks.xor import xor_break_byte_ciphertext
from cryptopals.building_blocks.input_output import hex_to_bytes


dir_path = os.path.dirname(os.path.realpath(__file__))
challenge_input = f"{dir_path}/_challenge_4_input.txt"


def complete_challenge(challenge_input):
	best_so_far = {
		"key": bytes(),
		"score": 0,
		"result": bytes()
	}

	with open(challenge_input) as f:
		file = f.readlines()
		for line in file:
			input_line = line.strip()
			input_bytes = hex_to_bytes(input_line)
			candidate = xor_break_byte_ciphertext(input_bytes)
			if candidate["score"] > best_so_far["score"]:
				best_so_far = candidate

	return best_so_far


print(complete_challenge(challenge_input))

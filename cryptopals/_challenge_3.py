import input_output
import statistics
import xor


challenge_input = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"


def complete_challenge(challenge_input):
	bytes_input = input_output.hex_to_bytes(challenge_input)
	input_length = len(bytes_input)
	best_so_far = {
					"key": bytes(),
					"score": 0,
					"result": bytes()
	}

	for possible_key in range(0, 255):
		character = bytes([possible_key])
		key_extended = input_output.resize_bytes(character, input_length)
		xor_result = xor.fixed_length(bytes_input, key_extended)
		score = statistics.english_score(xor_result)
		if score > best_so_far["score"]:
			best_so_far = {
							"key": character,
							"score": score,
							"result": xor_result
			}

	return best_so_far


print(complete_challenge(challenge_input))

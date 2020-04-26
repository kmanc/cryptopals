from itertools import chain, zip_longest
from cryptopals.building_blocks.statistics import english_score, hamming_distance
from cryptopals.building_blocks.xor import xor_same_length, resize_bytes


def xor_break_byte_ciphertext(input_bytes: bytes):
	"""Takes in a byte string. Decrypts the string as though it is xored with a single byte"""
	input_length = len(input_bytes)
	best_so_far = {
		"key": bytes(),
		"score": 0,
		"result": bytes()
	}

	for possible_key in range(0, 255):
		character = bytes([possible_key])
		key_extended = resize_bytes(character, input_length)
		xor_result = xor_same_length(input_bytes, key_extended)
		score = english_score(xor_result)
		if score > best_so_far["score"]:
			best_so_far = {
				"key": character,
				"score": score,
				"result": xor_result
			}

	return best_so_far


def xor_break_key_length(input_bytes: bytes):
	"""Takes in a byte string. Attempts to find the length of the key used for a repeated-key xor"""
	distance_key_dict = {}
	max_key_tested = min(40, int(len(input_bytes) / 16))
	for key_size in range(3, max_key_tested):
		chunk_1 = input_bytes[0: 8 * key_size]
		chunk_2 = input_bytes[8 * key_size: 16 * key_size]
		chunk_3 = input_bytes[-8 * key_size:]
		chunk_4 = input_bytes[-16 * key_size: -8 * key_size]
		distance_1 = hamming_distance(chunk_1, chunk_2)
		distance_2 = hamming_distance(chunk_3, chunk_4)
		avg_distance = (distance_1 + distance_2) / 2
		distance_key_dict[key_size] = avg_distance / key_size
	best_keys = list({k: v for k, v in sorted(distance_key_dict.items(), key=lambda item: item[1])}.keys())
	best_candidate = best_keys[0]
	second_best = best_keys[1]
	third_best = best_keys[2]

	return {"first": best_candidate, "second": second_best, "third": third_best}


def xor_break_keyed_ciphertext(input_bytes: bytes):
	"""Takes in a byte string. Attempts to decrypt the string as though it is xored with a key"""
	best_plaintexts = dict()
	best_keys = dict()
	key_len_guesses = xor_break_key_length(input_bytes)
	for key_len in key_len_guesses.values():
		plaintext_chunks = list()
		key_candidate = b""
		for index in range(key_len):
			chunk = input_bytes[index::key_len]
			key_char, broken_chunk = xor_break_byte_ciphertext(chunk)['key'], xor_break_byte_ciphertext(chunk)['result']
			plaintext_chunks.append(broken_chunk)
			key_candidate += key_char
		plaintext = list(chain.from_iterable(zip_longest(*plaintext_chunks)))
		plaintext = bytes([a for a in plaintext if a is not None])
		plaintext_score = english_score(plaintext)
		best_plaintexts[plaintext_score] = plaintext
		best_keys[plaintext_score] = key_candidate

	highest_score = max(list(best_plaintexts.keys()))

	return {"key": best_keys[highest_score], "result": best_plaintexts[highest_score]}

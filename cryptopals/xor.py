from cryptopals import generate
from itertools import chain, zip_longest


def fixed_size(byte_string_1, byte_string_2):
    """Take in two byte strings. Outputs the byte string representing the XOR of the inputs"""
    return bytes([(a ^ b) for (a, b) in zip(byte_string_1, byte_string_2)])


def repeat_key(byte_string, key):
    """Take in two byte strings; an input and a key. Outputs a byte string representing the key XORed with
    the input repeated until the input is exhausted"""
    full_key = generate.repeat_extend_string(key, len(byte_string))

    return fixed_size(byte_string, full_key)


def break_single_byte(byte_string):
    """Takes in a string of bytes representing a single-character XOR-encrypted ciphertext. Outputs the plaintext for
    that ciphertext"""
    best = tuple((bytes(), 0))
    for char in range(0, 255):
        candidate = repeat_key(byte_string, bytes([char]))
        scored = generate.english_score(candidate)
        if scored > best[1]:
            best = (candidate, scored)

    return best[0]


def determine_key_length(byte_string):
    """Takes in a byte string representing a keyed XOR-encrypted ciphertext. Outputs the length of the key
    used to make the ciphertext based on hamming distance"""
    distance_key_list = list()
    for key_size in range(3, 40):
        chunk_1 = byte_string[0: 8 * key_size]
        chunk_2 = byte_string[8 * key_size: 16 * key_size]
        distance = generate.hamming_distance(chunk_1, chunk_2)
        distance_key_list.append((key_size, distance / key_size))
    sorted_by_score = sorted(distance_key_list, key=lambda tup: tup[1])
    best_candidate = sorted_by_score[0][0]
    second_best = sorted_by_score[1][0]
    third_best = sorted_by_score[2][0]

    return [best_candidate, second_best, third_best]


def break_repeat_key(byte_string):
    """Takes in a byte string representing a keyed XOR-encrypted ciphertext. Outputs the plaintext for that
    ciphertext"""
    key_len_guesses = determine_key_length(byte_string)
    best_plaintexts_list = list()
    for key_len in key_len_guesses:
        plaintext_chunks = list()
        for index in range(key_len):
            chunk = byte_string[index::key_len]
            broken_chunk = break_single_byte(chunk)
            plaintext_chunks.append(broken_chunk)
        plaintext = list(chain.from_iterable(zip_longest(*plaintext_chunks)))
        plaintext = bytes([a for a in plaintext if a is not None])
        plaintext_score = generate.english_score(plaintext)
        best_plaintexts_list.append((plaintext, plaintext_score))
    sorted_by_score = sorted(best_plaintexts_list, key=lambda tup: tup[1], reverse=True)

    return sorted_by_score[0][0]

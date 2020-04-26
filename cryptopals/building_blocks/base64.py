alphabet = {
	0: b'A',
	1: b'B',
	2: b'C',
	3: b'D',
	4: b'E',
	5: b'F',
	6: b'G',
	7: b'H',
	8: b'I',
	9: b'J',
	10: b'K',
	11: b'L',
	12: b'M',
	13: b'N',
	14: b'O',
	15: b'P',
	16: b'Q',
	17: b'R',
	18: b'S',
	19: b'T',
	20: b'U',
	21: b'V',
	22: b'W',
	23: b'X',
	24: b'Y',
	25: b'Z',
	26: b'a',
	27: b'b',
	28: b'c',
	29: b'd',
	30: b'e',
	31: b'f',
	32: b'g',
	33: b'h',
	34: b'i',
	35: b'j',
	36: b'k',
	37: b'l',
	38: b'm',
	39: b'n',
	40: b'o',
	41: b'p',
	42: b'q',
	43: b'r',
	44: b's',
	45: b't',
	46: b'u',
	47: b'v',
	48: b'w',
	49: b'x',
	50: b'y',
	51: b'z',
	52: b'0',
	53: b'1',
	54: b'2',
	55: b'3',
	56: b'4',
	57: b'5',
	58: b'6',
	59: b'7',
	60: b'8',
	61: b'9',
	62: b'+',
	63: b'/'
}

reverse_alphabet = {
	b'A': 0,
	b'B': 1,
	b'C': 2,
	b'D': 3,
	b'E': 4,
	b'F': 5,
	b'G': 6,
	b'H': 7,
	b'I': 8,
	b'J': 9,
	b'K': 10,
	b'L': 11,
	b'M': 12,
	b'N': 13,
	b'O': 14,
	b'P': 15,
	b'Q': 16,
	b'R': 17,
	b'S': 18,
	b'T': 19,
	b'U': 20,
	b'V': 21,
	b'W': 22,
	b'X': 23,
	b'Y': 24,
	b'Z': 25,
	b'a': 26,
	b'b': 27,
	b'c': 28,
	b'd': 29,
	b'e': 30,
	b'f': 31,
	b'g': 32,
	b'h': 33,
	b'i': 34,
	b'j': 35,
	b'k': 36,
	b'l': 37,
	b'm': 38,
	b'n': 39,
	b'o': 40,
	b'p': 41,
	b'q': 42,
	b'r': 43,
	b's': 44,
	b't': 45,
	b'u': 46,
	b'v': 47,
	b'w': 48,
	b'x': 49,
	b'y': 50,
	b'z': 51,
	b'0': 52,
	b'1': 53,
	b'2': 54,
	b'3': 55,
	b'4': 56,
	b'5': 57,
	b'6': 58,
	b'7': 59,
	b'8': 60,
	b'9': 61,
	b'+': 62,
	b'/': 63
}


def base64_decode(input_bytes: bytes):
	"""Takes in a byte string. Decodes the string as though it was base64 encoded"""
	binary_representation = ''
	unpadded_input = input_bytes.replace(b"=", b"")

	for char in unpadded_input:
		mapped = reverse_alphabet[bytes([char])]
		char_as_binary_string = bin(mapped)[2:]
		padded_to_six = char_as_binary_string.rjust(6, '0')
		binary_representation += padded_to_six

	new_chars = [int(binary_representation[index: index + 8], 2) for index in range(0, len(binary_representation), 8)]

	if new_chars[-1] == 0:
		new_chars = new_chars[:-1]

	return bytes(new_chars)


def base64_encode(input_bytes: bytes):
	"""Takes in a byte string. Encodes the string as base64"""
	binary_representation = ''
	output = b''

	for char in input_bytes:
		char_as_binary_string = bin(char)[2:]
		padded_to_eight = char_as_binary_string.rjust(8, '0')
		binary_representation += padded_to_eight
	new_chars_binary = [binary_representation[index: index + 6] for index in range(0, len(binary_representation), 6)]
	last_char = new_chars_binary[-1]

	if len(last_char) % 6 != 0:
		new_chars_binary[-1] = last_char.ljust(6, '0')

	for char in new_chars_binary:
		char_as_decimal = int(char, 2)
		output_char = alphabet[char_as_decimal]
		output += output_char

	if len(input_bytes) % 3 == 2:
		output += b'='

	if len(input_bytes) % 3 == 1:
		output += b'=='

	return output

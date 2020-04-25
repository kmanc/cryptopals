from cryptopals.building_blocks import aes


class AES:

	@staticmethod
	def test_decrypt_ecb():
		test_in_1 = b"\xc52*\x12ECG6\xc7\xb9\x8d7d\x15\xda\x97E`\x19}\xec'1\x1dE\x936\xf1\xc1&B\xea"
		test_in_2 = b"Sixteen byte key"
		test_correct_1 = b"This was the plaintext\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10"
		my_output_1 = aes.decrypt_ecb(test_in_1, test_in_2)

		assert my_output_1 == test_correct_1

		test_in_3 = b"\xdeE&f\x03&\x1dqw\x04\x91W\x13)M\xb0"
		test_in_4 = b"Sixteen byte key"
		test_correct_2 = b"Sixteen byte in."
		my_output_2 = aes.decrypt_ecb(test_in_3, test_in_4)

		assert my_output_2 == test_correct_2

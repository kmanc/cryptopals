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

	@staticmethod
	def test_decrypt_cbc():
		test_in_1 = b"T\xe0&~fx\xe6\xbd1\xd2\xf3\xab\x86\xe8$[ub\xbf\xc0(\x0b?\xa6\xac2q\xdf\x11\xfa\xb54"
		test_in_2 = b"Sixteen byte key"
		test_in_3 = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
		test_correct_1 = b"This is my no IV CBC test\x07\x07\x07\x07\x07\x07\x07"
		my_output_1 = aes.decrypt_cbc(test_in_1, test_in_2, test_in_3)

		assert my_output_1 == test_correct_1

		test_in_4 = b".\xe4\xa1\xe4\x14]'\x80\xbbw\xa1\xc5NOZ\xba\xea\xd7\xcd\xf5t+\xfe\xe1\x92\xc0\x1b\xfd\x9bd\x11\x15"
		test_in_5 = b"Sixteen byte key"
		test_in_6 = b"0123456789abcdef"
		test_correct_2 = b"What happens if you have an IV?\x01"
		my_output_2 = aes.decrypt_cbc(test_in_4, test_in_5, test_in_6)

		assert my_output_2 == test_correct_2

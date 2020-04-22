from cryptopals.building_blocks import xor


class Xor:

	@staticmethod
	def test_same_length():
		test_in_1 = b"Show me how this thing works!!"
		test_in_2 = b"\x00\t\x16WP\x01\x00A\x1b\nWA\x1a\x0cI:\x00\x03\x01\x05\x02GS\x1f\x00\x05K\nNT"
		test_correct = b"Say please and I will show you"
		my_output = xor.xor_same_length(test_in_1, test_in_2)

		assert my_output == test_correct

	@staticmethod
	def test_keyed():
		test_in_1 = b"Show me how this thing works!!"
		test_in_2 = b"\x00\t\x16WP\x01\x00A\x1b\nWA\x1a\x0cI:\x00\x03\x01\x05\x02GS\x1f\x00\x05K\nNT"
		test_correct = b"Say please and I will show you"
		my_output = xor.xor_keyed(test_in_1, test_in_2)

		assert my_output == test_correct

	@staticmethod
	def test_resize_bytes():
		test_in_1 = b"This should be made longer"
		test_in_2 = 50
		test_correct_1 = b"This should be made longerThis should be made long"
		my_output_1 = xor.resize_bytes(test_in_1, test_in_2)

		assert my_output_1 == test_correct_1

		test_in_3 = b"This should stay the same"
		test_in_4 = 25
		test_correct_2 = b"This should stay the same"
		my_output_2 = xor.resize_bytes(test_in_3, test_in_4)

		assert my_output_2 == test_correct_2

		test_in_5 = b"This should be made shorter"
		test_in_6 = 11
		test_correct_3 = b"This should"
		my_output_3 = xor.resize_bytes(test_in_5, test_in_6)

		assert my_output_3 == test_correct_3

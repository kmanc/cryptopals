from cryptopals import input_output


class InputOutput:

	@staticmethod
	def test_hex_to_bytes():
		test_in = "54657374696e672068657820746f206279746573"
		test_correct = b"Testing hex to bytes"
		my_output = input_output.hex_to_bytes(test_in)

		assert my_output == test_correct

	@staticmethod
	def test_bytes_to_hex():
		test_in = b"Testing bytes to hex"
		test_correct = "54657374696e6720627974657320746f20686578"
		my_output = input_output.bytes_to_hex(test_in)

		assert my_output == test_correct

	@staticmethod
	def test_resize_bytes():
		test_in_1 = b"This should be made longer"
		test_in_2 = 50
		test_correct_1 = b"This should be made longerThis should be made long"
		my_output_1 = input_output.resize_bytes(test_in_1, test_in_2)

		assert my_output_1 == test_correct_1

		test_in_3 = b"This should stay the same"
		test_in_4 = 25
		test_correct_2 = b"This should stay the same"
		my_output_2 = input_output.resize_bytes(test_in_3, test_in_4)

		assert my_output_2 == test_correct_2

		test_in_5 = b"This should be made shorter"
		test_in_6 = 11
		test_correct_3 = b"This should"
		my_output_3 = input_output.resize_bytes(test_in_5, test_in_6)

		assert my_output_3 == test_correct_3

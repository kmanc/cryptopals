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

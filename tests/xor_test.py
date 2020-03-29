from cryptopals import xor


class Xor:

	@staticmethod
	def test_fixed_length():
		test_in_1 = b"Show me how this thing works!!"
		test_in_2 = b"\x00\t\x16WP\x01\x00A\x1b\nWA\x1a\x0cI:\x00\x03\x01\x05\x02GS\x1f\x00\x05K\nNT"
		test_correct = b"Say please and I will show you"
		my_output = xor.fixed_length(test_in_1, test_in_2)

		assert my_output == test_correct

from cryptopals import base64


class Base64:

	@staticmethod
	def test_base64_encode():
		test_in_1 = b"This should have no equals."
		test_correct_1 = b"VGhpcyBzaG91bGQgaGF2ZSBubyBlcXVhbHMu"
		my_output_1 = base64.base64_encode(test_in_1)

		assert my_output_1 == test_correct_1

		test_in_2 = b"This should have one equals.."
		test_correct_2 = b"VGhpcyBzaG91bGQgaGF2ZSBvbmUgZXF1YWxzLi4="
		my_output_2 = base64.base64_encode(test_in_2)

		assert my_output_2 == test_correct_2

		test_in_3 = b"This should have two equals."
		test_correct_3 = b"VGhpcyBzaG91bGQgaGF2ZSB0d28gZXF1YWxzLg=="
		my_output_3 = base64.base64_encode(test_in_3)

		assert my_output_3 == test_correct_3

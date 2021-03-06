from cryptopals.attacks import aes


class AesAttacks:

	@staticmethod
	def test_detect_ecb():
		test_in_1 = b"\xd8\x80a\x97@\xa8\xa1\x9bx@\xa8\xa3\x1c\x81\n=\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83\xe2\xdd\x05/kd\x1d\xbf\x9d\x11\xb04\x85B\xbbW\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83\x94u\xc9\xdf\xdb\xc1\xd4e\x97\x94\x9d\x9c~\x82\xbfZ\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83\x97\xa9>\xab\x8dj\xec\xd5fH\x91Tx\x9ak\x03\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83\xd4\x03\x18\x0c\x98\xc8\xf6\xdb\x1f*?\x9c@@\xde\xb0\xabQ\xb2\x993\xf2\xc1#\xc5\x83\x86\xb0o\xba\x18j"
		test_correct_1 = True
		my_output_1 = aes.detect_ecb(test_in_1)

		assert my_output_1 == test_correct_1

		test_in_2 = b"\xb6\xfa\x8e\xc4\xe0aJ\xe8\xd1\xcd\x80\xd5>\xa6\xb9\xefH\x97\xda\xaa\xe7f\xec\xafc\xb8\x9e;,z\xef\xe4\x158\xe6\xad\xa1\xa9\xf2\xf1'\xa3i\xd17\xff\x97\x05\xe1(\xf7\xbf\x92\x9aw\x01c\x06\xe5$\xe0\xf4\x82\xfb\x82*Q=\xd6\xc8\x19\x83L\x12@\xadn\x05\xab2\x8f\xdf\x1c\xb0\xd6\xb0\xb8J\x10`3L>\x0cxyv\x90g\xa0\x12sJ\xdfNR\x05\xe9 \xf6\xab\x17\xe9>\x19M/\xcbW\xbf}\x0f\xbc\xfb\x89\x86\x94^\xef\x13=\xd2\xf0\x1c\x11U\xa6J\xa8\xd3\xef\x15\x91\xfaw\xcf\xcb\x1a-\r\x91\xf5iK\x1c\x05\x9a\xd3H\xd8"
		test_correct_2 = False
		my_output_2 = aes.detect_ecb(test_in_2)

		assert my_output_2 == test_correct_2

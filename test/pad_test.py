from cryptopals.building_blocks import pad


class Statistics:

	@staticmethod
	def test_english_score():
		test_in_1 = b"This is sixteen!"
		test_in_2 = 19
		test_correct_1 = b"This is sixteen!\x03\x03\x03"
		my_output_1 = pad.pkcs_7_pad(test_in_1, test_in_2)

		assert my_output_1 == test_correct_1

		test_in_3 = b"This is sixteen!"
		test_in_4 = 16
		test_correct_2 = b"This is sixteen!\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10"
		my_output_2 = pad.pkcs_7_pad(test_in_3, test_in_4)

		assert my_output_2 == test_correct_2

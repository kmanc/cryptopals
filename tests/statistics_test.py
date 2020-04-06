from cryptopals import statistics


class Statistics:

	@staticmethod
	def test_english_score():
		test_in_1 = b"The chances this is English is:"
		test_correct_1 = 27
		my_output_1 = statistics.english_score(test_in_1)

		assert my_output_1 == test_correct_1

		test_in_2 = b"tHE CHANCES thIS iS eNglIsh is???"
		test_correct_2 = 27
		my_output_2 = statistics.english_score(test_in_2)

		assert my_output_2 == test_correct_2

	@staticmethod
	def test_hamming_distance():
		test_in_1 = b"this is a test"
		test_in_2 = b"wokka wokka!!!"
		test_correct_1 = 37
		my_output_1 = statistics.hamming_distance(test_in_1, test_in_2)

		assert my_output_1 == test_correct_1

		test_in_3 = b"This is the tale of,"
		test_in_4 = b"Captain Jack Sparrow"
		test_correct_2 = 55
		my_output_2 = statistics.hamming_distance(test_in_3, test_in_4)

		assert my_output_2 == test_correct_2

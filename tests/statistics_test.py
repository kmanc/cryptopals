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

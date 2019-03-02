from cryptopals import generate


class Generate:

    @staticmethod
    def test_repeat_extend_string():
        """Tests repeating a string to a certain length"""

        test_input = b"Hello"
        test_length = 13
        desired_output = b"HelloHelloHel"
        my_output = generate.repeat_extend_string(test_input, test_length)

        assert my_output == desired_output

    @staticmethod
    def test_english_score():
        """Tests a simple English scoring function"""

        test_input = b"Hello, my name is Kevin"
        desired_output = 17
        my_output = generate.english_score(test_input)

        assert my_output == desired_output

    @staticmethod
    def test_hamming_distance():
        """Tests a simple English scoring function"""

        test_input_1 = b"this is a test"
        test_input_2 = b"wokka wokka!!!"
        desired_output = 37
        my_output = generate.hamming_distance(test_input_1, test_input_2)

        assert my_output == desired_output


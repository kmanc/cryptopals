from cryptopals.challenges import set_1, file


class TestChallenges:

    @staticmethod
    def test_challenge_1():
        """Hex to base64"""

        challenge_file = file.to_string("tests/challenge_inputs/set_1/challenge_1.txt")
        answer_file = file.to_string("tests/challenge_answers/set_1/challenge_1.txt")

        attack_output = set_1.hex_to_base64(challenge_file)

        assert attack_output == answer_file

    @staticmethod
    def test_challenge_2():
        """Fixed size hex string XOR"""

        challenge_file = file.to_lines("tests/challenge_inputs/set_1/challenge_2.txt")
        answer_file = file.to_string("tests/challenge_answers/set_1/challenge_2.txt")

        attack_output = set_1.fixed_size_hex_xor(challenge_file[0], challenge_file[1])

        assert attack_output == answer_file

    @staticmethod
    def test_challenge_3():
        """Break single byte XOR"""

        challenge_file = file.to_string("tests/challenge_inputs/set_1/challenge_3.txt")
        answer_file = file.to_string("tests/challenge_answers/set_1/challenge_3.txt")

        attack_output = set_1.break_repeat_hex_char_xor(challenge_file)

        assert attack_output.upper() == answer_file.upper()

    @staticmethod
    def test_challenge_4():
        """Break single byte XOR"""

        challenge_file = file.to_lines("tests/challenge_inputs/set_1/challenge_4.txt")
        answer_file = file.to_string("tests/challenge_answers/set_1/challenge_4.txt")

        attack_output = set_1.find_and_break_repeat_hex_char_xor(challenge_file)

        assert attack_output.upper() == answer_file.upper()

    @staticmethod
    def test_challenge_5():
        """Do repeat key XOR"""

        challenge_file = file.to_string("tests/challenge_inputs/set_1/challenge_5.txt")
        answer_file = file.to_string("tests/challenge_answers/set_1/challenge_5.txt")

        attack_output = set_1.repeat_key_xor(challenge_file)

        assert attack_output == answer_file

    @staticmethod
    def test_challenge_6():
        """Break repeat key XOR"""

        challenge_file = file.to_lines("tests/challenge_inputs/set_1/challenge_6.txt")
        answer_file = file.to_string("tests/challenge_answers/set_1/challenge_6.txt")

        attack_output = set_1.break_repeat_key_xor(challenge_file)

        assert attack_output.upper() == answer_file.upper()


from cryptopals import attack
from cryptopals import file


class TestChallenges:

    @staticmethod
    def test_challenge_1():
        """Hex to base64"""

        challenge_file = file.to_string("tests/challenge_inputs/set_1/challenge_1.txt")
        answer_file = file.to_string("tests/challenge_answers/set_1/challenge_1.txt")

        attack_output = attack.hex_to_base64(challenge_file)

        assert attack_output == answer_file

    @staticmethod
    def test_challenge_2():
        """Fixed size hex string XOR"""

        challenge_file = file.to_lines("tests/challenge_inputs/set_1/challenge_2.txt")
        answer_file = file.to_string("tests/challenge_answers/set_1/challenge_2.txt")

        attack_output = attack.fixed_size_hex_xor(challenge_file[0], challenge_file[1])

        assert attack_output == answer_file

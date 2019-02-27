from cryptopals import attack
from cryptopals import file


class TestChallenges:

    @staticmethod
    def test_challenge_1():
        """Hex to base64
        https://cryptopals.com/sets/1/challenges/1"""

        challenge_file = file.to_string("tests/challenge_inputs/set_1_challenge_1.txt")
        answer_file = file.to_bytes("tests/challenge_answers/set_1_challenge_1.txt")

        attack_output = attack.hex_to_base64(challenge_file)

        assert attack_output == answer_file

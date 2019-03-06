from cryptopals.challenges import set_2, file


class Challenges:

    @staticmethod
    def test_challenge_9():
        """PKCS#7 padding"""

    challenge_file = file.to_string("tests/challenge_inputs/set_2/challenge_9.txt")
    answer_file = file.to_bytes("tests/challenge_answers/set_2/challenge_9.txt")

    attack_output = set_2.pkcs_7_pad(challenge_file)

    assert attack_output == answer_file + b"\x04\x04\x04\x04"

    @staticmethod
    def test_challenge_10():
        """AES CBC decryption"""

    challenge_file = file.to_bytes("tests/challenge_inputs/set_2/challenge_10.txt")
    challenge_key = "YELLOW SUBMARINE"
    challenge_iv = "\x00" * 16
    answer_file = file.to_bytes("tests/challenge_answers/set_2/challenge_10.txt")

    attack_output = set_2.aes_cbc_decrypt(challenge_file, challenge_key, challenge_iv)

    assert attack_output == answer_file + b"\x04\x04\x04\x04"


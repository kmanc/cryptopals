from cryptopals import generate
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

    @staticmethod
    def test_challenge_11():
        """AES ECB/CBC detection oracle"""

    challenge_file = file.to_bytes("tests/challenge_inputs/set_2/challenge_11.txt")
    challenge_key = "YELLOW SUBMARINE"
    challenge_iv = "\x00" * 16
    answer_file = file.to_lines("tests/challenge_answers/set_2/challenge_11.txt")

    attack_output = set_2.aes_ecb_cbc_oracle(challenge_file, challenge_key, challenge_iv)

    assert attack_output[0] == answer_file[0]
    assert attack_output[1] == answer_file[1]
    assert attack_output[2] == answer_file[2]
    assert attack_output[3] == answer_file[3]
    assert attack_output[4] == answer_file[4]

    @staticmethod
    def test_challenge_12():
        """AES ECB bytes-at-a-time break"""

        challenge_file = file.to_bytes("tests/challenge_inputs/set_2/challenge_12.txt")
        challenge_key = generate.random_byte_string(16)
        answer_file = file.to_bytes("tests/challenge_answers/set_2/challenge_12.txt")

        attack_output = set_2.aes_ecb_bytes_at_a_time(challenge_file, challenge_key)

        assert attack_output == answer_file


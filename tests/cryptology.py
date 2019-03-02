from cryptopals import convert, cryptology, pad
from cryptopals.challenges import file


class Cryptology:

    @staticmethod
    def test_decrypt_aes_ecb():
        """Tests AES ECB decryption"""

        test_input = file.to_string("tests/other_resources/lose_yourself_ecb_yellow_submarine_hex.txt")
        test_input = convert.hex_to_bytes(test_input)
        test_key = b"YELLOW SUBMARINE"
        desired_output = file.to_bytes("tests/other_resources/lose_yourself_lyrics.txt")
        my_output = cryptology.decrypt_aes_ecb(test_input, test_key)

        assert my_output == desired_output + b"\x01"

    @staticmethod
    def test_detect_aes_ecb():
        """Tests detecting AES ECB encryption"""

        test_input = file.to_lines("tests/other_resources/aes_ecb_line_and_random_line.txt")
        desired_output_1 = True
        my_output_1 = cryptology.detect_aes_ecb(test_input[0])
        desired_output_2 = False
        my_output_2 = cryptology.detect_aes_ecb(test_input[1])

        assert my_output_1 == desired_output_1
        assert my_output_2 == desired_output_2

    @staticmethod
    def test_decrypt_aes_cbc():
        """Tests decrypting AES CBC encryption"""

        test_input = file.to_string("tests/other_resources/lose_yourself_cbc_yellow_submarine_iv_0_hex.txt")
        test_input = convert.hex_to_bytes(test_input)
        test_key = b"YELLOW SUBMARINE"
        test_iv = b"\x00" * 16
        desired_output = file.to_bytes("tests/other_resources/lose_yourself_lyrics.txt")
        my_output = cryptology.decrypt_aes_cbc(test_input, test_key, test_iv)

        assert my_output == desired_output + b"\x01"

    @staticmethod
    def test_encrypt_aes_ecb():
        """Tests AES ECB encryption"""

        test_input = file.to_bytes("tests/other_resources/lose_yourself_lyrics.txt")
        test_input = pad.pkcs_7(test_input, 16)
        test_key = b"YELLOW SUBMARINE"
        hex_output = file.to_string("tests/other_resources/lose_yourself_ecb_yellow_submarine_hex.txt")
        desired_output = convert.hex_to_bytes(hex_output)
        my_output = cryptology.encrypt_aes_ecb(test_input, test_key)

        assert my_output == desired_output

    @staticmethod
    def test_encrypt_aes_cbc():
        """Tests encrypting AES CBC encryption"""

        test_input = file.to_bytes("tests/other_resources/lose_yourself_lyrics.txt")
        test_input = pad.pkcs_7(test_input, 16)
        test_key = b"YELLOW SUBMARINE"
        test_iv = b"\x00" * 16
        hex_output = file.to_string("tests/other_resources/lose_yourself_cbc_yellow_submarine_iv_0_hex.txt")
        desired_output = convert.hex_to_bytes(hex_output)
        my_output = cryptology.encrypt_aes_cbc(test_input, test_key, test_iv)

        assert my_output == desired_output


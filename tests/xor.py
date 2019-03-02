from cryptopals import convert, xor
from cryptopals.challenges import file


class XOR:

    @staticmethod
    def test_fixed_size_xor():
        """Tests xor"""

        test_input = b"Hello"
        test_key = b"elloH"
        desired_output = b"-\t\x00\x03'"
        my_output = xor.fixed_size(test_input, test_key)

        assert my_output == desired_output

    @staticmethod
    def test_repeat_key():
        """Tests XOR with repeat key"""

        test_input = b"Hello"
        test_key = b"AB"
        desired_output = b"\t'-.."
        my_output = xor.repeat_key(test_input, test_key)

        assert my_output == desired_output

    @staticmethod
    def test_break_single_byte():
        """Tests attack against single byte XOR"""

        test_input = b"yT]]^"
        desired_output = b"HELLO"
        my_output = xor.break_single_byte(test_input)

        assert my_output.upper() == desired_output

    @staticmethod
    def test_determine_key_length():
        """Determines most likely key length for an XOR ciphertext"""

        test_input = file.to_string("tests/other_resources/lose_yourself_xor_eminem_hex.txt")
        test_bytes = convert.hex_to_bytes(test_input)
        desired_output = [9, 6, 5]
        my_output = xor.determine_key_length(test_bytes)

        assert my_output == desired_output

    @staticmethod
    def test_break_repeat_key():
        """Tests attack against repeated key XOR"""

        test_input = file.to_string("tests/other_resources/lose_yourself_xor_eminem_hex.txt")
        test_bytes = convert.hex_to_bytes(test_input)
        desired_output = file.to_bytes("tests/other_resources/lose_yourself_lyrics.txt")
        my_output = xor.break_repeat_key(test_bytes)

        assert my_output.upper() == desired_output.upper()


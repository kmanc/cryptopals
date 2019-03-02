from cryptopals import xor, convert, cryptology, generate, pad
from cryptopals.challenges import file


class TestConvert:

    @staticmethod
    def test_ascii_to_bytes():
        """Tests ascii --> bytes"""

        test_input = "Hello"
        desired_output = b"Hello"
        my_output = convert.ascii_to_bytes(test_input)

        assert my_output == desired_output

    @staticmethod
    def test_ascii_to_hex():
        """Tests ascii --> hex"""

        test_input = "Hello"
        desired_output = "48656c6c6f"
        my_output = convert.ascii_to_hex(test_input)

        assert my_output == desired_output

    @staticmethod
    def test_base64_to_bytes():
        """Tests base64 --> bytes"""

        test_input = b"SGVsbG8="
        desired_output = b"Hello"
        my_output = convert.base64_to_bytes(test_input)

        assert my_output == desired_output

    @staticmethod
    def test_bytes_to_ascii():
        """Tests bytes --> ascii"""

        test_input = b"Hello"
        desired_output = "Hello"
        my_output = convert.bytes_to_ascii(test_input)

        assert my_output == desired_output

    @staticmethod
    def test_bytes_to_base64():
        """Tests bytes --> base64"""

        test_input = b"Hello"
        desired_output = b"SGVsbG8="
        my_output = convert.bytes_to_base64(test_input)

        assert my_output == desired_output

    @staticmethod
    def test_bytes_to_hex():
        """Tests bytes --> hex"""

        test_input = b"Hello"
        desired_output = "48656c6c6f"
        my_output = convert.bytes_to_hex(test_input)

        assert my_output == desired_output

    @staticmethod
    def test_hex_to_ascii():
        """Tests hex --> ascii"""

        test_input = "48656c6c6f"
        desired_output = "Hello"
        my_output = convert.hex_to_ascii(test_input)

        assert my_output == desired_output

    @staticmethod
    def test_hex_to_bytes():
        """Tests hex --> bytes"""

        test_input = "48656c6c6f"
        desired_output = b"Hello"
        my_output = convert.hex_to_bytes(test_input)

        assert my_output == desired_output


class TestXOR:
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


class TestGenerate:

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


class TestCryptology:

    @staticmethod
    def test_repeat_extend_string():
        """Tests AES ECB decryption"""

        test_input = b'\xa4\xb7\x8dMy\xd1\x92j_\xfd\x86:m\xfdj\x82'
        test_key = b"I'm a key len 16"
        desired_output = b"Hello\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b"
        my_output = cryptology.decrypt_aes_ecb(test_input, test_key)

        assert my_output == desired_output

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


class TestPad:

    @staticmethod
    def test_pkcs_7_pad():
        """Tests PKCS#7 padding"""

        test_input = b"YELLOW SUBMARINE"
        desired_output_1 = b'YELLOW SUBMARINE\x04\x04\x04\x04'
        my_output_1 = pad.pkcs_7(test_input, 20)
        desired_output_2 = b'YELLOW SUBMARINE\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10'
        my_output_2 = pad.pkcs_7(test_input, 16)

        assert my_output_1 == desired_output_1
        assert my_output_2 == desired_output_2



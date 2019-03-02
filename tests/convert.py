from cryptopals import convert


class Convert:

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


from cryptopals.building_blocks import convert
from cryptopals.building_blocks import encrypt
from cryptopals.building_blocks import generate
from cryptopals.building_blocks import pad
from cryptopals.building_blocks import xor


class TestBuildingBlocks:

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

    @staticmethod
    def test_fixed_size_xor():
        """Tests xor"""

        test_input = b"Hello"
        test_key = b"elloH"
        desired_output = b"-\t\x00\x03'"
        my_output = xor.fixed_size(test_input, test_key)

        assert my_output == desired_output


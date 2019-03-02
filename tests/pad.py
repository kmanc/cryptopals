from cryptopals import pad


class Pad:

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

    @staticmethod
    def test_undo_pkcs_7_pad():
        """Tests undoing PKCS#7 padding"""

        test_input_1 = b"YELLOW SUBMARINE\x04\x04\x04\x04"
        desired_output_1 = b'YELLOW SUBMARINE'
        my_output_1 = pad.undo_pkcs_7(test_input_1)
        test_input_2 = b"YELLOW SUBMARINE\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10"
        desired_output_2 = b'YELLOW SUBMARINE'
        my_output_2 = pad.undo_pkcs_7(test_input_2)

        assert my_output_1 == desired_output_1
        assert my_output_2 == desired_output_2

from cryptopals import convert, pad


def pkcs_7_pad(input_string):
    """https://cryptopals.com/sets/2/challenges/9"""

    input_bytes = convert.ascii_to_bytes(input_string)
    output = pad.pkcs_7(input_bytes, 20)

    return output


def aes_cbc_decrypt(input_string):
    """https://cryptopals.com/sets/2/challenges/10"""

    #input_bytes = convert.ascii_to_bytes(input_string)
    #output = pad.pkcs_7(input_bytes, 20)

    return True

from cryptopals import convert, cryptology, pad


def pkcs_7_pad(input_string):
    """https://cryptopals.com/sets/2/challenges/9"""

    input_bytes = convert.ascii_to_bytes(input_string)
    output = pad.pkcs_7(input_bytes, 20)

    return output


def aes_cbc_decrypt(input_base64, input_key, input_iv):
    """https://cryptopals.com/sets/2/challenges/10"""

    input_bytes = convert.base64_to_bytes(input_base64)
    key_bytes = convert.ascii_to_bytes(input_key)
    iv_bytes = convert.ascii_to_bytes(input_iv)
    plaintext_string = cryptology.decrypt_aes_cbc(input_bytes, key_bytes, iv_bytes)
    output = plaintext_string.replace(b" \n", b"\n")

    return output

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


def aes_ecb_cbc_oracle(input_bytes, input_key, input_iv):
    """https://cryptopals.com/sets/2/challenges/11"""

    padded_input = pad.pkcs_7(input_bytes, 16)
    key_bytes = convert.ascii_to_bytes(input_key)
    iv_bytes = convert.ascii_to_bytes(input_iv)
    ecb_ct = cryptology.encrypt_aes_ecb(padded_input, key_bytes)
    cbc_ct = cryptology.encrypt_aes_cbc(padded_input, key_bytes, iv_bytes)
    test_list = [cryptology.detect_aes_ecb(ecb_ct),
                 cryptology.detect_aes_ecb(cbc_ct),
                 cryptology.detect_aes_ecb(cbc_ct),
                 cryptology.detect_aes_ecb(cbc_ct),
                 cryptology.detect_aes_ecb(ecb_ct)]
    print(test_list)
    output = ['ECB' if x is True else 'CBC' for x in test_list]

    return output

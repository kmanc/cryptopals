from cryptopals import convert, cryptology, generate, pad


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
    output = ['ECB' if x is True else 'CBC' for x in test_list]

    return output


def aes_ecb_bytes_at_a_time(unknown_input, unknown_key):
    """https://cryptopals.com/sets/2/challenges/12"""

    unknown_append = convert.base64_to_bytes(unknown_input)
    size = 1
    while True:
        padded = pad.pkcs_7(b"", size)
        try:
            cryptology.encrypt_aes_ecb(padded, unknown_key)
        except ValueError:
            size += 1
            continue
        block_size = len(padded)
        break
    brute_dict = cryptology.brute_force_aes_ecb_table(block_size, unknown_key)
    output = b""
    for char in unknown_append:
        table_key = cryptology.encrypt_aes_ecb(b"A" * (block_size - 1) + bytes([char]), unknown_key)
        output += brute_dict[table_key]

    return output


def aes_ecb_cut_and_paste(input_bytes, unknown_key):
    """https://cryptopals.com/sets/2/challenges/13"""

    email_profile = generate.profile_from_email_address(input_bytes)
    padded_profile = pad.pkcs_7(email_profile, 16)
    encrypted_profile = cryptology.encrypt_aes_ecb(padded_profile, unknown_key)
    profile_cut = encrypted_profile[:-16]
    padded_admin = pad.pkcs_7(b'admin', 16)
    admin_paste = cryptology.encrypt_aes_ecb(padded_admin, unknown_key)
    profile_plaintext = cryptology.decrypt_aes_ecb(profile_cut + admin_paste, unknown_key)
    output = pad.undo_pkcs_7(profile_plaintext)

    return output







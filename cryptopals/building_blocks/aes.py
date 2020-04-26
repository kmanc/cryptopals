from Crypto.Cipher import AES


def decrypt_ecb(input_bytes_1, input_bytes_2):
    cipher = AES.new(input_bytes_2, AES.MODE_ECB)

    return cipher.decrypt(input_bytes_1)

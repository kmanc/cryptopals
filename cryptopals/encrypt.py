from Crypto.Cipher import AES


__AES_BLOCK_SIZE = 16


def aes_ecb_decrypt(ciphertext, key):
    """Take in a byte string that represents an AES-ECB encrypted ciphertext with using byte string key. Outputs the
    plaintext"""
    cipher = AES.new(key, AES.MODE_ECB)

    return cipher.decrypt(ciphertext)

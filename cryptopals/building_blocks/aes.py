from Crypto.Cipher import AES


def decrypt_ecb(ciphertext_bytes: bytes, key_bytes: bytes):
    """Takes in a ciphertext and a key as bytes. Decrypts the ciphertext using the key under AES ECB"""
    cipher = AES.new(key_bytes, AES.MODE_ECB)

    return cipher.decrypt(ciphertext_bytes)

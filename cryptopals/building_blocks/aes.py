from Crypto.Cipher import AES
from cryptopals.building_blocks import xor


def decrypt_ecb(ciphertext_bytes: bytes, key_bytes: bytes):
    """Takes in a ciphertext and a key as bytes. Decrypts the ciphertext using the key under AES ECB"""
    cipher = AES.new(key_bytes, AES.MODE_ECB)

    return cipher.decrypt(ciphertext_bytes)


def decrypt_cbc(ciphertext_bytes: bytes, key_bytes: bytes, iv_bytes: bytes):
    """Takes in byte strings representing AES-CBC encrypted ciphertext, key, iv. Outputs the plaintext"""
    plaintext_bytes = bytes()
    for index in range(0, len(ciphertext_bytes), 16):
        ciphertext_chunk = ciphertext_bytes[index: index + 16]
        decrypted_chunk = decrypt_ecb(ciphertext_chunk, key_bytes)
        plaintext_chunk = xor.xor_same_length(decrypted_chunk, iv_bytes)
        plaintext_bytes += plaintext_chunk
        iv_bytes = ciphertext_chunk

    return plaintext_bytes

from cryptopals import xor
from Crypto.Cipher import AES


__AES_BLOCK_SIZE = 16


def decrypt_aes_ecb(ciphertext, key):
    """Take in a byte string that represents an AES-ECB encrypted ciphertext with using byte string key. Outputs the
    plaintext"""
    cipher = AES.new(key, AES.MODE_ECB)

    return cipher.decrypt(ciphertext)


def detect_aes_ecb(ciphertext):
    """Takes in a ciphertext and returns True if the line is determined to be ECB by repeated blocks of ciphertext"""
    number_original_chunks = len(ciphertext) // __AES_BLOCK_SIZE
    dedupe_chunks = {ciphertext[i * __AES_BLOCK_SIZE: (i + 1) * __AES_BLOCK_SIZE] for i in range(number_original_chunks)}

    if len(dedupe_chunks) < number_original_chunks:
        return True

    return False


def decrypt_aes_cbc(ciphertext, key, iv):
    """Take in byte strings representing AES-CBC encrypted ciphertext, key, iv. Output the plaintext"""
    plaintext = bytes()
    for index in range(0, len(ciphertext), __AES_BLOCK_SIZE):
        ciphertext_chunk = ciphertext[index: index + __AES_BLOCK_SIZE]
        decrypted_chunk = decrypt_aes_ecb(ciphertext_chunk, key)
        plaintext_chunk = xor.fixed_size(decrypted_chunk, iv)
        plaintext += plaintext_chunk
        iv = ciphertext_chunk

    return plaintext


def encrypt_aes_ecb(plaintext, key):
    """Take in a byte strings representing plaintext and a key. Outputs the AES-ECB encrypted ciphertext"""
    cipher = AES.new(key, AES.MODE_ECB)

    return cipher.encrypt(plaintext)


def encrypt_aes_cbc(plaintext, key, iv):
    """Take in byte strings representing plaintext, key, iv. Output the AES-CBC encrypted ciphertext"""
    ciphertext = bytes()
    cipher = AES.new(key, AES.MODE_ECB)
    for index in range(0, len(plaintext), __AES_BLOCK_SIZE):
        plaintext_chunk = plaintext[index: index + __AES_BLOCK_SIZE]
        xored_chunk = xor.fixed_size(plaintext_chunk, iv)
        ciphertext_chunk = cipher.encrypt(xored_chunk)
        ciphertext += ciphertext_chunk
        iv = ciphertext_chunk

    return ciphertext


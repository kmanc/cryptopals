def detect_ecb(input_bytes: bytes):
    """Takes in a byte string. Determines whether or not it is likely to be an AEC-ECB-encrypted ciphertext"""
    number_original_chunks = len(input_bytes) // 16
    dedupe_chunks = {input_bytes[i: i + 16] for i in range(0, len(input_bytes), 16)}
    result = False

    if len(dedupe_chunks) < number_original_chunks:
        result = True

    return result

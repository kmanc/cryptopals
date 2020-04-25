def detect_ecb(input_bytes):
    number_original_chunks = len(input_bytes) // 16
    dedupe_chunks = {input_bytes[i: i + 16] for i in range(0, len(input_bytes), 16)}

    if len(dedupe_chunks) < number_original_chunks:
        return True

    return False

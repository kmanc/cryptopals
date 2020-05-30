def pkcs_7_pad(input_bytes: bytes, length: int):
    size_needed = length - (len(input_bytes) % length)
    padded_bytes = input_bytes + (bytes([size_needed]) * size_needed)

    return padded_bytes



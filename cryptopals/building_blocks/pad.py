def pkcs_7_pad(input_bytes: bytes, length: int):
    """Takes in a byte string and an integer. Outputs a byte string padded to a block size of integer following PKCS#7 standards"""
    size_needed = length - (len(input_bytes) % length)
    padded_bytes = input_bytes + (bytes([size_needed]) * size_needed)

    return padded_bytes



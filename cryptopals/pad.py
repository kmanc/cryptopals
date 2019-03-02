def pkcs_7(byte_string, length):
    """Take in a byte string and a length. Output the byte string padded to block size = length according to PKCS#7"""
    size_needed = length - (len(byte_string) % length)
    byte_string += bytes([size_needed]) * size_needed

    return byte_string

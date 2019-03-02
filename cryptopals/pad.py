def pkcs_7(byte_string, length):
    """Take in a byte string and a length. Output the byte string padded to block size = length according to PKCS#7"""
    size_needed = length - (len(byte_string) % length)
    byte_string += bytes([size_needed]) * size_needed

    return byte_string


def undo_pkcs_7(byte_string):
    """Take in a byte string that has been PKCS padded. Output the unpadded byte string or a value error if
    padding is not valid"""
    padded = True
    last_byte = byte_string[-1]
    for char in byte_string[-last_byte:]:
        if char != last_byte:
            padded = False

    if padded is True:
        return byte_string[:-last_byte]
    raise ValueError('Invalid padding')

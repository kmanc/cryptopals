def fixed_length(input_bytes_1, input_bytes_2):
    list_of_chars = [(a ^ b) for (a, b) in zip(input_bytes_1, input_bytes_2)]
    return bytes(list_of_chars)

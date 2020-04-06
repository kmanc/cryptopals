def english_score(input_bytes):
    # The following set contains the decimal number that corresponds to the ASCII for the most common english
    # characters ('ETAOIN SHRDLU') in both upper and lower case, also including the space
    point_worthy = {
        32,
        65,
        68,
        69,
        72,
        73,
        76,
        78,
        79,
        82,
        83,
        84,
        85,
        97,
        101,
        104,
        105,
        100,
        108,
        110,
        111,
        114,
        115,
        116,
        117
    }

    chars_in_point_worthy = list(filter(point_worthy.__contains__, input_bytes))

    return len(chars_in_point_worthy)


def hamming_distance(byte_string_1, byte_string_2):
    xor_result = ((a ^ b) for (a, b) in zip(byte_string_1, byte_string_2))
    joined_binary_string = "".join([bin(num) for num in xor_result])

    return joined_binary_string.count("1")

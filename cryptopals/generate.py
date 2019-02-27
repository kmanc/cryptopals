import math


def repeat_extend_string(byte_string, length):
    """Takes in a byte string and a length. Extends the byte string to the length by repeating the input until length
    is reached"""
    return (byte_string * math.ceil(length / len(byte_string)))[:length]


def english_score(byte_string):
    """Takes in a byte string that might be English text. Outputs a score corresponding to how likely it is that the
    string is in fact English"""
    # The following set contains the decimal number associated with the most common english characters
    # ('ETAOIN SHRDLU') in both upper and lower case, also including the space
    point_worthy = {69, 101, 84, 116, 65, 97, 79, 111, 73, 105, 78, 110,
                    32, 83, 115, 72, 104, 82, 114, 68, 100, 76, 108, 85, 117}

    chars_in_point_worthy = list(filter(point_worthy.__contains__, byte_string))

    return len(chars_in_point_worthy)


def hamming_score(byte_string_1, byte_string_2):
    """Takes in two byte strings. Outputs the hamming distance (# of bits that are different) between the two"""
    xor_gen = ((a ^ b) for (a, b) in zip(byte_string_1, byte_string_2))
    joined_binary_string = "".join([bin(num) for num in xor_gen])

    return joined_binary_string.count("1")


def english_score(input_bytes):
    # The following set contains the decimal number associated with the most common english characters
    # ('ETAOIN SHRDLU') in both upper and lower case, also including the space
    point_worthy = {69, 101, 84, 116, 65, 97, 79, 111, 73, 105, 78, 110,
                    32, 83, 115, 72, 104, 82, 114, 68, 100, 76, 108, 85, 117}

    chars_in_point_worthy = list(filter(point_worthy.__contains__, input_bytes))

    return len(chars_in_point_worthy)

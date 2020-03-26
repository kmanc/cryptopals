alphabet = {0: b'A',
            1: b'B',
            2: b'C',
            3: b'D',
            4: b'E',
            5: b'F',
            6: b'G',
            7: b'H',
            8: b'I',
            9: b'J',
            10: b'K',
            11: b'L',
            12: b'M',
            13: b'N',
            14: b'O',
            15: b'P',
            16: b'Q',
            17: b'R',
            18: b'S',
            19: b'T',
            20: b'U',
            21: b'V',
            22: b'W',
            23: b'X',
            24: b'Y',
            25: b'Z',
            26: b'a',
            27: b'b',
            28: b'c',
            29: b'd',
            30: b'e',
            31: b'f',
            32: b'g',
            33: b'h',
            34: b'i',
            35: b'j',
            36: b'k',
            37: b'l',
            38: b'm',
            39: b'n',
            40: b'o',
            41: b'p',
            42: b'q',
            43: b'r',
            44: b's',
            45: b't',
            46: b'u',
            47: b'v',
            48: b'w',
            49: b'x',
            50: b'y',
            51: b'z',
            52: b'0',
            53: b'1',
            54: b'2',
            55: b'3',
            56: b'4',
            57: b'5',
            58: b'6',
            59: b'7',
            60: b'8',
            61: b'9',
            62: b'+',
            63: b'/'}


def base64_encode(input_bytes):
    binary_representation = ''
    output = b''

    for char in input_bytes:
        char_as_binary_string = bin(char)[2:]
        padded_to_eight = char_as_binary_string.rjust(8, '0')
        binary_representation += padded_to_eight
    new_chars_binary = [binary_representation[index: index + 6] for index in range(0, len(binary_representation), 6)]
    last_char = new_chars_binary[-1]

    if len(last_char) % 6 != 0:
        new_chars_binary[-1] = last_char.ljust(6, '0')

    for char in new_chars_binary:
        char_as_decimal = int(char, 2)
        output_char = alphabet[char_as_decimal]
        output += output_char

    if len(input_bytes) % 3 == 2:
        output += b'='

    if len(input_bytes) % 3 == 1:
        output += b'=='

    return output

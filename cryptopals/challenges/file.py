def to_bytes(file_name):
    """Takes in a file name. Outputs the contents of that file as a string"""
    with open(file_name, 'r') as f:
        data = f.read()

    return str.encode(data)


def to_hex(file_name):
    """Takes in a file name. Outputs the contents of that file as a hex string"""
    with open(file_name, 'r') as f:
        data = f.read()

    return str.encode(data).hex()


def to_string(file_name):
    """Takes in a file name. Outputs the contents of that file as a string"""
    with open(file_name, 'r') as f:
        data = f.read()

    return data


def to_lines(file_name):
    """Takes in a file name. Output a list of strings where each element is a line in the original file"""
    with open(file_name, 'r') as f:
        stripped_lines = list(map(str.strip, f))

    return stripped_lines

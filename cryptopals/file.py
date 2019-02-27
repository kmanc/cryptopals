def to_bytes(file_name):
    """Takes in a file name. Outputs the contents of that file as a string"""
    with open(file_name, 'r') as f:
        data = f.read()

    return str.encode(data)


def to_string(file_name):
    """Takes in a file name. Outputs the contents of that file as a string"""
    with open(file_name, 'r') as f:
        data = f.read()

    return data

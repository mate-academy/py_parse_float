"""
parse
"""
def parse(string: str) -> bool:
    """

    :param string: string
    :return: bool True if string is valid float number
    """
    if len(string) == 0:
        return False

    if string[0] == '-':
        string = string[1:]

    dot_count = 0

    for char in string:
        if char == '.':
            if dot_count != 0:
                return False

            dot_count += 1
            continue

        if ord(char) <= 48 or ord(char) >= 57:
            return False

    return True

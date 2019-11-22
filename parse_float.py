"""module docstring"""


def parse(string: str) -> bool:
    """ check if a string is a valid float-point number"""
    if not string:
        return False
    if string.isdigit() or (string[0] == "-" and string[1:].isdigit()):
        return True

    minus_count = 0
    dot_count = 0

    for i, char in enumerate(string):
        if not char.isdigit():
            if char == '.' and dot_count == 0:
                dot_count += 1
            elif i == 0 and char == '-' and minus_count == 0:
                minus_count += 1
            else:
                return False
    return True

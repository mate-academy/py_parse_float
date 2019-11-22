"""
parse string to float module
"""


def parse(strng: str) -> bool:
    """
    Check if a string is a valid float-point number.
    :param strng: str
    :return: bool
    """
    if strng.count('-') >= 2:
        return False
    return strng.replace('.', '', 1).lstrip('-').isdigit()

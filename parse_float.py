"""digits checker module"""


def parse(strng: str) -> bool:
    """digits checker function"""
    if not strng:
        return False
    dots = False
    for index, value in enumerate(strng):
        if value == "-" and index == 0:
            continue
        if value == "." and not dots:
            dots = True
        elif not value.isdigit():
            return False
    return True

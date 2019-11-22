"""parse_float module"""
import re


def parse(strng: str) -> bool:
    """
    Returns True if given string
    is valid float-point number,
    otherwise returns False
    """
    return bool(re.match(r"^-?\d+\.?\d+?$", strng))

"""The function to check if a string is a valid float-point number"""

import re


def parse(string: str) -> bool:
    """General function"""
    return bool(re.match(r'^-?\d+\.?\d*$', string))

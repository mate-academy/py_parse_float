"""Check if a string is a valid float-point number"""
import re


def parse(value: str) -> bool:
    """Function to check if a string is a valid float-point number"""
    if re.findall(r"^[+-]?[0-9]{1,2}([,.]?[0-9]{1,2})?$", value):
        return True
    return False

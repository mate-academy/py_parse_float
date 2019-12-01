"""parse module."""
import re


def parse(string_input: str) -> bool:
    """gets True or False if input is float number."""
    if not string_input or type(string_input) is not str:
        return False
    if string_input.count('-') > 1 or string_input.count('.') > 1 \
            or re.search('[a-zA-Z]', string_input):
        return False
    return True

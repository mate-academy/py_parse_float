"""parse module."""
import re


def parse(string_input: str) -> bool:
    """gets True or False if input is float number."""
    def is_string(initial_input: str) -> bool:
        return not initial_input or not isinstance(initial_input, str)

    def is_valid_string(some_str: str) -> bool:
        return some_str.count('-') > 1 or some_str.count('.') > 1 \
            or re.search('[a-zA-Z]', some_str)
    if is_string(string_input):
        return False

    if is_valid_string(string_input):
        return False
    return True

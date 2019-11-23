"""
docstring
"""


def parse(abc: str) -> bool:
    """

    :param abc:
    :return:
    """
    if abc.count('.') > 1 or abc.count('-') > 1 or len(abc) < 1 or any(ch.isalpha() for ch in abc):
        return False
    return True

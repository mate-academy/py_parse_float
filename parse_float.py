"""
check a string
"""

def parse(strg: str) -> bool:
    """
    func
    """

    if not strg:
        return False

    if '-' in strg[1:]:
        return False

    if strg.count('.') > 1:
        return False

    for i in strg:
        if i.isalpha():
            return False

    return True
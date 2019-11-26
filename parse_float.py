"""
check a string
"""

def parse(strg: str) -> bool:
    """
    func
    """

    if not strg or strg.count('.') > 1 or '-' in strg[1:]:
        return False

    for i in strg:
        if i.isalpha():
            return False

    return True

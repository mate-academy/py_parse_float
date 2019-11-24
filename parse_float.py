"""module docstring"""
def parse(mb_float):
    """docstring"""
    if not mb_float or mb_float[0] not in "-.0123456789" or mb_float.count(".") > 1:
        return False
    for i in range(1, len(mb_float)):
        if mb_float[i] not in ".0123456789":
            return False

    return True

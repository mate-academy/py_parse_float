"""docstring"""


def valid(check):
    """check for valid char"""
    if check.isdigit() or check == "-" or check == ".":
        return True
    return False


def parse(list_item: str) -> bool:
    """check string for float number"""
    if not list_item or list_item.count(".") > 1 or list_item.count("-") > 1:
        return False
    if list_item[0] == ".":
        return False
    if "-" in list_item and list_item[0] != "-":
        return False
    for i in list_item[1:]:
        if not valid(i):
            return False
    return True

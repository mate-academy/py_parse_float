"""
docstring
"""
import parse_float


def test_empty():
    """

    :return:
    """
    assert parse_float.parse("") == False


def test_int():
    """

    :return:
    """
    assert parse_float.parse("123") == True


def test_negative():
    """

    :return:
    """
    assert parse_float.parse("-123") == True


def test_float():
    """

    :return:
    """
    assert parse_float.parse("12.34") == True


def test_neg_float():
    """

    :return:
    """
    assert parse_float.parse("-12.43") == True


def test_double_dots():
    """

    :return:
    """
    assert parse_float.parse("1.2.3") == False


def test_minuses():
    """

    :return:
    """
    assert parse_float.parse("-12.-23") == False


def test_chars():
    """

    :return:
    """
    assert parse_float.parse("12abc235") == False

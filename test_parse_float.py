import parse_float


def test_empty():
    assert parse_float.parse("") == False


def test_int():
    assert parse_float.parse("123") == True


def test_negative():
    assert parse_float.parse("-123") == True


def test_float():
    assert parse_float.parse("12.34") == True


def test_neg_float():
    assert parse_float.parse("-12.43") == True


def test_double_dots():
    assert parse_float.parse("1.2.3") == False


def test_minuses():
    assert parse_float.parse("-12.-23") == False


def test_chars():
    assert parse_float.parse("12abc235") == False
from Code.Missing_Number import missing_number


def test_missing_number_1():
    assert missing_number([1, 2, 4, 5]) == [3]


def test_missing_number_2():
    assert missing_number([1, 2, 4, 5, 8, 9]) == [3, 6, 7]


def test_missing_number_3():
    assert missing_number([1, 3, 5]) == [2, 4]


def test_missing_number_4():
    assert missing_number([2, 3, 5, 6]) == [4]


def test_missing_number_5():
    assert missing_number([10, 12, 15]) == [11, 13, 14]

#  python -m pytest .\Test_Code\Test_Missing_Number.py
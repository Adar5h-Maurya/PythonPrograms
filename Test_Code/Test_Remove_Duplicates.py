from Code.Remove_Duplicates import remove_duplicates


def test_remove_duplicates_1():
    assert remove_duplicates([1, 2, 2, 3, 3, 4]) == [1, 2, 3, 4]


def test_remove_duplicates_2():
    assert remove_duplicates([5, 5, 5, 6, 7]) == [5, 6, 7]


def test_remove_duplicates_3():
    assert remove_duplicates([1, 1, 2, 3, 2]) == [1, 2, 3]


def test_remove_duplicates_4():
    assert remove_duplicates([10, 20, 10, 30]) == [10, 20, 30]


def test_remove_duplicates_5():
    assert remove_duplicates([1, 2, 3, 4]) == [1, 2, 3, 4]


#  python -m pytest .\Test_Code\Test_Remove_Duplicates.py
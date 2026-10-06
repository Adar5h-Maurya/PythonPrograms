from Code.Find_Duplicates import find_duplicates


def test_find_duplicates_1():
    assert find_duplicates([1, 2, 2, 3, 4, 4]) == [2, 4]


def test_find_duplicates_2():
    assert find_duplicates([1, 1, 2, 3, 3]) == [1, 3]


def test_find_duplicates_3():
    assert find_duplicates([5, 6, 7, 8]) == []


def test_find_duplicates_4():
    assert find_duplicates([10, 10, 20, 20, 30]) == [10, 20]


def test_find_duplicates_5():
    assert find_duplicates([1, 2, 2, 2, 3]) == [2]

# python -m pytest .\Test_Code\Test_Find_Duplicates.py
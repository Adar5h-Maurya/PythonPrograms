from Code.second_largest import second_largest


def test_second_largest_1():
    assert second_largest([10, 5, 20, 8]) == 10


def test_second_largest_2():
    assert second_largest([4, 15, 8, 12]) == 12


def test_second_largest_3():
    assert second_largest([100, 45, 50, 75]) == 75

def test_second_largest_4():
    assert second_largest([1, 5, 3, 2]) == 3


def test_second_largest_5():
    assert second_largest([20, 10, 30, 40]) == 30


#  python -m pytest .\Test_Code\Test_second_largest.py
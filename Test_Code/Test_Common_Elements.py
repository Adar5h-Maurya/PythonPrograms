from Code.Common_Elements import common_elements


def test_common_elements_1():
    assert common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]


def test_common_elements_2():
    assert common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]


def test_common_elements_3():
    assert common_elements([10, 20, 30], [40, 50, 60]) == []


def test_common_elements_4():
    assert set(common_elements([1, 2, 2, 3], [2, 3, 4])) == {2, 3}


def test_common_elements_5():
    assert set(common_elements([5, 10, 15], [5, 15, 20])) == {5, 15}

# python -m pytest .\Test_Code\Test_Common_Elements.py
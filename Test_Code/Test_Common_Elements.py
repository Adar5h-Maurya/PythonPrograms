from Code.Common_Elements import common_elements

assert common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]
print("Test Case 1 pass")

assert common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
print("Test Case 2 pass")

assert common_elements([10, 20, 30], [40, 50, 60]) == []
print("Test Case 3 pass")

assert set(common_elements([1, 2, 2, 3], [2, 3, 4])) == {2, 3}
print("Test Case 4 pass")

assert set(common_elements([5, 10, 15], [5, 15, 20])) == {5, 15}
print("Test Case 5 pass")


# python -m Test_Code.Test_Common_Elements
from Code.Find_Duplicates import find_duplicates

assert find_duplicates([1, 2, 2, 3, 4, 4]) == [2, 4]
print("Test Case 1 pass")

assert find_duplicates([1, 1, 2, 3, 3]) == [1, 3]
print("Test Case 2 pass")

assert find_duplicates([5, 6, 7, 8]) == []
print("Test Case 3 pass")

assert find_duplicates([10, 10, 20, 20, 30]) == [10, 20]
print("Test Case 4 pass")

assert find_duplicates([1, 2, 2, 2, 3]) == [2]
print("Test Case 5 pass")


# python -m Test_Code.Test_Find_Duplicates
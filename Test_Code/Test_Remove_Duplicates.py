from Code.Remove_Duplicates import remove_duplicates

assert remove_duplicates([1, 2, 2, 3, 3, 4]) == [1, 2, 3, 4]
print("Test Case 1 pass")

assert remove_duplicates([5, 5, 5, 6, 7]) == [5, 6, 7]
print("Test Case 2 pass")

assert remove_duplicates([1, 1, 2, 3, 2]) == [1, 2, 3]
print("Test Case 3 pass")

assert remove_duplicates([10, 20, 10, 30]) == [10, 20, 30]
print("Test Case 4 pass")

assert remove_duplicates([1, 2, 3, 4]) == [1, 2, 3, 4]
print("Test Case 5 pass")


# python -m Test_Code.Test_Remove_Duplicate
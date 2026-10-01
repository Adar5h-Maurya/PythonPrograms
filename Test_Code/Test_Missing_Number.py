from Code.Missing_Number import missing_number

assert missing_number([1, 2, 4, 5]) == [3]
print("Test Case 1 pass")

assert missing_number([1, 2, 4, 5, 8, 9]) == [3, 6, 7]
print("Test Case 2 pass")

assert missing_number([1, 3, 5]) == [2, 4]
print("Test Case 3 pass")

assert missing_number([2, 3, 5, 6]) == [4]
print("Test Case 4 pass")

assert missing_number([10, 12, 15]) == [11, 13, 14]
print("Test Case 5 pass")


#  python -m Test_Code.Test_Missing_Number
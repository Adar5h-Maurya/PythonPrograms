from Code.Palindrome_Number import check_palindrome

assert check_palindrome(121) == "Palindrome"
print("Test Case 1 pass")

assert check_palindrome(123) == "Not Palindrome"
print("Test Case 2 pass")

assert check_palindrome(111) == "Palindrome"
print("Test Case 3 pass")

assert check_palindrome(456) == "Not Palindrome"
print("Test Case 4 pass")

assert check_palindrome(1221) == "Palindrome"
print("Test Case 5 pass")

# python -m Test_Code.Test_Palindrome_Number
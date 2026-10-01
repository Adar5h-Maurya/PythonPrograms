from Code.Palindrome_String import check_palindrome

assert check_palindrome("madam") == "Palindrome"
print("Test Case 1 pass")

assert check_palindrome("hello") == "Not Palindrome"
print("Test Case 2 pass")

assert check_palindrome("level") == "Palindrome"
print("Test Case 3 pass")

assert check_palindrome("python") == "Not Palindrome"
print("Test Case 4 pass")

assert check_palindrome("radar") == "Palindrome"
print("Test Case 5 pass")


# python -m Test_Code.Test_Palindrome_String
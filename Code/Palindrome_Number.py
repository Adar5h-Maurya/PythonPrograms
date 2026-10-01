def check_palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if original == reverse:
        return "Palindrome"
    else:
        return "Not Palindrome"


# print(check_palindrome(123))
# print(check_palindrome(220022))
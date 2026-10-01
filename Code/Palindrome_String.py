def check_palindrome(text):
    reverse = ""

    for char in text:
        reverse = char + reverse

    if text == reverse:
        return "Palindrome"
    else:
        return "Not Palindrome"


# print(check_palindrome("nitin"))
# print(check_palindrome("Adarsh"))
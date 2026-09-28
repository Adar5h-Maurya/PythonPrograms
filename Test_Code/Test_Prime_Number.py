from Code.Prime_Number import check_prime

assert check_prime(7) == "Prime"
print("Test Case 1 pass")

assert check_prime(10) == "Not Prime"
print("Test Case 2 pass")

assert check_prime(13) == "Prime"
print("Test Case 3 pass")

assert check_prime(1) == "Not Prime"
print("Test Case 4 pass")

assert check_prime(20) == "Not Prime"
print("Test Case 5 pass")
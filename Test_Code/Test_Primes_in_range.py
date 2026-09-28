from Code.Primes_in_range import primes_in_range

assert primes_in_range(1, 10) == [2, 3, 5, 7]
print("Test Case 1 pass")

assert primes_in_range(10, 20) == [11, 13, 17, 19]
print("Test Case 2 pass")

assert primes_in_range(1, 5) == [2, 3, 5]
print("Test Case 3 pass")

assert primes_in_range(20, 30) == [23, 29]
print("Test Case 4 pass")

assert primes_in_range(1, 2) == [2]
print("Test Case 5 pass")
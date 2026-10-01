from Code.Vowels_Consonants import count_vowels_consonants

assert count_vowels_consonants("hello") == (2, 3)
print("Test Case 1 pass")

assert count_vowels_consonants("python") == (1, 5)
print("Test Case 2 pass")

assert count_vowels_consonants("apple") == (2, 3)
print("Test Case 3 pass")

assert count_vowels_consonants("HELLO") == (2, 3)
print("Test Case 4 pass")

assert count_vowels_consonants("education") == (5, 4)
print("Test Case 5 pass")

# python -m Test_Code.Test_Vowels_Consonants
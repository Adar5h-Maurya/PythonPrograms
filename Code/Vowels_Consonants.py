def count_vowels_consonants(text):
    vowels = 0
    consonants = 0

    for char in text:
        if char.isalpha():
            if char in "aeiouAEIOU":
                vowels = vowels + 1
            else:
                consonants = consonants + 1

    return vowels, consonants


# print(count_vowels_consonants("Adarsh"))
# print(count_vowels_consonants("Learning Python"))
from Code.Char_Frequency import char_frequency

assert char_frequency("hello") == {
    "h": 1,
    "e": 1,
    "l": 2,
    "o": 1
}
print("Test Case 1 pass")

assert char_frequency("aabbc") == {
    "a": 2,
    "b": 2,
    "c": 1
}
print("Test Case 2 pass")

assert char_frequency("apple") == {
    "a": 1,
    "p": 2,
    "l": 1,
    "e": 1
}
print("Test Case 3 pass")

assert char_frequency("aaa") == {
    "a": 3
}
print("Test Case 4 pass")

assert char_frequency("abc") == {
    "a": 1,
    "b": 1,
    "c": 1
}
print("Test Case 5 pass")
from Code.Word_Frequency import word_frequency

assert word_frequency("hello world hello") == {
    "hello": 2,
    "world": 1
}
print("Test Case 1 pass")

assert word_frequency("python is easy python") == {
    "python": 2,
    "is": 1,
    "easy": 1
}
print("Test Case 2 pass")

assert word_frequency("apple apple banana") == {
    "apple": 2,
    "banana": 1
}
print("Test Case 3 pass")

assert word_frequency("one two three") == {
    "one": 1,
    "two": 1,
    "three": 1
}
print("Test Case 4 pass")

assert word_frequency("cat dog cat dog cat") == {
    "cat": 3,
    "dog": 2
}
print("Test Case 5 pass")


# python -m Test_Code.Test_Word_Frequency
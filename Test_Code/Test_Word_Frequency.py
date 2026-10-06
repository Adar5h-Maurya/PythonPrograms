from Code.Word_Frequency import word_frequency


def test_word_frequency_1():
    assert word_frequency("hello world hello") == {
        "hello": 2,
        "world": 1
    }


def test_word_frequency_2():
    assert word_frequency("python is easy python") == {
        "python": 2,
        "is": 1,
        "easy": 1
    }


def test_word_frequency_3():
    assert word_frequency("apple apple banana") == {
        "apple": 2,
        "banana": 1
    }


def test_word_frequency_4():
    assert word_frequency("one two three") == {
        "one": 1,
        "two": 1,
        "three": 1
    }


def test_word_frequency_5():
    assert word_frequency("cat dog cat dog cat") == {
        "cat": 3,
        "dog": 2
    }

# python -m pytest .\Test_Code\Test_Word_Frequency.py
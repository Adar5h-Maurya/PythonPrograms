def word_frequency(sentence):
    words = sentence.split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] = frequency[word] + 1
        else:
            frequency[word] = 1

    return frequency


# print(word_frequency("hello world hello"))
# print(word_frequency("cat dog cat dog cat"))
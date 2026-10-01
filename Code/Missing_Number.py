def missing_number(numbers):
    missing = []

    for i in range(min(numbers), max(numbers) + 1):
        if i not in numbers:
            missing.append(i)

    return missing


# print(missing_number([1, 2, 3, 5]))
# print(missing_number([1, 2, 4, 5, 8, 9]))
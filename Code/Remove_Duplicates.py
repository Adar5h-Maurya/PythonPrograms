def remove_duplicates(numbers):
    result = []

    for num in numbers:
        if num not in result:
            result.append(num)

    return result

# print(remove_duplicates([1,2,3,2,2,3,1]))
# print(remove_duplicates([1,1,1,1,]))
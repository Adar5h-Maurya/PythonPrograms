def second_largest(numbers):
    largest = numbers[0]
    second = numbers[1]

    if second > largest:
        largest, second = second, largest

    for num in numbers[2:]:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second

# print(second_largest([10, 5, 20, 8]))
# print(second_largest([4, 15, 8, 12]))
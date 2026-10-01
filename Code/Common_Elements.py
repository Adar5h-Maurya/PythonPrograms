def common_elements(l1,l2):
    list1 = set(l1)
    list2 = set(l2)
    common = list1.intersection(list2)
    return list(common)


# print(common_elements([1, 2, 3], [2, 3, 4]))
# print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
x1 = [1, 2, 3, 2, 0]
x2 = [5, 1, 2, 7, 3, 2]


def intersection(list1, list2):
    result = []
    for i in range(len(list1)):
        if list1[i] in list2:
            result.append(list1[i])

    return sorted(result)


output = intersection(x1, x2)

print(output)
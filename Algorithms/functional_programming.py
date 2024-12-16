# Functional programming indeed

# Hint: определяем базовый случай и стараемся все свести к нему.
# Базовый случай для массивов часто оказывается пустой массив или массив из одного элемента.
# Если не знаешь с чего начать - начни с этого.

def array_sum(arr):
    """
    :param arr: array of numbers
    :return: numbers sum of array
    """
    if arr == []:
        return 0
    return arr[0] + array_sum(arr[1:])

#print(array_sum([1, 2, 3]))


def elements_count(arr):
    """
    :param arr: array of numbers
    :return: numbers count of array
    """
    if arr == []:
        return 0
    return 1 + elements_count(arr[1:])

#print(elements_count([1, 23, 3, 4, 3, 4, 1123, 2, 3]))


def find_biggest_number(arr):
    """
    :param arr: array of number
    :return: biggest number in array
    """
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = find_biggest_number(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

print(find_biggest_number([1, 2, 12, 31, 2]))
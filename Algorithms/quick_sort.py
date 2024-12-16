# Quick Sort

def quick_sort(arr):
    """
    :param arr: array of number
    :return: sorted array
    """
    if len(arr) < 2:  # Базовый случай
        return arr
    else:   # Рекурсивный случай
        pivot = arr[0]  # Выбираем любой опорный элемент (в данном случае первый)
        less = [i for i in arr[1:] if pivot > i]    # Подмассив чисел, меньших чем опорный
        greater = [i for i in arr[1:] if pivot < i] # Подмассив чисел, больщих чем опорный
        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([1, 4, 2, 6, 10, 9, 3]))
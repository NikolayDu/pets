# Binary Search
# Complexity: 0(log N)

def binary_search(array, value):
    """
    :param array: array of numbers
    :param value: number which needs to find
    :return: index of number if there is a number or None if there is no value in array
    """
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        guess = array[mid]
        if guess == value:
            return mid
        elif guess < value:
            start = mid + 1
        else:
            end = mid - 1
    return None

#print(binary_search([1, 2, 3, 4, 5, 6], 5))
#print(binary_search(list(range(101)), 250))

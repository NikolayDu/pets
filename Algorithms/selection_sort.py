# Selection Sort

# Sample: sort by ascending numbers
# Complexity: 0(n^2)

def find_smallest(arr):
    """
    :param arr: array of numbers
    :return: smallets number index of array
    """
    smallest_num = arr[0]
    smallest_num_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest_num:
            smallest_num = arr[i]
            smallest_num_index = i
    return smallest_num_index

def sort_array(arr):
    """
    :param arr: array of numbers
    :return: array sort by ascending numbers
    """
    new_arr = []
    for i in range(len(arr)):
        smallest_index_of_num = find_smallest(arr)
        new_arr.append(arr.pop(smallest_index_of_num))
    return new_arr

if __name__ == "__main__":

    test_array1 = [0, 5, 7, 12, 99, 23, 4]
    test_array2 = [.2, 6.4, .5, 10.0, 4.2, 3.3, .1]

    # print(sort_array(test_array1))
    # print(sort_array(test_array2))

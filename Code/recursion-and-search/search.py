#!python


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if array[index] == item:
        return index
    elif index + 1 >= len(array):
        return None
    else:
        return linear_search_recursive(array, item, index+1)

    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    array = sorted(array)
    half_arr = int(len(array)/2)
    if half_arr > item:
        for i in range(0, half_arr):
            if array[i] == item:
                return i
    if half_arr < item:
        for i in range(half_arr, len(array)):
            if array[i] == item:
                return i
    else:
        print("Error")
    # TODO: implement binary search iteratively here
    pass
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    array = sorted(array)

    if left or right is None:
        left = 0
        right = len(array) - 1

    half_arr = (left + right)//2
    if array[half_arr] == item:
        return half_arr
    elif array[half_arr] < item:
        left = half_arr + 1
    else:
        right = half_arr - 1

    return binary_search_recursive(array, item, left, right)
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests


def test():
    arr = [1, 2, 4, 3, 8, 6, 7, 5, 9]
    print(linear_search_iterative(arr, 9))
    print(binary_search_iterative(arr, 2))
    print(binary_search_recursive(arr, 2))


if __name__ == "__main__":
    test()


"""
file name: bsearch.py
The below program named auto-complete.py implements a auto-complete system.
This system will suggest a word based on the entered prefix.


"""


def binSearchRecursive(data: list, val, left: int, right: int):
    """
    The recursive binary search function.
    :param data: list of data
    :param val: the value to search for
    :param left: the starting index in data
    :param right: the ending index in data
    :return: The index of the first occurrence of the value, if present,
        -1 otherwise.
    """

    if left > right:
        return -1

    if data[left].startswith(val):
        return left

    midindex = (left + right) // 2
    if data[midindex].startswith(val):
        return binSearchRecursive(data, val, left, midindex)

    if data[midindex] > val:
        return binSearchRecursive(data, val, left, midindex - 1)
    else:
        return binSearchRecursive(data, val, midindex + 1, right)


def binarySearch(data: list, val: int) -> int:
    """
    The main binary search function, which calls the recursive helper
    function to do the actual search.
    :param data: A list of data
    :param val: The value to search for
    :return: The index of the first occurrence of the value, if present,
        -1 otherwise.
    """
    return binSearchRecursive(data, val, 0, len(data) - 1)

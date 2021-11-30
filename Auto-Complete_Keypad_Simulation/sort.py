
"""
file name: sort.py
The below program named auto-complete.py implements a auto-complete system.
This system will suggest a word based on the entered prefix.


"""


def findMinIndex(data: list, mark: int) -> int:
    """
    A helper routine for selectionSort which finds the index
    of the smallest value in data at the mark index or greater.
    :param data: a list of data
    :param mark: an index which is in range 0..len(data)-1 inclusive
    :return: An index which is in range 0..len(data)-1 inclusive
    """

    minIndex = mark
    for mark in range(mark + 1, len(data)):
        if data[mark] < data[minIndex]:
            minIndex = mark
    return minIndex


def selectionSort(data: list) -> None:

    """
    Perform an in-place selection sort of data.
    :param data: The data to be sorted (a list)
    :return: None
    """
    for mark in range(len(data) - 1):
        minIndex = findMinIndex(data, mark)
        data[mark], data[minIndex] = data[minIndex], data[mark]

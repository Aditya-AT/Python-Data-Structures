from bsearch import *
from sort import *
import sys

"""
file name: auto-complete.py

The below program named auto-complete.py implements a auto-complete system.
This system will suggest a word based on the entered prefix.

imported libraries:
a. bsearch.py
b. sort.py
c. sys

"""

# word list
list_of_Words = []


def wordsList(file):
    """
    This function reads from file and stores all the list of words extracted from the file test.dic
    in a list named list_of_Words.

    :param: file
    :return: None

    """

    with open(file) as scanner:
        lines = scanner.readlines()
        for line in lines:
            word = line.strip()
            list_of_Words.append(word.lower())


def findLastIndex(data: list, val):
    """
    This function finds the last occurance of the prefix to be searched.

    :param: data: list, val
    :return: index of last occurance of the user's specified prefix: int.

    """

    # subSetData consists words begining with first occurance of the prefix till the end of the list.
    subsetData = data[binarySearch(list_of_Words, val):]

    for index in range(len(subsetData)):
        if not subsetData[index].startswith(val):
            return binarySearch(list_of_Words, val) + index - 1
        elif subsetData[index] == list_of_Words[-1]:
            return list_of_Words.index(subsetData[index])


def autoWords(data: list, prefix):
    """
    This function returns list of matched words based on user's specified prefix.

    :param: data: list, prefix: str
    :return: list of mateched words

    """

    if findLastIndex(list_of_Words, prefix) is None:
        autoMatchedWords = list_of_Words[binarySearch(list_of_Words, prefix):]
        return autoMatchedWords

    else:
        autoMatchedWords = list_of_Words[binarySearch(list_of_Words, prefix):findLastIndex(list_of_Words, prefix) + 1]
        return autoMatchedWords


def main():

    """
    General Idea/Logic:
    1. Reads the words from the file test.dic and stores them in a list.
    2. Sorts the list in ascending order using selection sort.
    3. Takes prefix as input from the user and passes it to associated functions to check if the occurance exists and
    returns a list of matched words.
    4. Then, asks the user in a repeated loop for a prefix to auto-complete.
    5. Once a prefix is given to the program it prints the first match.
    6. If the same prefix is specified again by the user, then it prints the next valid word.
    7.  If the user enters the empty string,the autocomplete system will
    use the previously entered prefix but suggest the next valid word.
    8. However if the first entered prefix is an empty string or in other words there is no previously entered prefix,
    then the system will show all the words in the dictionary one by one in a repeating pattern.
    9. If the user enters an invalid word, then it prints out No match.



    """

    # reading file name from argument
    wordsList(sys.argv[1])

    # using selection sort to sort the list: imported sort.py
    selectionSort(list_of_Words)
    print('The sorted list:', list_of_Words)
    print('Welcome to Auto-Complete!')
    print('Enter <QUIT> to exit.')

    # taking input from user
    prefix = input('Enter a prefix to search for:')
    lastWord = prefix

    # looping until user wants to exit from the main program by entering <QUIT>
    while prefix != "<QUIT>":

        # if user enters invalid input, propmt to enter again
        if binarySearch(list_of_Words, prefix) == -1:
            print('No match')
            prefix = input('Enter a prefix to search for:')

        #  if user enters a valid input
        else:
            words = autoWords(list_of_Words, prefix)
            print(words[0])
            prefix = input('Enter a prefix to search for:')

            # lowerLimit,upperLimit: start and end index of the matchedWords list
            lowerLimit = binarySearch(list_of_Words, lastWord)
            upperLimit = findLastIndex(list_of_Words, lastWord)

            # if user enters a word which was just entered before or enters an empty string, then return the next valid word
            listTemp = list_of_Words[lowerLimit:upperLimit + 1]
            counterTemp = 1
            while prefix == lastWord or prefix == '':
                if len(listTemp) != 1:
                    print(listTemp[counterTemp])
                    counterTemp += 1
                    if counterTemp == len(listTemp):
                        counterTemp = 0
                else:
                    print(listTemp[0])
                prefix = input('Enter a prefix to search for:')
            # if user enters a different word, then its set the lastWord variable to new entered prefix
            if prefix != '':
                lastWord = prefix
    print('Exiting Auto-complete! Good bye.')
    exit()


# main conditional guard
if __name__ == '__main__':
    main()

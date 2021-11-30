import sys

"""
file name: spellfixer.py
Authors:
1. Aniket Narendra Patil (ap8504@rit.edu)
2. Aditya Ajit Tirakannavar (at2650@rit.edu)

CSCI-603 Computational Problem Solving
Lab 4 : The below program named spellfixer.py reads text from the standard input.
The program corrects text input errors that occur because a user's
finger accidentally hit a key adjacent to the intended one instead of the intended one.
Besides the above requirements, the program also implements the spelling
corrections as mentioned below:
a. Transpose two adjacent letters (e.g. assingment --> assignment)
b. Remove a letter (e.g. lettter --> letter)

imported libraries:
a. sys

"""

# word list set
list_of_Words = set()

# dictionary for adjacent keys
adjecent_keys = {}


def words_list(file):
    """
    This function reads from file and stores all the list of words extracted from the file in a set named list_of_Words.

    :param: file
    :return: None

    """

    with open(file) as words:
        lines = words.readlines()
        for line in lines:
            words = line.strip()
            list_of_Words.add(words.lower())


def adjecent_letters(file):
    """
    This function is used to read from file and store the key mapping for a particular key on the keyboard in a
    dictionary.
    The key is a single charcter or key on the keyboard and the value is the list of adjacent keys.

    :param: file
    :return: None

    """

    with open(file) as f:
        content = f.readlines()
        for line in content:
            words = line.strip()
            data = words.split(" ")

            # the letters after the first one
            sub = data[1:]

            # the first letter is the key,
            # the rest are the values
            adjecent_keys[data[0].lower()] = sub


def adjecent_correction(input):
    """
    Find if the input is in the dictionary, or if the input is
    a slippery finger error and then corrects the input
    according to the dictionary.

    :param  user input
    :return: mutable.__str__(): the string representation of the corrected word
    :return: input: the original user input
    """

    # if the input is in the word_list
    if input in list_of_Words:
        return input + " "

    elif input not in list_of_Words:

        # loop through each character in the word
        for i in range(len(input)):

            # if the letter is in the adjacent key dictionary
            if input[i] in adjecent_keys.keys():

                for adjletter in adjecent_keys[input[i].lower()]:
                    s = input[:i] + adjletter + input[i + 1:]

                    if s.lower() in list_of_Words:
                        return s + " "

    return input + ' '


def transpose_correction(input):
    """
    This function is used to fix the transpose errors that occur in a given word.
    For example: (e.g. assingment --> assignment).
    The above is acheived by replacing/transposing the charcters at specified index and checking if new word formed is legal.
    If the word is found to be legal, then it returns the legal word else it returns the input.

    :param: word
    :return: transpose corrected word or input word

    """

    if input not in list_of_Words:
        newList = []
        copyList = []

        for letter in input:
            newList.append(letter)
            copyList.append(letter)

        for i in range(1, len(newList)):
            newList[i - 1], newList[i] = newList[i], newList[i - 1]
            str1 = ''.join(newList)
            # print(str1)
            if str1 in list_of_Words:
                newList = [i for i in copyList]
                return str1 + ' '
            newList = [i for i in copyList]

    return input + ' '


def remove_extra_letter(input):
    """
    This function is used to remove any extra letter or character that was mistakenly added in a given word.
    For example:  (e.g. lettter --> letter)
    The above is acheived by removing one charcter from every index and checking if the new word is legal.
    If the word is found to be legal, then it returns the legal word else it returns the input.

    :param: word
    :return: extra character corrected word or input word

    """

    if input not in list_of_Words:

        new_list = []
        copy_list = []
        for letter in input:
            new_list.append(letter)
            copy_list.append(letter)

        for i in range(0, len(new_list)):
            new_list.pop(i)
            str2 = ''.join(new_list)
            # print(str2)
            if str2 in list_of_Words:
                new_list = [i for i in copy_list]
                return str2 + " "
            new_list = [i for i in copy_list]

    return input + ' '


def main():
    """
    Entry point for program execution.
    1. Firstly, Reads two (2) files as mentioned below:
    a. A dictionary containing set of all words in English language
    and stores the words extracted in a set named list_of_Words.
    b. Keyboard mapping data indicating the charcters (keys) adjacent to any selected character (key)
    and stores the characters (keys) extracted in a dictionary named adjecent_keys
    2. Secondly, prompts the user to enter the sentence and then splits the sentence based on whitespaces
    to store the sentence word by word in a list named sentence_to_words.
    3. Thirdly, for every word in sentence_to_words it checks if there exists any adjecent_correction
    or transpose_correction or remove_extra_letter correction as mentioned in respective method description.
    4. If any error is found in the word, then that word is corrected based on the guts of the above mentioned functions
    and returned back to the user through a string named correct_sentence.
    5. If no errors are found or the word cannot be fixed
    then that word is simply returned and appended to the string named correct_sentence.
    6. If user enters !*!, then the program exits and prints Bye!.

    :param input: user input
    :return: None

    """

    words_list(sys.argv[1])
    adjecent_letters(sys.argv[2])

    sentence = input('Write: \n')

    while (sentence != '!*!'):

        correct_sentence = ''
        correct_sentence2 = ''
        correct_sentence3 = ''
        for word in sentence.split():
            word = word.strip(".,?!:;'")
            correct_sentence += adjecent_correction(word)

        for w in correct_sentence.split():
            correct_sentence2 += transpose_correction(w)

        for k in correct_sentence2.split():
            correct_sentence3 += remove_extra_letter(k)

        if sentence[-1] == '.' or sentence[-1] == '!' or sentence[-1] == '?' or sentence[-1] == ',':
            print(correct_sentence3 + sentence[-1])
        else:
            print(correct_sentence3)
        sentence = input('Write: \n')
    print('Bye!')


# main conditional guard
if __name__ == "__main__":
    main()

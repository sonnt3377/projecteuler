"""
    Project Euler 42: Coded triangle numbers

    The nth term of the sequence of triangle numbers is given by, tn = 1/2n(n+1); so the first ten triangle numbers are:
    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    By converting each letter in a word to a number corresponding to its alphabetical position and adding these values
    we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
    If the word value is a triangle number then we shall call the word a triangle word.

    Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
    English words, how many are triangle words?
"""
import time

# List of English alphabet letters. the letter position's is its value
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def generate_triangle_number_list(number):
    """
    Generate a list containing triangle numbers
    :param number: the number of items in the list
    :return: the list
    """
    list1 = []
    for i in range(number):
        list1.append((i + 1) * (i + 2) / 2)

    return list1


def is_triangle_word(word, triangle_number_list):
    """
    Check if a word is a triangle word

    :param word: input word to check
    :param triangle_number_list:

    :return: True of the word is a triangle word, False otherwise
    """
    value = 0

    # Calculate value of the word
    for letter in word:
        value += letters.index(letter) + 1

    return value in triangle_number_list


def get_words_from_file(file_name):
    """
    Read input data from file, and return a list containing all words

    :param file_name: input data file
    :return: list of words
    """
    f = open(file_name)
    word_list = f.read().replace('\"', '').split(",")

    return word_list


def main():
    start_time = time.time()

    result = 0
    word_list = get_words_from_file("project_euler_42.txt")

    # This triangle number list is long enough to contains all possible situations
    triangle_number_list = generate_triangle_number_list(20)

    for word in word_list:
        if is_triangle_word(word, triangle_number_list):
            result += 1

    print("The result is {0}, found in {1} seconds".format(result, time.time() - start_time))


if __name__ == "__main__":
    main()

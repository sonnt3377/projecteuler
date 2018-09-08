"""
    Project Euler 24: Lexicographic permutations

    A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits
    1, 2, 3 and 4.
    If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.

    The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import time
import math

INPUT_NUMBER = 1000000


def find_the_right_permutation(number):
    """
    Loop through permutations to find the 1000000th position

    :param number:
    :return: a string at the 1000000th position
    """
    result_string = ""
    digit_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    list_length = len(digit_list)

    # With the loop, we find the first digit of that string, then the second digit, and so on.
    for i in range(list_length):
        # Number of permutations of the remaining (9 - i) digits
        no_of_permutations = math.factorial(list_length - 1 - i)
        # Finding index-i digit so that the number is less than 1000000
        quotient = number // no_of_permutations
        # Remaining part for subsequent digits
        remainder = number % no_of_permutations
        number = remainder

        result_string += str(digit_list[quotient])
        # This digit is already used and cannot be used again.
        del digit_list[quotient]

    return result_string


def main():
    """
    Test function
    """
    start_time = time.time()
    result = find_the_right_permutation(INPUT_NUMBER - 1)
    print("Result is: {0}, found in {1} seconds".format(result, time.time() - start_time))


if __name__ == "__main__":
    main()

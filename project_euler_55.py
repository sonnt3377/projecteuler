"""
    Project Euler 55: Lychrel numbers
        If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

        Not all numbers produce palindromes so quickly. For example,

        349 + 943 = 1292,
        1292 + 2921 = 4213
        4213 + 3124 = 7337

        That is, 349 took three iterations to arrive at a palindrome.

        Although no one has proved it yet, it is thought that some numbers, like 196,
        never produce a palindrome. A number that never forms a palindrome through the
        reverse and add process is called a Lychrel number. Due to the theoretical nature
        of these numbers, and for the purpose of this problem, we shall assume that a number
        is Lychrel until proven otherwise. In addition you are given that for every number
        below ten-thousand, it will either (i) become a palindrome in less than fifty
        iterations, or, (ii) no one, with all the computing power that exists, has managed so
        far to map it to a palindrome. In fact, 10677 is the first number to be shown to
        require over fifty iterations before producing a palindrome:
        4668731596684224866951378664 (53 iterations, 28-digits).

        Surprisingly, there are palindromic numbers that are themselves Lychrel numbers;
        the first example is 4994.

        How many Lychrel numbers are there below ten-thousand?

        NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical
        nature of Lychrel numbers.
"""
import time
from project_euler import is_palindrome_base_10


def is_lychrel_number(number):
    """
    Check if a number is a Lychrel number by checking for palindrome up to 50 iterations

    :param number: the number to be checked
    :return: True if the number is Lychrel, False otherwise
    """
    the_sum = number
    # Iterate up to 50 times
    for _ in range(1, 50):
        original = the_sum
        inversed = int(str(original)[::-1])
        the_sum = original + inversed

        if is_palindrome_base_10(the_sum):
            return False

    # This is a Lychrel number, concluded by exhaustive search (uo to 50 iterations)
    return True


def count_lychrel_number(limit):
    """
    Count the number of Lychrel numbers less than the limit

    :param limit: the upper bound
    :return: the number of Lychrel number below the limit
    """
    count = 0

    for i in range(1, limit + 1):
        if is_lychrel_number(i):
            count += 1

    return count


def main():
    """
    Test
    """
    start_time = time.time()
    result = count_lychrel_number(10000)
    print("The result is {0}, found in {1} seconds.".format(result, time.time() - start_time))


if __name__ == "__main__":
    main()

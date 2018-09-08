"""
    Project Euler 36: Double-base palindromes

    The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

    Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

    (Please note that the palindromic number, in either base, may not include leading zeros.)
"""
import time
import project_euler

def find_sum(limit):
    """
    Find sum of all numbers less than a limit, which are palindromic in both base 10 and base 2

    :param limit: the upper limit
    :return: the sum
    """
    the_sum = 0

    for i in range(limit):
        if project_euler.is_palindrome_base_10(i) and project_euler.is_palindrome_base_2(i):
            the_sum += i

    return the_sum


def main():
    """
    Test method
    """
    input_numer = 1000000

    start_time = time.time()
    result = find_sum(input_numer)
    print("Result is {0}, found in {1} seconds".format(result, time.time() - start_time))


if __name__ == "__main__":
    main()

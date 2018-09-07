"""
    Project Euler 4: Largest palindrome product

    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
    is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time
import itertools


def brute_force_search():
    """
    Finding the largest palindromes with brute force

    :return: the largest palindrome, and two numbers which form that palindrome
    """
    largest_palindrome = 0
    number1 = 0
    number2 = 0

    for i, j in itertools.product(range(100, 1000), range(100, 1000)):
        product = i * j
        # If a larger palindrome is found
        if str(product) == str(product)[::-1] and product > largest_palindrome:
            largest_palindrome = product
            number1 = i
            number2 = j

    return largest_palindrome, number1, number2


def reverse_search():
    """
    Search from larger number down to smaller ones and stop when we found a palindrome.
    This approach may reduce the search space.

    :return: the largest palindrome, and two numbers which form that palindrome
    """

    palindrome = 0
    number1 = 0
    number2 = 0
    is_result_found = False

    # As the product number is a palindrome, it can be formed by mirroring half of the string representing that number
    # i represents the first half of the palindrome
    for i in range(999, 100, -1):
        # Make the palindrome out of that number
        palindrome = int(str(i) + str(i)[::-1])
        # Find the numbers, that create the palindrome, if exists
        for j in range(999, 100, -1):
            # The numbers cannot be larger than 999
            # Only need to search up to the square root of the palindrome, instead of the whole range
            if (palindrome // j) > 999 or (j * j < palindrome):
                break

            # If the numbers are found
            if palindrome % j == 0:
                is_result_found = True
                number1 = j
                number2 = palindrome // j
                break

        if is_result_found:
            break

    return palindrome, number1, number2


def main():
    """
    Test function
    """
    # Brute force search
    start_time = time.time()
    result = brute_force_search()
    print("Brute force search: the palindrome is {0}, made of {1} and {2}. Result found in {3} seconds".
          format(result[0], result[1], result[2], time.time() - start_time))

    # Reverse search
    start_time = time.time()
    result = reverse_search()
    print("Reverse search: the palindrome is {0}, made of {1} and {2}. Result found in {3} seconds".
          format(result[0], result[1], result[2], time.time() - start_time))


if __name__ == "__main__":
    main()

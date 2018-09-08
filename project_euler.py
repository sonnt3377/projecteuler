"""
    Contain some common methods that are used again and again in different problem
"""
import math


def sieve(upper_limit, lower_limit=0):
    """
    Generating a list of prime numbers between the two bounds using sieving.
    If the lower limit is omitted, then the method generate list of primes less than
    the upper bound

    :param lower_limit:
    :param upper_limit:
    :return: the prime list
    """
    # A boolean list, each index indicates a corresponding number, the value in that
    # index is True if that number is prime, and False otherwise
    primes = [True] * upper_limit

    # 0 and 1 are not primes
    primes[0], primes[1] = [False] * 2

    for index, value in enumerate(primes):
        # The first number with True is a prime, but the multiples of it are not
        if value:
            primes[index * 2::index] = [False] * (((upper_limit - 1) // index) - 1)

    # The "primes" list above contains all numbers from 0 to upper_limit
    # We only need primes from lower_limit to upper_limit
    prime_list = [i for i in range(lower_limit, upper_limit) if primes[i]]

    return prime_list


def is_prime(number):
    """
    Check if a number is a prime

    :param number: input number
    :return: return True if the number is prime, and False otherwise
    """
    # 1 is not a prime
    if number == 1:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


def is_circular_prime(number):
    """
    Check if a number is a circular prime

    :param number: input number
    :return: True if the number is a circular prime, False otherwise
    """
    number_string = str(number)

    for i in range(len(number_string)):
        if not is_prime(int(number_string[i + 1:] + number_string[:i + 1])):
            return False

    return True


def is_palindrome_base_10(number):
    """
    Check if a number is a palindrome in base 10

    :param number: input number
    :return: True if the number is a palindrome, and False otherwise
    """
    if str(number) == str(number)[::-1]:
        return True

    return False


def is_palindrome_base_2(number):
    """
    Check if a number in base 10 is a palindrome in base 2

    :param number: input number in base 10
    :return: True if the number is a palindrome in base 2, and False otherwise
    """
    # Convert to binary, and remove the '0b' prefix
    binary_representation = bin(number)[2:]

    if binary_representation == binary_representation[::-1]:
        return True

    return False


def is_9_digit_pandigital(*numbers):
    """
    Decide if a list of numbers, when concatenating to each other, create a 9-digit
    pandigital

    :param numbers: list of numbers to test
    :return: True if the concatenating of numbers create a pandigital, False otherwise
    """
    test_string = ""
    digit_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for number in numbers:
        test_string += str(number)

    # The string is not pandigital if it contains 0 or if it has more than 9 digits
    if len(test_string) != 9 or '0' in test_string:
        return False

    # The string is pandigital if each digit from 1 to 9 appears only once
    return all(digit in test_string for digit in digit_list)


def is_pandigital(number):
    """
    Check if the number is a pandigital

    :param number: input number
    :return: True if the number is a pandigital, and False otherwise
    """
    test_string = str(number)
    digit_list = [str(i) for i in range(1, len(test_string) + 1)]

    # The string is pandigital if each digit appears only once
    return all(digit in test_string for digit in digit_list)


def is_pentagonal(number):
    """
    Check if an integer is a pentagon
    Ref: https://en.wikipedia.org/wiki/Pentagonal_number#Tests_for_pentagonal_numbers

    :param n: number to check
    :return: True if the number is pentagonal, False otherwise.
    """
    test = (math.sqrt(24 * number + 1) + 1) / 6
    return test == int(test)

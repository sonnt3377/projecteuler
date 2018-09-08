"""
    Contain some common methods that are used again and again in different problem
"""
import math


def sieve(number):
    """
    Finding a list of primes less than a number using sieving

    :param number: the upper bound number, that all primes need to be less than or equal
    :return: list containing all primes less than the limit
    """
    # A boolean list, each index indicates a corresponding number, the value in that index is True if that number is prime, and False otherwise
    primes = [True] * number

    # 0 and 1 are not primes
    primes[0], primes[1] = [False] * 2

    for index, value in enumerate(primes):
        # The first number with True is a prime, but the multiples of it are not
        if value is True:
            primes[index * 2::index] = [False] * (((number - 1) // index) - 1)

    prime_list = [i for i in range(number) if primes[i]]

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


def is_pandigital(n):
    """
    Check if the number is a pandigital

    :param n: input number
    :return: True if the number is a pandigital, and False otherwise
    """
    test_string = str(n)
    digit_list = [str(i) for i in range(1, len(test_string) + 1)]

    # The string is pandigital if each digit appears only once
    return all(digit in test_string for digit in digit_list)
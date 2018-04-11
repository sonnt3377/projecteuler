"""
    Project Euler 47: Distinct primes factors

    The first two consecutive numbers to have two distinct prime factors are:

    14 = 2 * 7
    15 = 3 * 5

    The first three consecutive numbers to have three distinct prime factors are:

    644 = 2^2 * 7 * 23
    645 = 3 * 5 * 43
    646 = 2 * 17 * 19.

    Find the first four consecutive integers to have four distinct prime factors each. What is the first of these
    numbers?
"""
import time


def find_prime_numbers_with_sieving(limit):
    """
    Find all prime numbers less than a limit using sieving.
    We use the same approach as in Project Euler 35.

    :param limit: the upper bound number
    :return: list containing all primes less than the limit
    """
    # A boolean list, with index indicating number, value in that index is True if that number is prime, and False
    # otherwise
    primes = [True] * limit
    # 0 and 1 are not prime
    primes[0], primes[1] = [False] * 2

    for index, value in enumerate(primes):
        # The first number with True is a prime, but the multiples of it are not
        if value is True:
            primes[index * 2::index] = [False] * (((limit - 1) // index) - 1)

    prime_list = [i for i in range(limit) if primes[i]]

    return prime_list


def get_no_of_prime_factors(number, prime_list):
    """
    Get the number of prime factors for the input number.
    For example, if the input number is 644 = 2^2 * 7 * 23, then the number of prime factors is 3 i.e. the prime factors
    are 2, 7, and 23

    :param number: input number
    :param prime_list: list of prime numbers

    :return: the number of prime factors
    """
    is_prime_factor = False
    remainder = number
    number_of_prime_factors = 0

    # Continuously factoring the number to prime factors, starting from the minimum prime number
    for prime_number in prime_list:
        # Continuously divided the number by a prime number, until it is not possible
        while remainder % prime_number == 0:
            is_prime_factor = True
            remainder /= prime_number

        # Then we move to the next prime number, and count the previous prime factor
        if is_prime_factor:
            number_of_prime_factors += 1
            # Reset flag, starting new prime factor
            is_prime_factor = False

        # The factorization is done when the remainder is 1
        if remainder == 1:
            break

    return number_of_prime_factors


def find_4_integers():
    """
    Find 4 consecutive integers, each with 4 distinct prime factors

    :return: 4 consecutive integers
    """

    # This prime list needs to be long enough because it contains all primes that are tested.
    # If the list is not long enough, the result found may be larger than it supposed to be, because the algorithm needs
    # to for a larger range in order to find those have factors in a limited prime space.
    prime_list = find_prime_numbers_with_sieving(1000)

    # The number of consecutive integers satisfying the condition
    number_of_consecutive_integers = 1
    number_of_required_prime_factors = 4
    number_of_required_integers = 4
    # The first number with four prime factors. We start from here
    start_number = 2 * 3 * 5 * 7

    # Run until we find 4 integers satisfying the condition
    while number_of_consecutive_integers < number_of_required_integers:
        start_number += 1
        if get_no_of_prime_factors(start_number, prime_list) == number_of_required_prime_factors:
            number_of_consecutive_integers += 1
        else:
            number_of_consecutive_integers = 0

    return start_number - 3


def main():
    start_time = time.time()
    result = find_4_integers()
    print("The result is {0}, found in {1} seconds".format(result, time.time() - start_time))


if __name__ == "__main__":
    main()

"""
    Project Euler 35: Circular primes

    The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are
    themselves prime.

    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

    How many circular primes are there below one million?
"""
import math
import time


def is_prime(number):
    """
    Check if a number is a prime

    :param number: input number
    :return: return True if the number is prime, and False otherwise
    """
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


def find_prime_numbers(limit):
    """
    Find all prime numbers less than the limit

    :param limit: upper limit
    :return: a list, containing all prime numbers less than the limit.
    """
    prime_list = []

    for i in range(2, limit):
        if is_prime(i):
            prime_list.append(i)

    return prime_list


# This approach is similar to that in Project Euler 27
def find_prime_numbers_with_sieving(limit):
    """
    Find all prime numbers less than a limit using sieving

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


def find_circular_primes(limit):
    """
    Find the number of circular prime less than the limit

    :param limit: upper bound
    :return: the number of circular primes less than the upper bound
    """
    prime_list = find_prime_numbers(limit)

    circular_prime_list = [i for i in prime_list if is_circular_prime(i)]

    return len(circular_prime_list)


def find_circular_primes_with_sieving(limit):
    """
    Find the number of circular prime less than the limit using sieving

    :param limit: upper bound
    :return: the number of circular primes less than the upper bound
    """
    prime_list = find_prime_numbers_with_sieving(limit)

    circular_prime_list = [i for i in prime_list if is_circular_prime(i)]

    return len(circular_prime_list)


def main():
    input_number = 1000000

    # Test sieving method
    start_time = time.time()
    result = find_circular_primes_with_sieving(input_number)
    print("Result is {0} found in {1} seconds".format(result, time.time() - start_time))

    # Test non-sieving method
    start_time = time.time()
    result = find_circular_primes(input_number)
    print("Result is {0} found in {1} seconds".format(result, time.time() - start_time))


if __name__ == "__main__":
    main()

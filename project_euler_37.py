"""
    Project Euler 37: Truncatable primes

    The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from
    left to right, and remain prime at each stage: 3797, 797, 97, and 7.
    Similarly we can work from right to left: 3797, 379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
import math
import time

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

# This approach is similar to that in Project Euler 27 and 35
def find_prime_numbers_with_sieving(limit):
    """
    Find all prime numbers less than a limit using sieving, except 2, 3, 5, 7

    :param limit: the upper bound number
    :return: list containing all primes less than the limit
    """
    # A boolean list, with index indicating number, value in that index is True if that number is prime, and False otherwise
    primes = [True] * limit
    # 0 and 1 are not prime
    primes[0], primes[1] = [False] * 2

    for index, value in enumerate(primes):
        # The first number with True is a prime, but the multiples of it are not
        if value is True:
            primes[index * 2::index] = [False] * (((limit - 1) // index) - 1)

    prime_list = [i for i in range(limit) if primes[i] == True]

    # Return prime list, except 2, 3, 5, 7
    return prime_list[4:]

def is_truncatable_prime(number):
    """
    Decide if a number is a truncatable prime

    :param number: input number
    :return: True if the number is a truncatable, and False otherwise
    """

    for i in range(1, len(str(number))):
        # Check if the number is NOT right truncatable
        if not is_prime(int(str(number)[:i])):
            return False
        # Check if the number is NOT left truncatable
        if not is_prime(int(str(number)[-i:])):
            return False

    # The number is truncatable
    return True

def sum_truncatable_primes():
    """
    Find the sum of all 11 truncatable primes

    :return: the sum
    """
    # NOTE: instead of searching for all prime numbers, and stop when we find the 11th truncatable prime, we define
    # the search space and hope that we will find all 11 truncatable primes in that space, if not, we increase the
    # the search space.
    # There is no guarantee that a certain search space contains all the numbers, but with a define search space, we
    # can use sieving to find all primes in such space, with faster speed.
    SEARCH_LIMIT = 1000000
    prime_list = find_prime_numbers_with_sieving(SEARCH_LIMIT)
    sum = 0
    counter = 0

    for prime_number in prime_list:
        if is_truncatable_prime(prime_number):
            print("The truncatable prime is {0}".format(prime_number))
            sum += prime_number
            counter += 1
        # Found all 11 required prime, no need to check for more.
        if counter == 11:
            break

    return sum

def main():
    start_time = time.time()
    result = sum_truncatable_primes()
    print("Result is {0}, found in {1} seconds".format(result, time.time() - start_time))

if __name__ == "__main__":
    main()
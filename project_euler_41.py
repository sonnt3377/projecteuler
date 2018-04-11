"""
    Project Euler 41: Pandigital prime

    We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
    For example, 2143 is a 4-digit pandigital and is also prime.

    What is the largest n-digit pandigital prime that exists?
"""
import time


# This approach is similar to that used in Project Euler 35
def find_prime_numbers_with_sieving(limit):
    """
    Find all prime numbers less than a limit using sieving

    :param limit: the upper bound number
    :return: list containing all primes less than the limit
    """
    # A boolean list, with index indicating number, value in that index is True if that number is prime,
    # and False otherwise
    primes = [True] * limit
    # 0 and 1 are not prime
    primes[0], primes[1] = [False] * 2

    for index, value in enumerate(primes):
        # The first number with True is a prime, but the multiples of it are not
        if value is True:
            primes[index * 2::index] = [False] * (((limit - 1) // index) - 1)

    prime_list = [i for i in range(limit) if primes[i]]

    return prime_list


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


def find_max_pandigital_prime(limit):
    """
    Find the largest n-digit pandigital prime that less than limit

    :param limit: the limit number
    :return: the largest pandigital prime less than limit
    """
    prime_list = find_prime_numbers_with_sieving(limit)

    # Counting from the largest prime number down, until we find a number that is a pandigital
    for i in reversed(prime_list):
        if is_pandigital(i):
            return i


"""
    Analysis:
    A n-digit pandigital number will have a form 123...n or the permutation of that. However, the number of digits will
    be the same.
    In addition, to be a pandigital, a number cannot have more than 9 digits, because there will be duplicate(s)
    otherwise
    So a 9-digit pandigital (if exists) contains all digits from 1 to 9, and the sum of the digits = 45. This number is
    divisible by 3 or 9, meaning that those pandigital numbers are not prime
    Similarly, a 8-digit pandigital (if exists) will not be a prime.
    A 7-digit pandigital (if exists) contains all digits from 1 to 7, with the sum of all the digits = 28. There is a
    chance that there is a 7-digit pandigital that is a prime, so we only need to search up to the 7-digit pandigital.

    The max 7-digit pandigital is 7654321, so we only need to limit the search up to this point
"""


def main():
    # Max number, as taken from the analysis above
    input_number = 7654321

    start_time = time.time()
    result = find_max_pandigital_prime(input_number + 1)
    print("Result is {0}, found in {1} seconds".format(result, time.time() - start_time))


if __name__ == "__main__":
    main()

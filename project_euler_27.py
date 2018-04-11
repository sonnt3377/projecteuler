# coding=utf-8

"""
    Project Euler 27: Quadratic primes

    Euler discovered the remarkable quadratic formula: n^2 + n + 41
    It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39.
    However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
    and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

    The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for
    the consecutive values 0 <= n <= 79. The product of the coefficients, -79 and 1601, is -126479.

    Considering quadratics of the form: n^2 + an + b, where |a| < 1000 and |b| <= 1000
    where |n| is the modulus/absolute value of n e.g. |11| = 11 and |−4| = 4

    Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum
    number of primes for consecutive values of n, starting with n = 0.

"""

import time


def sieve(number):
    """
    Finding a list of primes less than to a number using sieving

    :param number: the upper bound number, that all primes need to be less than or equal
    :return: a list where its items are marked as prime/not prime
    """
    # A boolean list, each index indicates a corresponding number, the value in that index is True if that number is
    # prime,
    # and False otherwise
    primes = [True] * number

    # 0 and 1 are not primes
    primes[0], primes[1] = [False] * 2

    for index, value in enumerate(primes):
        # The first number with True is a prime, but the multiples of it are not
        if value is True:
            primes[index * 2::index] = [False] * (((number - 1) // index) - 1)

    return primes


def do_work(number, a_limit, b_limit):
    """
    Return answer to the exercise with certain a_limit and b_limit

    :param number: the input number to prepare a prime list
    :param a_limit:
    :param b_limit:
    :return: print out a, b, longest sequence, and product of the corresponding a and b

    Ref: http://code.jasonbhill.com/sage/project-euler-problem-27/ with some modifications
    """
    start_time = time.time()

    p = sieve(number)
    a_max, b_max, max_sequence = 0, 0, 0

    try:
        for a in range(- a_limit, a_limit + 1):
            # The expected value of 'b' should be > 80, since the expected combination of a and b will produce at least
            # 80 primes as in the example, meaning that b > 80
            for b in range(80, b_limit + 1):
                # 'b' must be a prime, otherwise the requirement does not satisfy when n = 0
                if p[b] is False:
                    continue
                # b must be greater than (- n^2 - a*n) since primes must be positive
                # This should apply to n = 40 too so it becomes b > (-40^2 - 40*a)
                if b < -1600 - 40 * a or b < max_sequence:
                    continue

                sequence_length, n = 0, 0

                # Calculate the number of consecutive primes
                while p[n ** 2 + a * n + b] is True:
                    sequence_length += 1
                    n += 1

                # Update max_sequence
                if sequence_length > max_sequence:
                    a_max, b_max, max_sequence = a, b, sequence_length

        product = a_max * b_max

        print("Brute force: a = {0}, b = {1}, longest sequence = {2}, product = {3} \nfound in {4} seconds".format(
            a_max, b_max, max_sequence, product, time.time() - start_time))
    except IndexError:
        print("Prepared prime list does not contains enough items, use a larger input number")


def main():
    # The first parameter, number is hand-picked so the list of prime numbers covers all possible primes produced
    # by certain a and b.
    # For |a| < 1000 and |b| <= 1000, and we know that the result should be more restrictive than n^2 - 79n + 1601
    # it looks like number ~ 79^2 + 79 * 1000 + 1000 is a good choice i.e. n is less than 79
    # The larger 'number' may reduce the performance, but a more restrictive number may not create enough primes for
    # a certain a and b
    do_work(86400, 1000, 1000)


if __name__ == "__main__":
    main()

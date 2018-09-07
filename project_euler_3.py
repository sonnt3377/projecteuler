"""
    Project Euler 3: Largest prime factor

    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143?
"""
import time
import math
from project_euler import is_prime


def find_largest_prime_factor_1(number):
    """
    Find largest prime factor using brute force

    :param number: input number
    :return: the largest prime factor
    """
    largest_factor = 0

    # Going through all numbers from 2 to square root of the input number to check if 
    # they are the factors
    for i in range(2, int(math.sqrt(number))):
        # If the number is a divisor
        if number % i == 0:
            factor1 = number // i
            factor2 = i

            # Update the largest prime factor
            if is_prime(factor1) and factor1 > largest_factor:
                largest_factor = factor1

            if is_prime(factor2) and factor2 > largest_factor:
                largest_factor = factor2

    return largest_factor


def find_largest_prime_factor_2(number):
    """
    Find largest prime factor of a number using continuous divisions.

    :param number: input number
    :return: larger prime factor
    """
    largest_factor = 0
    # The initial quotient is the input number itself
    quotient = number
    # The first, smallest factor
    i = 2

    # Continuously factor the number, we only need to do it from 2 to roughly the square root of the number
    while i <= int(math.sqrt(number)):
        # If i is a divisor,
        # Continue to factor until the quotient is not divisible by that number
        if quotient % i == 0:
            quotient = quotient // i
            # With the check above, i is always a prime
            largest_factor = i
        # If i is not a divisor, try the next one
        else:
            i += 1

    # After all the divisions, the largest factor is the last largest_factor, or the quotient itself
    if quotient > largest_factor:
        largest_factor = quotient

    return largest_factor


def main():
    """
    Test function
    """
    input_number = 600851475143

    # Test with algorithm 1
    start_time = time.time()
    result = find_largest_prime_factor_1(input_number)
    print("Result is {0} found in {1} seconds".format(result, time.time() - start_time))

    # Test with algorithm 2
    # Algorithm 2 has fewer division steps than algorithm 1
    start_time = time.time()
    result = find_largest_prime_factor_2(input_number)
    print("Result is {0} found in {1} seconds".format(result, time.time() - start_time))


if __name__ == "__main__":
    main()

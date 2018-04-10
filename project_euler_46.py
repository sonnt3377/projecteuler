"""
    Project Euler 46: Goldbach's other conjecture

    It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

    9 = 7 + 2 * 1^2
    15 = 7 + 2 * 2^2
    21 = 3 + 2 * 3^2
    25 = 7 + 2 * 3^2
    27 = 19 + 2 * 2^2
    33 = 31 + 2 * 1^2

    It turns out that the conjecture was false.

    What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
import math
import time

def find_prime_numbers_with_sieving(limit):
    """
    Find all prime numbers less than a limit using sieving.
    We use the same approach as in Project Euler 35.

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

    return prime_list

def is_twice_a_square(number):
    """
    Check if a number is twice a square

    :param number: input number

    :return: True if the number is twice a square, False otherwise
    """
    square_number = math.sqrt(number / 2)
    # print("{0} {1}".format(square_number, int(square_number)))
    return square_number == int(square_number)

def do_work():
    """
    Loop through all odd numbers, starting from the smallest, and check if it is the sum of a prime and 2 times a
    square number.

    :return: the smallest number satisfying that condition
    """

    # Generate the prime list at a certain size
    # Here we need to guess the list, that MAY contain enough numbers to find the result.
    # If the list is not long enough, the program may needs to run forever as it need to try larger odd numbers
    prime_list = find_prime_numbers_with_sieving(7000)

    is_result_found = False
    odd_number = 3

    while not is_result_found:

        # Check for the next odd number, we skip numbers less than 5
        odd_number += 2
        is_square = False

        for prime_number in prime_list:
            # Only check prime numbers that are not greater than the odd number
            if odd_number >= prime_number:
                # Check if the difference is a double of a square
                is_square = is_twice_a_square(odd_number - prime_number)
                # The diff number is already twice a square, no need to check for more.
                # This also means the odd number is not what we are looking for.
                # Go for the next odd number.
                if is_square:
                    break
            # This odd number satisfies the condition.
            else:
                is_result_found = True
                break

    return odd_number

def main():

    start_time = time.time()
    result = do_work()
    print("The result is {0}, found in {1} seconds".format(result, time.time() - start_time))

if __name__ == "__main__":
    main()
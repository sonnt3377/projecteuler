"""
    Project Euler 1: Multiples of 3 and 5

    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
"""
import time

def find_the_sum(number):
    """
    Find the sum of all multiples of 3 and 5 below 'number'

    :param number: the limit number
    :return: sum of all multiples of 3 and 5
    """
    sum = 0

    for i in range(number):
        # The number is a multiple of 3 or 5
        # If the number is a multiple of both 3 and 5, it is counted once
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i

    return sum

def main():
    start_time = time.time()
    result = find_the_sum(1000)
    print("Result is {0} found in {1} seconds".format(result, time.time() - start_time))

if __name__ == "__main__":
    main()
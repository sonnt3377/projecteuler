"""
    Project Euler 23: Non-abundant sums

    A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
    For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a
    perfect number.

    A number n is called deficient if the sum of its proper divisors is less than n and
    it is called abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
    the smallest number that can be written as the sum of two abundant numbers is 24.

    By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two
    abundant numbers.
    However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number
    that cannot be expressed as the sum of two abundant numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
import math
import time

UPPER_LIMIT = 28123


def find_divisor_sum(number):
    """
    Find sum of all divisors of a number. To find a divisor of 'number', we only need to test the division from number 2
    to a number ~ sqrt(number).

    :param number:
    :return: the sum of all divisors of 'number'
    """
    the_sum = 1  # 1 is always added to the sum since 1 is the divisor of all numbers

    # Start counting from 2
    i = 2

    while i <= math.sqrt(number):
        # If i is a divisor, then number/i is also a divisor
        if number % i == 0:
            the_sum += i
            other_divisor = number / i
            # Don't add the same divisor twice
            if i != other_divisor:
                the_sum += other_divisor
        i += 1

    return the_sum


def is_abundant(number):
    """
    Check if 'number' is abundant number

    :param number: a number to check
    :return: True is 'number' is abundant, False otherwise
    """
    return find_divisor_sum(number) > number


def create_abundant_number_list(number):
    """
    Create a list containing all abundant numbers less than or equal to 'number'

    :param number:
    :return: a list containing all abundant numbers less than or equal to 'number'
    """
    abundant_list = []

    for i in range(1, number + 1):
        if is_abundant(i):
            abundant_list.append(i)

    return abundant_list


def create_sum_abundant_list(number):
    """
    Create a list containing 'number' items.
    For the list item at index = i, marked it as True if that index is the sum of two abundant numbers, and False
    otherwise

    :param number:
    :return: a list in which items are True/False
    """

    # This is a boolean list, holding True/False to indicate if the corresponding number (represent by the index)
    # is sum of two abundant numbers
    list1 = [False] * number

    abundant_list = create_abundant_number_list(number)
    # Update 'list' above with True/False values
    for i in range(len(abundant_list)):
        for j in range(i, len(abundant_list)):
            # We only care about the abundant sum that is less than 'number'
            sum1 = abundant_list[i] + abundant_list[j]
            if sum1 <= number:
                list1[sum1 - 1] = True

    return list1


def find_sum_of_non_abundant_numbers(number):
    """
    Find sum of all positive integers which are not sum of two abundant numbers

    :param number:
    :return:
    """
    sum1 = 0
    list1 = create_sum_abundant_list(number)

    for i in range(number):
        if not list1[i]:
            # The number should start from 1, but Python list index starts from 0
            sum1 += i + 1

    return sum1


def main():
    """
    Test function
    """
    start_time = time.time()
    result = find_sum_of_non_abundant_numbers(UPPER_LIMIT)
    elapsed = time.time() - start_time
    print("Result is {0} found in {1} seconds.".format(result, elapsed))


if __name__ == "__main__":
    main()

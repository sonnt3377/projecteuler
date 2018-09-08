"""
    Project Euler 30: Digit fifth powers

    Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

    As 1 = 1^4 is not a sum it is not included.

    The sum of these numbers is 1634 + 8208 + 9474 = 19316.

    Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

"""
import math
import time


def calculate_fifth_power_sum(number):
    """
    Calculate the fifth power sum of a number

    :param number:
    :return:
    """
    number_list = [int(i) for i in str(number)]
    fifth_power_sum = 0

    for i in number_list:
        fifth_power_sum += math.pow(i, 5)

    return fifth_power_sum


def total_sum(threshold):
    """
    Find the sum of all the numbers less than the threshold,
    that can be written as the sum of fifth powers of their digits

    :param threshold:
    :return:
    """
    the_sum = 0
    for i in range(2, threshold):
        if i == calculate_fifth_power_sum(i):
            the_sum += i

    return the_sum


def main():
    """
    Observation:
    A digit ranges from 0 to 9, and 9^5 = 59049
    A number of the form abcdefg...h, and a^5 + b^5 + ... + h^5 < 9^5 + 9^5 + ... 9^5
    If the number contains 6 digits, then the fifth powers sum = a^5 + b^5 + c^5 + d^5 + e^5 + f^5
    The number itself = a . 10^5 + b . 10^4 + c.10^3 + d.10^2 + e.10 + f
    In this case, the number itself > fifth powers sum. This also applies to number with more than 6 digits
    It means, we only need to search for numbers up to 6 digits
    """
    start = time.time()
    result = total_sum(999999)

    print("Find result = {0} in {1} seconds".format(result, time.time() - start))


if __name__ == "__main__":
    main()

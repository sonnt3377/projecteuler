"""
    Project Euler 40: Champernowne's constant

    An irrational decimal fraction is created by concatenating the positive integers:

    0.123456789101112131415161718192021...

    It can be seen that the 12th digit of the fractional part is 1.

    If dn represents the nth digit of the fractional part, find the value of the following expression.

    d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
"""
import functools
import operator
import time


def calculate_the_product():
    """
    Calculating the product of d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000

    :return: the product
    """
    """
    Analysis: There are
        9 1-digit numbers: 1 to 9 -> 9 digits
        90 2-digit numbers: 10 to 99 -> 90 x 2 = 180 digits
        900 3-digit numbers: 100 to 999 ->  900 x 3 = 2700 digits
        9000 4-digit numbers: 1000 to 9999 -> 9000 x 4 = 36000 digits
        90000 5-digit numbers: 10000 to 99999 -> 90000 x 5 = 450000 digits
        900000 6-digit numbers: 100000 to 999999 -> 900000 x 6 = 54000000 digits

    Depending on n, one can calculate which group that digit belongs to.
    """
    max_number_of_digit = 1000000
    # Approximating the actual number corresponding to the max digit e.g. 1000000
    # This number should be a 6-digit number
    # We add 10 to cover a bit more than that exact number
    number = (max_number_of_digit - 9 - 180 - 2700 - 36000 - 450000) // 6 + 99999 + 10

    # Create a list containing all numbers from 1 to that number of interest
    string = ""
    for i in range(1, number):
        string += str(i)

    digit_list = list(string)
    result_digits = [int(digit_list[10 ** i - 1]) for i in range(7)]
    product = functools.reduce(operator.mul, result_digits, 1)

    return result_digits, product


def main():
    start_time = time.time()
    result_digits, product = calculate_the_product()
    print("The result is {0}, found in {1} seconds. The digits are {2}".format(product, time.time() - start_time,
                                                                               result_digits))


if __name__ == "__main__":
    main()

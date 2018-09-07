"""
    Project Euler 20: Factorial digit sum

    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!
"""

import time


def factorial_1(number):
    """
    Finding n! using recursive

    :param number: input number
    :return: n!
    """
    if number == 0:
        return 1

    return number * factorial_1(number - 1)


def factorial_2(number):
    """
    Finding n! using multiplication

    :param number: input number
    :return: n!
    """
    result = 1

    for i in range(2, number + 1):
        result *= i

    return result


def factorial_3(number):
    """
    Finding n! by multiplying and storing digits in an array.
    This array is a representation of the factorial number, but not the number itself.

    :param number: input number
    :return: array where each item represents a digit in the factorial number, in reverse order
    """
    result = [1]

    for i in range(2, number + 1):
        result = multiply(result, i)

    return result


def multiply(number1_list, number2):
    """
    Multiplying two numbers, by multiplying the second number with each digit of the first number respectively, then
    carry result over to the higher digits if it is larger than 9 i.e. the largest number of a digit.

    :param number1_list: a list representing a number in the reverse order
        e.g. if the number is 123, then the list is [3, 2, 1]
    :param number2: the multiplying number
    :return: a list representing a result number, in reverse order.
    """
    # Initially, there is nothing to carry over to the higher digits
    carry_over = 0

    for number in number1_list:
        product = int(number) * number2 + carry_over
        # Update the least significant digit in number1_list with the result digit
        number = product % 10
        # Carry the remaining value over to higher digits
        carry_over = product // 10

    # If there is anything more to carry over, the result list will have more digits than the original list
    while carry_over > 0:
        new_digit = carry_over % 10
        number1_list.append(str(new_digit))
        carry_over = carry_over // 10

    return number1_list


def main():
    """
    Test method
    """
    # Using recursive
    # This method cannot work with large numbers due to the recursion limits
    # It also has problem when multiplying large numbers
    # sys.setrecursionlimit(100000)
    # start = time.time()
    # result = sum(map(int, str(factorial_1(1000))))

    # Using multiplication
    # This method may go up to the limit of the number defined by the software
    # It also has problem when multiplying large numbers
    start = time.time()
    result = sum(map(int, str(factorial_2(1000))))
    print("Result is {0} found in {1} seconds".format(result, time.time() - start))

    # Using multiplication and carry over
    # This method does not provide a number representing a factorial, but a list with item representing
    # the digits in the factorial number.
    # This method avoids using larger number as the output of the multiplication operations.
    start = time.time()
    result_list = factorial_3(1000)
    result = sum(int(i) for i in result_list)
    print("Result is {0} found in {1} seconds".format(result, time.time() - start))


if __name__ == '__main__':
    main()

"""

    Test performance of different factorial methods

"""
import math
import time

def conventional_factorial(number):
    """
    Calculate factorial n! = 1 x 2 x 3 x ... x n using recursive

    :param number: input number
    :return: number!, return 0 if number < 1
    """
    if number < 1:
        print("There is no factorial value")
        return 0

    if number == 1:
        return 1

    return number * conventional_factorial(number - 1)


def range_prod(low, high):
    """
    Ref: https://stackoverflow.com/questions/16325988/factorial-of-a-large-number-in-python
    In the conventional recursive method, the result gets larger very quick, then with each recursive step,
    the algorithm multiplies a small number with an already-large value, which takes a lot of time.
    This method tries to avoid multiplication of larger numbers in the early phase of the calculation by trying to
    multiply numbers of roughly the same size, hence avoiding multiplying a small and a larger number.

    :param low: lower bound
    :param high: upper bound
    :return: product of all numbers from lower bound to upper bound
    """
    if low + 1 < high:
        middle = (high + low) // 2
        return range_prod(low, middle) * range_prod(middle + 1, high)

    if low == high:
        return low

    return low * high


def tree_factorial(number):
    """
    Implement factorial using range_prod above.
    Ref: https://stackoverflow.com/questions/16325988/factorial-of-a-large-number-in-python

    :param number: input number
    :return: number!
    """
    if number < 2:
        return 1

    return range_prod(1, number)


def main():
    """
    Test function
    """
    # Test number
    input_number = 900  # 20000

    # Method 1: tree factorial
    start_time = time.time()
    result = tree_factorial(input_number)
    print("Tree factorial result: {0} found in {1}".format(result, time.time() - start_time))

    # Method 2: Python math.factorial
    start_time = time.time()
    result = (math.factorial(input_number))
    print("Math.factorial result: {0} found in {1}".format(result, time.time() - start_time))

    # Method 3: factorial using recursive
    # This method will quickly explode when n becomes large due to RecursionError
    start_time = time.time()
    result = conventional_factorial(input_number)
    print("Recursive factorial result: {0} found in {1}".format(result, time.time() - start_time))


if __name__ == "__main__":
    main()

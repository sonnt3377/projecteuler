"""

    Test performance of different factorial methods

"""

import math
import time

def conventional_factorial(n):
    """
    Calculate factorial n! = 1 x 2 x 3 x ... x n using recursive

    :param n: input number
    :return: n!
    """
    if n < 1:
        print("There is no factorial value")
    else:
        if n == 1:
            return 1
        else:
            return n * conventional_factorial(n - 1)

def range_prod(low, high):
    """
    Ref: https://stackoverflow.com/questions/16325988/factorial-of-a-large-number-in-python
    In the conventional recursive method, the result gets larger very quick, then with each recursive step, the algorithm
    multiplies a small number with an already-large value, which takes a lot of time.
    This method tries to avoid multiplication of larger numbers in the early phase of the calculation by trying to multiply
    numbers of roughly the same size, hence avoiding multiplying a small and a larger number.

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

def tree_factorial(n):
    """
    Implement factorial using range_prod above.
    Ref: https://stackoverflow.com/questions/16325988/factorial-of-a-large-number-in-python

    :param n: input number
    :return: n!
    """
    if n < 2:
        return 1
    return range_prod(1, n)

def main():
    # Test number
    INPUT_NUMBER = 900 #20000

    # Method 1: tree factorial
    start_time = time.time()
    result = tree_factorial(INPUT_NUMBER)
    print("Tree factorial result: {0} found in {1}".format(result, time.time() - start_time))

    # Method 2: Python math.factorial
    start_time = time.time()
    result = (math.factorial(INPUT_NUMBER))
    print("Math.factorial result: {0} found in {1}".format(result, time.time() - start_time))

    # Method 3: factorial using recursive
    # This method will quickly explode when n becomes large due to RecursionError
    start_time = time.time()
    result = conventional_factorial(INPUT_NUMBER)
    print("Recursive factorial result: {0} found in {1}".format(result, time.time() - start_time))

if __name__ == "__main__":
    main()
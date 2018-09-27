"""
    Project Euler 56: Powerful digit sum

    A googol (10^100) is a massive number: one followed by one-hundred zeros;
    100^100 is almost unimaginably large: one followed by two-hundred zeros.
    Despite their size, the sum of the digits in each number is only 1.

    Considering natural numbers of the form, a^b, where a, b < 100, what is the
    maximum digital sum?
"""
import time

def find_max_sum():
    """
    Find the max digit sum of all number a^b when 0 < i < 100, and 0 < j < 100

    return: the max digit sum
    """
    max_sum = 0

    for i in range(100):
        for j in range(100):
            product = i**j
            temp_sum = sum([int(digit) for digit in str(product)])
            if temp_sum > max_sum:
                max_sum = temp_sum

    return max_sum


def find_max_sum_one_liner():
    """
    Use Python one-liner to find max sum
    """
    return max(sum(map(int, str(i**j))) for i in range(100) for j in range(100))


def find_max_sum_one_liner_1():
    """
    Use Python one-liner to find max sum.
    Modified method to limit the search range
    """
    return max(sum(map(int, str(i**j))) for i in range(90, 100) for j in range(90, 100))


def main():
    """
    Test
    """
    start_time = time.time()
    result = find_max_sum()
    print("The result is {0}, found in {1} seconds.".format(result, time.time() - start_time))

    start_time = time.time()
    result = find_max_sum_one_liner()
    print("One-liner: The result is {0}, found in {1} seconds."
          .format(result, time.time() - start_time))

    start_time = time.time()
    result = find_max_sum_one_liner_1()
    print("Modified one-liner: The result is {0}, found in {1} seconds."
          .format(result, time.time() - start_time))


if __name__ == "__main__":
    main()

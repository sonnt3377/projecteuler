"""
    Project Euler 48: Self powers

    The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

    Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""
import time


def do_work(n):
    """
    Find the last ten digit of the sum 1^1 + 2^2 + ... n^n

    :param n: input number
    :return: the last ten digit of the sum
    """
    """
    Analysis: we use two properties of modulo arithmetic
        (a + b) mod n = [(a mod n) + (b mod n)] mod n
        (a * b) mod n = (a mod n) * (b mod n)
    """
    # For number n, the remainder of n mod 10000000000 is the last 10 digits of that number
    divisor = 10000000000
    result = 0

    for i in range(1, n + 1):
        temp = i
        # Finding i^i mod n
        for j in range(1, i):
            temp *= i
            temp %= divisor

        # Finding (i^i + j^j) mod n
        result += temp
        result %= divisor

    return result


def main():
    start_time = time.time()
    result = do_work(1000)
    print("The result is {0}, found in {1} seconds".format(result, time.time() - start_time))


if __name__ == "__main__":
    main()

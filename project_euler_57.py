"""
Project Euler 57: Square root convergents
    It is possible to show that the square root of two can be expressed
    as an infinite continued fraction.

    √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

    By expanding this for the first four iterations, we get:
    1 + 1/2 = 3/2 = 1.5
    1 + 1/(2 + 1/2) = 7/5 = 1.4
    1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
    1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

    The next three expansions are 99/70, 239/169, and 577/408,
    but the eighth expansion, 1393/985, is the first example where the number
    of digits in the numerator exceeds the number of digits in the denominator.

    In the first one-thousand expansions, how many fractions contain a numerator
    with more digits than denominator?
"""
import time
import math


def do_work(limit):
    """
    With the number of expansions upper to 'limit', return the number of fractions
    whenre the numerator has more digits than denominator

    param limit: the upper limit for the number of tested expansions
    return: number of fractions satisfying the condition
    """
    no_of_fractions = 0

    # First denominator and numerator
    den = 3
    num = 2

    # Note that the next denominator and numerator can be found by formula
    # den_k+1 = den_k + num_k
    # num_k+1 = num_k + 2 * den_k = num_k + 2 *(den_k+1 - num_k)
    #         = 2 * den_k+1 - num_k

    for _ in range(1, limit + 1):
        den += num
        num = 2 * den - num
        # Check the number of digits of num and en using log10
        if (int)(math.log10(num)) > (int)(math.log10(den)):
            no_of_fractions += 1

    return no_of_fractions


def main():
    """
    Test
    """
    start_time = time.time()
    result = do_work(1000)
    print("The result is {0}, found in {1} seconds."
          .format(result, time.time() - start_time))


if __name__ == "__main__":
    main()

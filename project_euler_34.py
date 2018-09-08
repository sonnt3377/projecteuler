"""
    Project Euler 34: Digit factorials

    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the sum of the factorial of their digits.

    Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
import time
import math


def do_work():
    """
        Analysis:
        Assuming that the number contains n digits, then
            A = The sum of the factorials of its digits is <= n*9! = 362880*n (= if all digits are 9)
            B = The value of the number itself >= 10^(n-1) (= when the highest digit is 1, and all others are 0)

        For a certain value of n, B will always > A and as n increases beyond that value, A will never catch up,
        so to find the solution, we only need to reach to the point where A may catch up with B.

        For n = 7, max(A) = 7*9! = 2,540,160, min(B) = 10^6 = 1,000,000 => there is a possibility for A = B
        For n = 8, max(A) = 2,903,040, min(B) = 10^7 = 10,000,000 => no possibility for A = B.
        For n > 8, same as n = 8

        So we only need to search for up to n = 7 digits, with the max possible value is 7*9!
    """
    # A list containing pre-calculated factorial of number from 0 to 9
    factorial_list = [math.factorial(i) for i in range(0, 10)]
    # The sum of all numbers which are equal to the sum of the factorial of their digits.
    sum_of_number = 0
    # Max search range, as discussed in the Analysis part
    max_range = 2540160

    # Start from 3, as 1 and 2 are excluded
    for i in range(3, max_range + 1):
        number = i
        factorial_sum = 0

        # Finding sum of factorials of the digits
        while number > 0:
            digit = number % 10
            number //= 10
            factorial_sum += factorial_list[digit]

        # If the number is equal to the sum of the factorials of its digits, it satisfies the requirement.
        if factorial_sum == i:
            print("The number is {0}".format(i))
            sum_of_number += i

    return sum_of_number


def main():
    """
    Test function
    """
    start_time = time.time()
    result = do_work()
    print("Result is {0} found in {1} seconds".format(result, time.time() - start_time))


if __name__ == "__main__":
    main()

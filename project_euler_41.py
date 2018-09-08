"""
    Project Euler 41: Pandigital prime

    We shall say that an n-digit number is pandigital if it makes use of all the
    digits 1 to n exactly once.
    For example, 2143 is a 4-digit pandigital and is also prime.

    What is the largest n-digit pandigital prime that exists?
"""
import time
import project_euler


def find_max_pandigital_prime(limit):
    """
    Find the largest n-digit pandigital prime that less than limit

    :param limit: the limit number
    :return: the largest pandigital prime less than limit
    """
    prime_list = project_euler.sieve(limit)

    # Counting from the largest prime number down, until we find a number that is a pandigital
    for i in reversed(prime_list):
        if project_euler.is_pandigital(i):
            return i

    # Should never reach here
    # Return the smallest prime
    return 2

# Analysis:

# A n-digit pandigital number will have a form 123...n or the permutation of that.
# However, the number of digits will be the same.
# In addition, to be a pandigital, a number cannot have more than 9 digits, because
# there will be duplicate(s) otherwise
# So a 9-digit pandigital (if exists) contains all digits from 1 to 9, and the sum of
# the digits = 45. This number is divisible by 3 or 9, meaning that those pandigital
# numbers are not prime
# Similarly, a 8-digit pandigital (if exists) will not be a prime.
# A 7-digit pandigital (if exists) contains all digits from 1 to 7, with the sum of all
# the digits = 28. There is a chance that there is a 7-digit pandigital that is a prime,
# so we only need to search up to the 7-digit pandigital.

# The max 7-digit pandigital is 7654321, so we only need to limit the search up to this
# point
def main():
    """
    Test
    """
    # Max number, as taken from the analysis above
    input_number = 7654321

    start_time = time.time()
    result = find_max_pandigital_prime(input_number + 1)
    print("Result is {0}, found in {1} seconds".format(result, time.time() - start_time))


if __name__ == "__main__":
    main()

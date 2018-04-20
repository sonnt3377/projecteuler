"""
    Project Euler 50: Consecutive prime sum

    The prime 41, can be written as the sum of six consecutive primes:
    41 = 2 + 3 + 5 + 7 + 11 + 13

    This is the longest sum of consecutive primes that adds to a prime below one-hundred.

    The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms,
    and is equal to 953.

    Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
import time


def generate_primes_using_sieving(limit):
    """
    Generating a list of prime numbers less than the limit.

    :param limit: the upper limit
    :return: the prime list
    """
    # A boolean list, in which an item's index indicates a number corresponding to that index, and the item's value
    # is True if that corresponding number is a prime, and False otherwise
    primes = [True] * limit
    # 0 and 1 are not prime
    primes[0], primes[1] = [False] * 2

    for index, value in enumerate(primes):
        # The first number with True is a prime, but the multiples of it are not
        if value is True:
            primes[index * 2::index] = [False] * (((limit - 1) // index) - 1)

    prime_list = [i for i in range(limit) if primes[i] is True]

    return prime_list


def find_cumulative_prime_sum(prime_list):
    """
    Find a list, corresponding to the input prime list, where each item is the cumulative sum of all previous
    primes in the prime_list
    Ref: https://www.mathblog.dk/project-euler-50-sum-consecutive-primes/

    :param prime_list:
    :return: the list of cumulative prime sums
    """
    # First item in the list
    prime_sum_list = [2]

    for i in range(len(prime_list) - 1):
        prime_sum_list.append(prime_list[i + 1] + prime_sum_list[i])

    return prime_sum_list


def find_largest_prime(prime_sum_list, prime_list, limit):
    """
    Find the prime, below one-million, that can be written as the sum of the most consecutive primes

    :return: that prime
    """
    # Number of consecutive primes, when add up, will create another prime below 10000000
    consecutive_prime_counter = 0

    the_prime = 2

    for i in range(consecutive_prime_counter, len(prime_sum_list)):
        for j in range(i - consecutive_prime_counter - 1, -1, -1):
            diff = prime_sum_list[i] - prime_sum_list[j]
            if diff > limit:
                break
            # This is a prime
            if diff in prime_list:
                consecutive_prime_counter = i - j
                the_prime = prime_sum_list[i] - prime_sum_list[j]

    return consecutive_prime_counter, the_prime


def main():
    start_time = time.time()
    limit = 1000000
    prime_list = generate_primes_using_sieving(limit)
    prime_sum_list = find_cumulative_prime_sum(prime_list)
    result = find_largest_prime(prime_sum_list, prime_list, limit)
    print("The number of consecutive primes is {0}, and the prime is {1}, "
          "found in {2} seconds".format(result[0], result[1], time.time() - start_time))


if __name__ == "__main__":
    main()

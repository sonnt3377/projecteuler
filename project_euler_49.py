"""
    Project Euler 49: Prime permutations

    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by
    3330, is unusual in two ways:
    (i) each of the three terms are prime, and,
    (ii) each of the 4-digit numbers are permutations of one another.

    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
    exhibiting this property, but there is one other 4-digit increasing sequence.

    What 12-digit number do you form by concatenating the three terms in this sequence?
"""
import time
import project_euler


def is_permutation(number1, number2):
    """
    Check if two numbers are permutations of each other

    :param number1:
    :param number2:
    :return: True if two numbers are permutation of each other, False otherwise.
    """
    str1 = str(number1)
    str2 = str(number2)

    # If number1 and number2 are not the same length, they are not permutation of each other
    if len(str1) != len(str2):
        return False

    dict1 = {}
    dict2 = {}

    # Count the number of different digits in number1 and store them.
    for digit in str1:
        # This digit appears before
        if digit in dict1.keys():
            dict1[digit] += 1
        # This digit appears the first time
        else:
            dict1[digit] = 1

    # Count the number of different digits in number2 and store them
    for digit in str2:
        # This digit appears before
        if digit in dict2.keys():
            dict2[digit] += 1
        # This digit appears the first time
        else:
            dict2[digit] = 1

    # Compare the number of digits in number1 with those in number2
    for digit in dict1.keys():
        # If number1 contains a digit that is not in number2, then the two numbers are
        # not permutations
        if digit not in dict2.keys():
            return False

        # If the two numbers contain different numbers of the same digit, they are not permutations.
        if dict1[digit] != dict2[digit]:
            return False

    return True


def do_work():
    """
    Find the three primes that are:
        1. Permutations of one another
        2. prime1 - prime2 = prime2 - prime3

    :return: those three primes
    """
    # Generate 4-digit prime list, skipping the 1487 to exclude the existing solutions.
    prime_list = project_euler.sieve(10000, 1488)

    # Pick two primes out of the prime list
    for i in range(len(prime_list) - 1):
        for j in range(i + 1, len(prime_list)):
            # Find a number satisfying condition 2. above
            test_number = prime_list[j] + (prime_list[j] - prime_list[i])
            # Check if the test number is also a prime
            # And if so, there three primes are permutation of each other
            if test_number in prime_list:
                if is_permutation(prime_list[i], prime_list[j]) \
                   and is_permutation(prime_list[j], test_number):
                    return prime_list[i], prime_list[j], test_number

    # Test code
    return 1, 2, 3


def main():
    """
    Test
    """
    start_time = time.time()
    primes = do_work()
    print("The three primes are: {0}, {1}, {2}".format(primes[0], primes[1], primes[2]))
    print("The result is {0}, found in {1} seconds"
          .format(str(primes[0]) + str(primes[1]) + str(primes[2]),
                  time.time() - start_time))


if __name__ == "__main__":
    main()

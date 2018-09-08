"""

    Project Euler 21: Amicable numbers

    Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
    If d(a) = b and d(b) = a, where a <> b, then a and b are an amicable pair and each of a and b are called
    amicable numbers.
    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
    The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.

"""
import time


def find_divisor_sum(number):
    """
    Find sum of all proper divisors of a number

    :param number:
    :return: sum of all proper divisors of that number
    """
    sum1 = 0
    for i in range(1, number):
        if number % i == 0:
            # i is a divisor
            sum1 += i
    return sum1


def find_amicable_pairs(number):
    """
    Find all amicable pairs for numbers less than the number

    :param number:
    :return: a list of all amicable pairs
    """

    # Create a list containing sum of all proper divisors of i, with i ranging from 1 to n.
    # This list contains n items
    list_of_sum = [find_divisor_sum(i) for i in range(1, number + 1)]

    # 'pairs' is a list in which each component is an amicable pair
    pairs = []

    # Loop through 'list_of_sum' to find every amicable pairs
    for i in range(1, number):
        temp = list_of_sum[i]
        # Check if there is any number that forms a pair with this 'temp' value
        if (temp >= 1 and i + 1 < temp <= number and list_of_sum[temp - 1] == i + 1):
            # Find the pair, add it to 'pairs'
            pairs.append([i + 1, temp])

    return pairs


def find_amicable_sum(pairs):
    """
    Find sum of all pairs
    """
    return sum([sum(pair) for pair in pairs])


def main():
    """
    Test function
    """
    number = 10000
    start_time = time.time()
    result = find_amicable_sum(find_amicable_pairs(number))
    stop_time = time.time()

    print("Result is {0} found in {1} seconds".format(result, stop_time - start_time))
    

if __name__ == '__main__':
    main()

# coding=utf-8

"""
    Project Euler 31

    Coins sum

    In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
    It is possible to make £2 in the following way:
    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
    How many different ways can £2 be made using any number of coins?
"""

import time

def calculate_with_dp(target_number):
    """
    Calculate the number of combinations using dynamic programming

    :param target_number: the target number of the combination. E.g. 200 (cents) in this example
    :return: the number of combination to form that target_number, using the combination of available coins.
    """

    # All possible English coins, amount in pence
    coins = [1, 2, 5, 10, 20, 50, 100, 200]

    # 201-element list, which represents how many ways we can combine the above mentioned coins to create the exact
    # number in the corresponding element.
    #
    # The list index represents the target number
    # ways[index] = number of combination using existing coins to form that target number.
    # E.g ways[200] = number of ways to form 2 pounds out of the available coins.
    ways = [0] * (target_number + 1)

    # When we need to return £0 with coins, then there is only one solution i.e. that solution is "impossible"
    ways[0] = 1

    # Going through all the coins
    # When i = 1, we need to fill in the list ways[] using only 1 penny coin.
    # Then ways[] only contains elements with value = 1 e.g there is only one way to do that for all numbers from
    # 0 to 200.
    # When i = 2, we can use either 1 penny or 2 penny or any combination to fill in ways[]
    # Then the number of ways[] = the previous number of ways[] (for 1 penny) plus any other possible ways using 2 penny.
    # Not all numbers in ways[] get this updated though, it depends on the combinations.
    # And so on for other i in coins list.
    for i in range(len(coins)):
        for j in range(coins[i], target_number + 1):
            ways[j] += ways[j - coins[i]]

    return ways

def calculate_with_brute_force(target_number):
    """
    Calculate the number of combinations using brute force approach

    :param target_number: the target number of the combination. E.g. 200 (cents) in this example
    :return: the number of combination to form that target_number, using the combination of available coins.
    """
    ways = 0
    # Loop through all possible values
    for a in range(target_number, -1, -200):
        for b in range(a, -1, -100):
            for c in range(b, -1, -50):
                for d in range(c, -1, -20):
                    for e in range(d, -1, -10):
                        for f in range(e, -1, -5):
                            for g in range(f, -1, -2):
                                ways += 1

    return ways

# £2 (200p), bigger numbers will show larger difference between the two algorithms.
number = 200

start_time = time.clock()
result_dp = calculate_with_dp(number)
result = result_dp[len(result_dp) - 1]
dp_time = time.clock() - start_time

start_time = time.clock()
result_brute_force = calculate_with_brute_force(number)
brute_force_time = time.clock() - start_time

print("Result is {0} found in {1} with dynamic programming".format(result, dp_time))
print("Result is {0} found in {1} with brute force".format(result_brute_force, brute_force_time))
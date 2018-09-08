"""
    Project Euler 38: Pandigital multiples

    Take the number 192 and multiply it by each of 1, 2, and 3:
    192 x 1 = 192
    192 x 2 = 384
    192 x 3 = 576

    By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated
    product of 192 and (1,2,3)

    The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
    which is the concatenated product of 9 and (1,2,3,4,5).

    What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer
    with (1,2, ... , n) where n > 1?
"""
import time
import project_euler


def find_max_pandigital():
    """
    Find the max 9-digit pandigital
    :return: the max value, plus the components generating that value

    Analysis:
    A 9-digit pandigital can be formed by:
        Number A x (1, 2)
        Number B x (1, 2, 3)
        Number C x (1, 2, 3, 4)
        Number D x (1, 2, 3, 4, 5)
    Since the pandigital is 9-digit
        A should be a 4-digit number
        B should be a 3-digit number
        C should be a 2-digit number
        D should be a 1-digit number
    """
    max_value = 0

    # Search for all cases in A
    for four_digit_number in range(1000, 10000):
        # If a pandigital is found
        if project_euler.is_9_digit_pandigital(four_digit_number, four_digit_number * 2):
            pan_digital = int(str(four_digit_number) + str(four_digit_number * 2))
            if max_value < pan_digital:
                max_value = pan_digital

    # Search for all cases in B
    for three_digit_number in range(100, 1000):
        # If a pandigital is found
        if project_euler.is_9_digit_pandigital(three_digit_number, three_digit_number * 2, three_digit_number * 3):
            pan_digital = int(str(three_digit_number) + str(three_digit_number * 2) + str(three_digit_number * 3))
            if max_value < pan_digital:
                max_value = pan_digital

    # Search for all cases in C
    for two_digit_number in range(10, 100):
        # If a pandigital is found
        if project_euler.is_9_digit_pandigital(two_digit_number, two_digit_number * 2,
                                       two_digit_number * 3, two_digit_number * 4):
            pan_digital = int(str(two_digit_number) + str(two_digit_number * 2)
                              + str(two_digit_number * 3) + str(two_digit_number * 4))
            if max_value < pan_digital:
                max_value = pan_digital

    # Search for all cases in D
    for one_digit_number in range(1, 10):
        # If a pandigital is found
        if project_euler.is_9_digit_pandigital(one_digit_number, one_digit_number * 2, one_digit_number * 3,
                                       one_digit_number * 4, one_digit_number * 5):
            pan_digital = int(str(one_digit_number) + str(one_digit_number * 2)
                              + str(one_digit_number * 3) + str(one_digit_number * 4) + str(one_digit_number * 5))
            if max_value < pan_digital:
                max_value = pan_digital

    return max_value

# Analysis:
#     The max 9-digit pandigital should start with digit 9, so the fixed number should
#     start with 9 since it multiplies with 1 and then concated to be the first path
#     of the 9-digit pandigital.
#     A 9-digit pandigital can be formed by:
#         Number A x (1, 2)
#         Number B x (1, 2, 3)
#         Number C x (1, 2, 3, 4)
#         Number D x (1, 2, 3, 4, 5)
#     Since the pandigital is 9-digit
#         A should be a 4-digit number
#         B should be a 3-digit number
#         C should be a 2-digit number
#         D should be a 1-digit number
#     If the number is 2-digit (we only consider it in the form 9x, as we search for
#     the max pandigital)
#         When multiplying with (1, 2, 3), the longest number it creates has 8 digits
#         When multiplying with (1, 2, 3, 4), the shortest number it creates has 11 digits
#     If the number is 3-digit (we only consider it in the form 9x, as we search for
#     the max pandigital)
#         When multiplying with (1, 2), the longest number it creates has 7 digits
#         When multiplying with (1, 2, 3), the shortest number it creates has 11 digits
#     So the number can have only one digit i.e. 9 or 4 digits i.e 9xyz
#     Regarding 4-digit numbers, the range should be from 9123 (smallest 4-digit with
#     possibility to create a 9-digit pandigital) to 9876 (largest 4-digit with
#     possibility to create a 9-digit pandigital).

def find_max_pandigital_2():
    """
    Find the max 9-digit pandigital with some additional constraints

    :return: the max value
    """
    # Max 9-digit pandigital, found when multiplying 9 with (1, 2, 3, 4, 5)
    max_value = 918273645

    # We search from large numbers down until finding a pandigital, and stop, since we already find the largest
    for i in range(9876, 9123, -1):
        if project_euler.is_9_digit_pandigital(i, i * 2):
            max_value = int(str(i) + str(i * 2))
            break

    return max_value


def main():
    """
    Test
    """
    # Searching with 'brute force'
    start_time = time.time()
    result = find_max_pandigital()
    print("Method 1: Result is {0}, found in {1} seconds".format(result, time.time() - start_time))

    # Searching using a more optimal approach
    start_time = time.time()
    result = find_max_pandigital_2()
    print("Method 2: Result is {0}, found in {1} seconds".format(result, time.time() - start_time))


if __name__ == "__main__":
    main()

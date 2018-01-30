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

def is_pandigital(*numbers):
    """
    Decide if a list of numbers, when concatenating to each other, create a pandigital

    :param numbers: list of numbers to test
    :return: True if the concatenating of numbers create a pandigital, False otherwise
    """
    test_string = ""
    digit_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for number in numbers:
        test_string += str(number)

    # The string is not pandigital if it contains 0 or if it has more than 9 digits
    if len(test_string) != 9 or '0' in test_string:
        return False

    # The string is pandigital if each digit from 1 to 9 appears only once
    return all(digit in test_string for digit in digit_list)

def find_max_pandigital():
    """
    Find the max 9-digit pandigital
    :return: the max value, plus the components generating that value
    """
    """
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
    for a in range(1000, 10000):
        # If a pandigital is found
        if is_pandigital(a, a * 2):
            pan_digital = int(str(a) + str(a * 2))
            if max_value < pan_digital:
                max_value = pan_digital

    # Search for all cases in B
    for b in range(100, 1000):
        # If a pandigital is found
        if is_pandigital(b, b * 2, b * 3):
            pan_digital = int(str(b) + str(b * 2) + str(b * 3))
            if max_value < pan_digital:
                max_value = pan_digital

    # Search for all cases in C
    for c in range(10, 100):
        # If a pandigital is found
        if is_pandigital(c, c * 2, c * 3, c * 4):
            pan_digital = int(str(c) + str(c * 2) + str(c * 3) + str(c * 4))
            if max_value < pan_digital:
                max_value = pan_digital

    # Search for all cases in D
    for d in range(1, 10):
        # If a pandigital is found
        if is_pandigital(d, d * 2, d * 3, d * 4, d * 5):
            pan_digital = int(str(d) + str(d * 2) + str(d * 3) + str(d * 4) + str(d * 5))
            if max_value < pan_digital:
                max_value = pan_digital

    return max_value

def main():

    start_time = time.time()
    result = find_max_pandigital()
    print("Brute force: Result is {0}, found in {1} seconds".format(result, time.time() - start_time))

if __name__ == "__main__":
    main()
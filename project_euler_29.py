# coding=utf-8

"""
    Project Euler 29: Distinct powers

    Consider all integer combinations of a^b for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

    2^2=4, 2^3=8, 2^4=16, 2^5=32
    3^2=9, 3^3=27, 3^4=81, 3^5=243
    4^2=16, 4^3=64, 4^4=256, 4^5=1024
    5^2=25, 5^3=125, 5^4=625, 5^5=3125

    If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:

    4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

    How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
"""
import math
import time

def calculate_a_to_power_b(a_start, a_end, b_start, b_end):
    """
    Calculate a^b for a in range a_start to a_end, and b_start to b_end, then store them in a list

    :param a_start:
    :param a_end:
    :param b_start:
    :param b_end:
    :return:
    """
    list = []
    a = a_start
    b = b_start

    while(a <= a_end):
        while(b <= b_end):
            temp = math.pow(a, b)
            list.append(temp)
            b += 1
        a += 1
        b = b_start

    return list

def remove_duplicate(input_list):
    """
    Create a new list and remove duplicate number

    :param input_list: original list, possibly with duplicate numbers
    :return: a list where duplicate numbers are removed
    """
    output_list = []
    for item in input_list:
        if item not in output_list:
            output_list.append(item)

    return output_list

def main():
    start = time.time()
    result = len(remove_duplicate(calculate_a_to_power_b(2, 100, 2, 100)))
    elapsed = time.time() - start

    print("The result is {0}, found in {1} seconds".format(result, elapsed))

if __name__ == '__main__':
    main()
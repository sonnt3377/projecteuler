"""
    Project Euler 28: Number spiral diagonals

    Starting with the number 1 and moving to the right in a clockwise direction, a 5 by 5 spiral is formed as follows:

        21 22 23 24 25
        20  7  8  9 10
        19  6  1  2 11
        18  5  4  3 12
        17 16 15 14 13

    It can be verified that the sum of the numbers on the diagonals is 101.

    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
import math
import time

def sum_of_corners(n):
    """
    Calculate the sum of the four corners of a square size 2n + 1

    :param n: input number
    :return: the sum
    """
    square_size = 2 * n + 1
    corner_value_distance = square_size - 1

    # Finding the conner values
    # The upper right corner value is always n^2, be n = 1, 3, 5, 7 etc.,
    # The other corners are n^2 - k*(n-1)
    upper_right = math.pow(square_size, 2)
    upper_left = upper_right - corner_value_distance
    lower_left = upper_left - corner_value_distance
    lower_right = lower_left - corner_value_distance

    # Calculate sum of all corners
    return upper_right + upper_left + lower_left + lower_right

def diagonal_sum(size_of_square):
    """
    Sum of the diagonals of 1001 by 1001 square

    :param size_of_square:
    :return: the sum
    """
    # This is sum of the square which has one 1 element
    sum = 1
    counter = 1

    # Sum of corners of all squares from the innermost to the outermost.
    # This will form the sum of the diagonals
    while (2 * counter + 1 <= size_of_square):
        sum += sum_of_corners(counter)
        counter += 1

    return sum

def main():
    start_time = time.time()
    result = diagonal_sum(1001)
    elapsed = time.time() - start_time
    print("The result is {0}, found in {1} seconds".format(result, elapsed))

if __name__ == '__main__':
    main()
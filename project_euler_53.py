"""
    Project Euler 53: Combinatoric selections

    There are exactly ten ways of selecting three from five, 12345:
        123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

    In combinatorics, we use the notation, 5C3 = 10.

    In general,
        nCr = n!/(r!(n−r)!) where r ≤ n, n! = n * (n−1) * ... * 3 * 2 * 1, and 0! = 1.

    It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

    How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than
    one-million?
"""
import math
import time


# A Pascal triangle looks like this:
#   1
#   1 1
#   1 2 1
#   1 3 3 1
#   1 4 6 4 1
# Where:
#   The row number indicates n, the column number indicates r. Both n and r start from 0
#   The first item in each round is 1
#   From the second row, each item is the sum of two items in the previous round, one in
#   the previous column, and the other one in the same column with the resulting item.
def use_pascal_triangle(number, limit):
    """
    Use Pascal triangle to find the number of values nCr where nCr < limit
    Ref: Pascal triangle and combinations
    https://en.wikipedia.org/wiki/Pascal%27s_triangle#Combinations

    :param number:
    :param limit:
    :return: the number of nCr that satisfies the condition
    """
    result = 0

    # Pascal triangle represented as list of list. Each sublist represents one row of the triangle
    pascal_triangle = []
    # Pascal triangle row 0
    row_0 = [1] + [0] * number
    pascal_triangle.append(row_0)

    for r in range(1, number + 1):
        # First item (column) in each row
        triangle_row = [1]
        # Finding other items (other columns) in each row
        for i in range(1, number + 1):
            item = pascal_triangle[r - 1][i - 1] + pascal_triangle[r - 1][i]
            triangle_row.append(item)

            if item > limit:
                result += 1

        # Finish calculating one row, add to the Pascal triangle
        # We use this new value to calculate the next round
        pascal_triangle.append(triangle_row)

    return result


def use_brute_force(n, limit):
    """
    Use brute force method to find the number of nCr where nCr < limit.

    :param n:
    :param limit:
    :return: number of values satisfying the condition
    """
    result = 0

    for r in range(n + 1):
        for i in range(r + 1):
            combinatoric_value = math.factorial(r) / (math.factorial(r - i)
                                                      * math.factorial(i))

            if combinatoric_value > limit:
                result += 1

    return result


def main():
    """
    Test
    """
    n = 100
    limit = 1000000

    # Use Pascal triangle
    start_time = time.time()
    result = use_pascal_triangle(n, limit)
    print("Pascal triangle: The result is {0}, found in {1} seconds"
          .format(result, time.time() - start_time))

    # Use brute force. The performance between this method and Pascal triangle appears with
    # larger n e.g. n = 1000
    start_time = time.time()
    result = use_brute_force(n, limit)
    print("Brute force method: The result is {0}, found in {1} seconds"
          .format(result, time.time() - start_time))


if __name__ == "__main__":
    main()

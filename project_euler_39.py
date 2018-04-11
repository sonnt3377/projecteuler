"""
    Project Euler 39: Integer right triangles

    If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three
    solutions for p = 120.

    {20,48,52}, {24,45,51}, {30,40,50}

    For which value of p <= 1000, is the number of solutions maximised?
"""
import time


def find_number_of_solutions(p):
    """
    Find the number of solutions for certain value of the perimeter p

    :param p: perimeter of the right triangle
    :return: the number of solutions for that triangle
    """
    """
    Analysis: consider a, b, c are three sides of the triangle, where a is the largest side, then
        1. a + b + c = p
        2. a < b + c
        3. b^2 + c^2 = a^2
    Some relation between them:
        c <= b < a < p/2
        c < p/3 (since c is the smallest side)
    """
    # Initially, we do not have any solution at all
    number_of_solutions = 0

    # Brute force using the constraints above
    for c in range(1, p // 3 + 1):
        for b in range(1, p // 2 + 1):
            a = p - b - c
            if a * a == b * b + c * c:
                number_of_solutions += 1

    return number_of_solutions


def find_optimal_p(limit):
    """
    Find the value of p less than a limit with max number of solutions

    :return: p value
    """
    max_number_of_solutions = 0
    result = 0

    for p in range(1, limit):
        number_of_solutions = find_number_of_solutions(p)
        if number_of_solutions > max_number_of_solutions:
            max_number_of_solutions = number_of_solutions
            result = p

    return result


def find_optimal_p_2(limit):
    """
    Another way to find the value of p less than a limit with max number of solutions.

    :return: p value
    """
    """
    Analysis: consider a, b, c are three sides of the triangle, where a is the largest side, then
        1. a + b + c = p
        2. a < b + c
        3. b^2 + c^2 = a^2
    Some relation between them:
        c <= b < a < p/2
        c < p/3 (since c is the smallest side)

    From 1, a = p - b - c, replace in 3, then b^2 + c^2 = (p - b - c)^2 = p^2 + b^2 + c^2 - 2bp - 2cp + 2bc
    then b = (p^2 - 2cp)/(2p - 2c) is an integer, where p < 1000, and c < p/3

    Also from 1 and 3, we see that:
        If b AND c are odd, then a is even, then p is even
        If b AND c are even, then a is even, then p is even
        If b OR c are odd, then a is odd, then p is even.
    So we only need to search for p is even
    """
    max_number_of_solutions = 0
    result = 0

    for p in range(2, limit, 2):
        number_of_solutions = 0

        for c in range(1, p // 3 + 1):
            # Check if b is an integer
            if (p * p - 2 * c * p) % (2 * p - 2 * c) == 0:
                number_of_solutions += 1

        if number_of_solutions > max_number_of_solutions:
            max_number_of_solutions = number_of_solutions
            result = p

    return result


def main():
    input_number = 1000

    # Running time ~ O(n^3)
    start_time = time.time()
    result = find_optimal_p(input_number)
    print("Method 1: Result is {0}, found in {1} seconds".format(result, time.time() - start_time))

    # Running time ~ O(n^2)
    start_time = time.time()
    result = find_optimal_p_2(input_number)
    print("Method 2: Result is {0}, found in {1} seconds".format(result, time.time() - start_time))


if __name__ == "__main__":
    main()

"""
    Project Euler 52: Permuted multiples

    It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a
    different order.

    Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""
import time


def is_permutation(number1, number2):
    """
    Decide if two numbers are permutation of each other

    :param number1:
    :param number2:
    :return: True if two numbers are permutation of each other, False otherwise
    """
    # Identical numbers
    if number1 == number2:
        return False

    list1 = list(str(number1))
    list2 = list(str(number2))

    # If two numbers are of different size, they are not permutation of each other
    if len(list1) != len(list2):
        return False

    # Check if the digits are the same
    if set(list1) == set(list2):
        return True

    return False


def find_the_number():
    """
    Find the smallest number satisfies the condition

    :return: the number
    """
    """
        Analysis:
            If n is the smallest integer with such property, then the first digit of n should be 1, because otherwise, 
            6 * n will have more digits than n.
            More precisely, the range of possible values of n cannot exceed  10 * n / 6 because  6 * n will have more 
            digits otherwise.
            
            To find the solution, we search for all numbers n, from that with 1 digit and get larger, until we find a 
            solution. The only constraint is mentioned above.
    """
    smallest_number = 1
    is_result_found = False

    # Run until find a result
    while is_result_found is False:
        # Increase n by one digit
        smallest_number *= 10

        # Looping for all possible n values satisfying the above constraint
        for i in range(smallest_number, int(smallest_number * 10 / 6) + 1):
            # Assuming we find the result, unless proved otherwise
            is_result_found = True
            # Checking 2 * n, 3 * n, ..., 6 * n
            for j in range(2, 7):
                # If the multiply is not permuted, no need to check for other multiply
                # Try the next number n
                if is_permutation(i, j * i) is False:
                    is_result_found = False
                    break

            # If found then stop since this is the smallest number with such property
            if is_result_found:
                smallest_number = i
                break

    return smallest_number


def main():
    start_time = time.time()
    result = find_the_number()
    print("The result is {0}, found in {1} seconds".format(result, time.time() - start_time))


if __name__ == "__main__":
    main()

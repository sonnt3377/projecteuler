"""
    Project Euler 25: 1000-digit Fibonacci number

    The Fibonacci sequence is defined by the recurrence relation:
    Fn = F(n-1) + F(n-2), where F1 = 1 and F2 = 1.
    Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

    The 12th term, F12, is the first term to contain three digits.

    What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
import time


def num_digits(number):
    """
    Count the number of digit in a number

    :param number: input number
    :return: the number of digit that number contains
    """
    count = 0

    while number > 0:
        count += 1
        number = number // 10

    return count


def main():
    """
    Test function
    """
    start_time = time.time()

    # The list contains the first 3 Fibonacci numbers in the beginning
    # This list will hold the last 3 Fibonacci numbers at any step. To calculate a next Fibonacci number, we replace
    # this list's items with the three new to avoid recursive call to calculate Fibonacci numbers.
    fibonacci_list = [1, 1, 2]
    # Index of the last Fibonacci number in the list. This will be the index of the item with 1000 digits when the
    # condition hits
    result_index = 3

    # Repeatedly calculate new Fibonacci numbers, and checking for 1000-digit hit
    while num_digits(fibonacci_list[2]) < 1000:
        fibonacci_list[0] = fibonacci_list[1]
        temp = fibonacci_list[1]
        fibonacci_list[1] = fibonacci_list[2]
        fibonacci_list[2] = fibonacci_list[2] + temp
        # Update the index of the latest Fibonacci number.
        # Though this index in the list is still 2 i.e. the third number, the 'index' in this context is the actual
        # position
        # of a number in a full Fibonacci list.
        result_index += 1

    print("Result is {0}, found in {1} seconds".format(result_index, time.time() - start_time))


if __name__ == "__main__":
    main()

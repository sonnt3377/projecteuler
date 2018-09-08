"""
    Project Euler 26: Reciprocal cycles

    A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2
    to 10 are given:
    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1
    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring
    cycle.

    Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""
import time


def find_recurring_cycle(number):
    """
    Find the recurring cycle of the faction 1/number

    :param number: input number
    :return: the number of digit representing the recurring cycle
    """
    # List indexes indicate remainders of 1/n operation at a certain point.
    # The list value at a corresponding division_counts indicates the number of division operation so far.
    # This list should only have maximum n items because a remainder cannot be larger than the number n
    remainders = [0] * number

    # Initial nominator since we need to find 1/n
    nominator = 1

    # List division_counts to hold the remainder at each division step
    division_counts = 0

    # If remainders[nominator] != 0
    # It means result of the latest division creates the same remainder as one of the previous
    # operations, and the cycle will start from this point.
    # In the worst case, this will go through the whole list before it repeats
    #
    # If nominator == 0
    # It means the division result is not indefinite and we just stop.
    try:
        while remainders[nominator] == 0 and nominator != 0:
            remainders[nominator] = division_counts
            # Prepare nominator for the next division step
            nominator *= 10
            # Divide and get new nominator
            nominator %= number
            division_counts += 1
    except IndexError:
        print("Index out of range.")
        print("Total number of list items is {0}, index is {1}".format(number, nominator))

    return division_counts - 1


def find_max_recurring_cycle(num):
    """
    Find the max recurring cycle for number less than or equal num

    :param num: input number
    :return: max recurring cycle and the corresponding number
    """
    max_recurring_cycle = 0
    resulting_number = 0

    for i in range(num, 1, -1):
        # We found the recurring_cycle already, do not need to test smaller number
        if i <= max_recurring_cycle:
            break

        recurring_cycle = find_recurring_cycle(i)

        # If we find a number with longer recurring cycle, update it
        if max_recurring_cycle < recurring_cycle:
            max_recurring_cycle = recurring_cycle
            resulting_number = i

    return max_recurring_cycle, resulting_number


def main():
    """
    Test function
    """
    number = int(input('Enter the integer number: '))
    start_time = time.time()
    output = find_max_recurring_cycle(number)
    max_recurring_cycle = output[0]
    result_number = output[1]

    print("The longest recurring cycle for 1/d where d < {0} is {1}. The number is {2}".format(number, max_recurring_cycle,
                                                                                               result_number))
    print("Result found in {0} seconds".format(time.time() - start_time))


if __name__ == "__main__":
    main()

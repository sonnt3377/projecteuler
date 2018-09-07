"""
    Project Euler 18

    By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total
    from top to bottom is 23.

    3
    7 4
    2 4 6
    8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom of the triangle below:

    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

    NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However,
    Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force,
    and requires a clever method! ;o)

"""
import time


def recursive_sum(input_data, row_number):
    """
    A recursive function to create sums from certain row upward.

    :param input_data:
    :param row_number: row number to start the recursive with, then work upward
    :return:
    """
    for i in range(len(input_data[row_number])):
        # Find the sums of the item with its lower left and lower right items (the row below)
        # Then replace this item with the larger of the sum
        input_data[row_number][i] += max([input_data[row_number + 1][i], input_data[row_number + 1][i + 1]])

    # If it is the top row, then we are done
    if len(input_data[row_number]) == 1:
        return input_data[row_number][0]

    # If not the top row, then use recursive
    return recursive_sum(input_data, row_number - 1)


def main():
    """
    Test method
    """
    # Loading lines of data into list, each list item is one line
    rows = []
    with open("project_euler_18_data") as file:
        for line in file:
            rows.append([int(i) for i in line.rstrip('\n').split(" ")])

    start = time.time()
    result = recursive_sum(rows, len(rows) - 2)  # start from second to last row, then work upward
    elapsed = time.time() - start

    print("{0} found in {1:.8f} seconds".format(result, elapsed))

if __name__ == '__main__':
    main()
